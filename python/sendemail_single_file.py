# -*- coding: utf-8 -*-
import argparse
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib


def sendqctabcfg(username, password, sender, receiverlst, cclst, runid, fnames):
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
    subject = '%s质控表' % runid
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    text = '附件是%s质控表，请注意查收。' % runid
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    # 构造附件
    for fname in fnames:
        att1 = MIMEText(open(fname, 'rb').read(), 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        # 邮件中显示的文件名
        att1['Content-Disposition'] = 'attachment;filename="%s"' % os.path.basename(fname)
        message.attach(att1)
    # 发送
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def sendqctab(runid, fpath, receiver, fast=False):
    username = 'datadelivery@haplox.com'
    #password = 'Srsz2020!'
    password = 'rZkivHHGW9DAEUzQ'
    sender = 'datadelivery@haplox.com'
    receiverlst = ['project@haplox.com', 'longrw@haplox.com', 'wuliuyu@haplox.com']
    if receiver:
        receiverlst.append(receiver)
    cclst = ['project@haplox.com', 'longrw@haplox.com', 'wuliuyu@haplox.com', 'datadelivery@haplox.com']
    fnames = []
    if fast:
        fname1 = os.path.join(fpath, '%s_sample_qc_fast.csv' % runid)
        fname2 = os.path.join(fpath, '%s_lane_qc_fast.csv' % runid)
        if os.path.isfile(fname1):
            fnames.append(fname1)
        if os.path.isfile(fname2):
            fnames.append(fname2)
    else:
        fname1 = os.path.join(fpath, '%s_sample_qc.csv' % runid)
        fname2 = os.path.join(fpath, '%s_lane_qc.csv' % runid)
        if os.path.isfile(fname1):
            fnames.append(fname1)
        if os.path.isfile(fname2):
            fnames.append(fname2)
    sendqctabcfg(username, password, sender, receiverlst, cclst, runid, fnames)
    print('Send successful!')


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
    att1 = MIMEText(open(fname, 'rb').readline(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # 邮件中显示的文件名
    att1['Content-Disposition'] = 'attachment;filename="%s"' % os.path.basename(fname)
    message.attach(att1)
    # 发送
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def sendlink(projectid, fname, receiver):
    username = 'datadelivery@haplox.com'
    password = 'rZkivHHGW9DAEUzQ'
    sender = 'datadelivery@haplox.com'
    receiverlst = ['project@haplox.com', 'longrw@haplox.com', 'wuliuyu@haplox.com', 'yangzx@haplox.com']
    if receiver:
        receiverlst.append(receiver)
    cclst = ['project@haplox.com', 'longrw@haplox.com', 'wuliuyu@haplox.com', 'datadelivery@haplox.com']
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
