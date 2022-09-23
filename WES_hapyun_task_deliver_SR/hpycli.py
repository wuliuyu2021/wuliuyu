#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import sys
import re
import csv
import json
import urllib2
import getpass
from plumbum import cli
from collections import namedtuple
from optparse import OptionParser
from pexpect import pxssh
from os.path import expanduser, isfile
import configparser

ENDPOINT='https://api.hapyun.com'

def parseCommand():
    usage = "usage:  %prog <-t tpl> <-c param> <-u username> <-p password> "
    version = "%prog 1.0"
    parser  = OptionParser(usage = usage, version =version)
    parser.add_option("-t", "--tpl", dest = "tpl", help = "workflow_tpl.json")
    parser.add_option("-c", "--param",  dest = "param",  help = "param.csv")
    parser.add_option("-u", "--username",  dest = "username",  help = "username")
    parser.add_option("-p", "--password",  dest = "password",  help = "password")
    return parser.parse_args()

def getToken(username, password):
    url = ENDPOINT + '/account/login'
    data = json.dumps({'username': username, 'password': password})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    json_response = json.loads(f.read())
    f.close()
    # print json_response['token']
    return json_response['token']

def parseTpl(tplFile):
    paramKeys = []
    file_object = open(tplFile, 'r') #创建一个文件对象，也是一个可迭代对象
    try:
        all_the_text = file_object.read()  #结果为str类型
        # print all_the_text
        resList = re.findall(r"(<\$([^>]+)>)", all_the_text)
        if resList:
            for i in resList:
                paramKeys.append(i[1])
        if paramKeys:
            paramKeys = list(set(paramKeys))
    finally:
        file_object.close()

    # print paramKeys
    return all_the_text, paramKeys

def readFile(file):
    contents = ''
    file_object = open(file, 'r')
    try:
        contents = file_object.read()
    finally:
        file_object.close()

    return contents


def parseParam(csvFile, paramKeys):
    rows = []
    with open(csvFile) as f:
        h_csv = csv.reader(f)
        headers = next(h_csv)
        print headers
        for i in paramKeys:
            if i not in headers:
                print ("Fatal: %s is not in headers") % i
                sys.exit(-1)

    with open(csvFile) as f:
        f_csv = csv.DictReader(f,skipinitialspace=True)
        for row in f_csv:
            # print row
            for i in paramKeys:
                if not row['sample']:
                    print ("Fatal: %s value is empty") % i
                    sys.exit(-1)
            rows.append(row)
    return rows

def getParamConfig(row, json_txt, paramKeys):
    for i in paramKeys:
        json_txt = json_txt.replace('<$'+i+'>', row[i])
    # print json_txt
    return json.loads(json_txt)

def getWorkflowTpl(workflowName, workflowVersion, token):
    url = ENDPOINT + '/api/workflowparameter/' +workflowName+ '?id=' +workflowName+ '&workflow_version=' +workflowVersion
    req = urllib2.Request(url, None, {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token})
    try:
        f = urllib2.urlopen(req)
        json_response = f.read()
        f.close()
        # print json_response
        return json_response
    except urllib2.HTTPError, e:
        # print(str(e))
        return 'Error: ' + str(e.code) + ' ' + e.read()

def createJob(configJson, token, region='sz'):
    url = ENDPOINT + '/' +region+ '-api/tasks'
    data = json.dumps(configJson)
    req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token})
    try:
        f = urllib2.urlopen(req)
        json_response = f.read()
        f.close()
        # print json_response
        return json_response
    except urllib2.HTTPError, e:
        # print(str(e))
        return 'Error: ' + str(e.code) + ' ' + e.read()


def getConfig():
    ep = ''
    user = ''
    token = ''
    configfile = expanduser("~") + '/.hapyunconfig'
    if isfile(configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        if 'Credentials' in config:
            Credentials = config['Credentials']
            ep = Credentials.get('endpoint')
            user = Credentials.get('username')
            token = Credentials.get('token')
    return ep, user, token

def checkToken(token):
    url = ENDPOINT + '/account/me'
    req = urllib2.Request(url, None, {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token})
    try:
        f = urllib2.urlopen(req)
        contents = f.read()
        response_code = f.getcode()
        f.close()
        return response_code == 200
    except urllib2.HTTPError, e:
        # print(str(e))
        return False

class HapyunCli(cli.Application):
    """The HapyunCli version control"""
    VERSION = "1.0.0"

    # auto_add = cli.Flag("-a", help = "automatically add changed files")

    def main(self, *args):
        # print "version: " + self.VERSION
        ep, user, token = getConfig()
        if not checkToken(token):
            print "Session expired. Please try login again"

@HapyunCli.subcommand("tpl")
class HapyunTpl(cli.Application):
    # auto_add = cli.Flag("-a", help = "automatically add changed files")
    workflowName = cli.SwitchAttr("-w", str, mandatory = True, help = "sets the workflow name")
    workflowVersion = cli.SwitchAttr("--wv", str, mandatory = False, help = "sets the version of workflow, default is 1", default = "1")

    def main(self, *args):
        # (options, args) = parseCommand()
        ep, user, token = getConfig()
        if checkToken(token):
            json_response = getWorkflowTpl(self.workflowName, self.workflowVersion, token)

            # replace "enid": "<Please input the enid of the data in here>",
            json_response = json_response.replace('"<Please input the enid of the data in here>"', 'null')
            json_response = json_response.replace('"<Please input the reference task\'s id>"', 'null')
            json_response = json_response.replace('<Please input the task\'s description in here>', '')
            json_orgin = json.loads(json_response)

            task_name = self.workflowName + '_<Please input the sample name>'
            json_object = {
                'task_name': task_name,
                'name': self.workflowName,
                'workflow_name': self.workflowName,
                'workflow_version': int(self.workflowVersion),
                'emergency': False
            }
            # transform the fields
            json_object['parameters'] = json_orgin['parameter']
            json_object['parameters']['name'] = task_name

            print json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))
            # print ("get workflow input template : %s") % (json_response)
        else:
            print "Session expired. Please try login again"

@HapyunCli.subcommand("run")
class HapyunRun(cli.Application):
    # auto_add = cli.Flag("-a", help = "automatically add changed files")
    params = cli.SwitchAttr("-p", str, mandatory = True, help = "sets the tpl_params.json file path")
    region = cli.SwitchAttr("-r", str, mandatory = False, help = "sets the job run region: sz or bj", default = "sz")

    def main(self, *args):
        # (options, args) = parseCommand()
        if self.region == "bj":
            print "waring: 当前任务运行在北京域"
        elif self.region != "sz":
            print "error: 当前任务运行在不支持的区域：" + self.region
            sys.exit(-1)

        ep, user, token = getConfig()
        if checkToken(token):
            paramConfigJson = json.loads(readFile(self.params))
            json_response = createJob(paramConfigJson, token, self.region)
            print ("create %s Job: %s result: %s") % (self.region, paramConfigJson['task_name'], json_response)
        else:
            print "Session expired. Please try login again"

@HapyunCli.subcommand("batch")
class HapyunBatch(cli.Application):
    # auto_add = cli.Flag("-a", help = "automatically add changed files")
    tpl = cli.SwitchAttr("-t", str, mandatory = True, help = "sets the workflow_tpl.json file path")
    param = cli.SwitchAttr("-c", str, mandatory = True, help = "sets the param.csv file path")
    region = cli.SwitchAttr("-r", str, mandatory = False, help = "sets the job run region: sz or bj", default = "sz")

    def main(self, *args):
        # (options, args) = parseCommand()
        if self.region == "bj":
            print "waring: 当前任务运行在北京域"
        elif self.region != "sz":
            print "error: 当前任务运行在不支持的区域：" + self.region
            sys.exit(-1)

        ep, user, token = getConfig()
        if checkToken(token):
            json_txt, paramKeys = parseTpl(self.tpl)
            rows = parseParam(self.param, paramKeys)

            for row in rows:
                paramConfigJson = getParamConfig(row, json_txt, paramKeys)
                # print json.dumps(paramConfigJson)
                json_response = createJob(paramConfigJson, token, self.region)
                print ("create %s Job: %s result: %s") % (self.region, paramConfigJson['task_name'], json_response)
                # sys.exit(-1)
        else:
            print "Session expired. Please try login again"

@HapyunCli.subcommand("login")
class HapyunLogin(cli.Application):
    """login in store token"""

    def main(self):
        ep, user, token = getConfig()
        try:
            s = pxssh.pxssh()
            # endpoint = raw_input('Endpoint['+ENDPOINT+']:') or ENDPOINT
            if user:
                username = raw_input('Username['+user+']:') or user
            else:
                username = raw_input('Username:')
            password = getpass.getpass('Password:')

            token = getToken(username, password)
            if token:
                # save to ~/.hapyunconfig
                configfile = expanduser("~") + '/.hapyunconfig'
                configcontent = "[Credentials]\nendpoint="+ENDPOINT+"\nusername="+username+"\ntoken=" + token + "\n"
                with open(configfile, 'w') as file:
                    file.write(configcontent)
                print('login success.')
                return 0
            print('failed on login.')
            return 1
        except pxssh.ExceptionPxssh, e:
            print('failed on login.')
            print('Error: ' + str(e.code) + ' ' + e.read())

if __name__ == "__main__":
    HapyunCli.run()
