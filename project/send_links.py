#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header

dn = {'WXJ':'wuxj@haplox.com', 'WXQ':'wuxq@haplox.com', 'ZJ':'zhoujia@haplox.com', 'ZLC':'zenglc@haplox.com'}


def mail_info(seqcsv):
	lst, cp_nums=[], []
	for line in open(seqcsv):
		sample=Seqcsv(line.strip().split(','))
		cp_num="%s_%s" % (sample.contractID, sample.project_leader)
		cp_nums.append(cp_num)
	lst=list(set(cp_nums))
	print(lst)
	return lst

def right_receiver(seqcsv, contact_id):
	lsts=mail_info(seqcsv)
	for lst in lsts:
		if contact_id == lst.split('_')[0]:
			print(lst.split('_')[1])
			return lst.split('_')[1]

def writer_content(seq_ID, f):
	if os.path.exists(f):
		content = '你好！\n  附件为%s芯片,%s阿里云数据交付链接，请注意查收，及时发送给客户' % (seq_ID, os.path.basename(f).split('.link')[0])
		f_name = '%s' % os.path.basename(f)
	return content, f_name


def send_link(seqcsv, contact_id, f, seq_ID):
	person=right_receiver(seqcsv, contact_id)
	content=writer_content(seq_ID, f)[0]
	f_name=writer_content(seq_ID, f)[1]
	my_sender = "wuliuyu@haplox.com"
	my_pass = "Zhu19900907"
	my_receiver = "%s" % dn[person]
	msg = MIMEMultipart()
	msg['Subject'] = Header('阿里云交付链接邮件','utf-8').encode() 
	msg['From']=formataddr(["wuliuyu", my_sender])
	msg['To']= formataddr(["%s" % person, my_receiver])
	msg.attach(MIMEText(content,'plain','utf-8'))
	aliyun = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
	aliyun["Content-Type"] = 'application/octet-stream'
	aliyun["Content-Disposition"] = 'attachment;filename=' + f_name
	msg.attach(aliyun)
	try:
		server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
		server.login(my_sender, my_pass)
		text = msg.as_string()
		server.sendmail(my_sender, [my_sender] + [my_receiver], text)
		server.quit()
		print "邮件发送成功"
	except:
		print "Error:无法发送邮件"

if __name__ == '__main__':
	seq_ID=sys.argv[1]
	seqcsv=sys.argv[2]
	contact_id=sys.argv[3]
	f=sys.argv[4]
	send_link(seqcsv, contact_id, f, seq_ID)