# -*- coding: utf-8 -*-
import argparse
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
import smtplib

envf1="/data/users/wuliuyu/wuliuyu/cfg/.novastream_settings"
envf2="/thinker/nfs5/public/wuliuyu/wuliuyu/cfg/.novastream_settings"

def get_email_info():
    try:
        if os.path.exists(envf1):
            envf= envf1
        elif os.path.exists(envf2):
            envf= envf2
        else:
            print('Warning: no such file settings file.')
            raise FileNotFoundError
        with open(envf) as fp:
            d = json.load(fp)
            username = d.get('EHU')
            password = d.get('EHP')
            qctab_receiver_list = d.get('QctabReceiverList')
            osslink_receiver_list = d.get('OssLinkReceiverList')
        if not all([username, password, qctab_receiver_list, osslink_receiver_list]):
            print('Invalid value in [username, password, qctab_receiver_list, osslink_receiver_list].')
            raise ValueError
    except Exception as e:
        print(e)
        raise
    return username, password, qctab_receiver_list, osslink_receiver_list

def sendlinkcfg(username, password, sender, receiverlst, cclst, projectid, fname):
    # 邮件服务器设置
    smtpserver = 'smtp.exmail.qq.com'
    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver, 465)
    # 登录
    smtp.login(username, password)
    # 以下是邮件内容
    # 发件人邮箱
    sender = sender
    # 收件人邮箱
    receivers = receiverlst
    # 抄送
    ccs = cclst
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Cc'] = ','.join(ccs)
    subject = '%s数据下载链接' % projectid
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    text = '附件是%s数据下载链接，请注意查收。' % projectid
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    # 构造附件
    att1 = MIMEText(open(fname, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # 邮件中显示的文件名
    att1['Content-Disposition'] = 'attachment;filename="%s"' % os.path.basename(fname)
    message.attach(att1)
    # 发送
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def sendlink(projectid, fname, receiver):
    username, password, _, receiverlst = get_email_info()
    # username = 'datadelivery@haplox.com'
    # password = 'Srsz2020!'
    # sender = 'datadelivery@haplox.com'
    sender = username
    # receiverlst = ['project@haplox.com', 'longrw@haplox.com', 'wuliuyu@haplox.com']
    if receiver:
        receiverlst.append(receiver)
    # cclst = ['datadelivery@haplox.com']
    cclst = [username]
    receiverlst += cclst
    sendlinkcfg(username, password, sender, receiverlst, cclst, projectid, fname)
    print('Send successful!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--projectid', help='')
    parser.add_argument('-f', '--fname', help='the link file')
    parser.add_argument('-r', '--receiver', help='', default='')
    args = parser.parse_args()
    projectid = args.projectid
    fname = args.fname
    receiver = args.receiver
    sendlink(projectid, fname, receiver)
