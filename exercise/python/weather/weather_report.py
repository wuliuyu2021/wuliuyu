#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
import smtplib
import urllib
from email.mime.text import MIMEText
import json
from email.header import Header
from city import citycode


 

cityname = raw_input('你想查哪个城市的天气？')

print cityname

cityc = citycode.get(cityname)

print cityc

if cityc:

   url = ('http://www.weather.com.cn/weather1d/%s.shtml' % cityc)

   print url

   content = urllib2.urlopen(url).read()

   print content

else:

   print "城市名不存在"

fromaddr = "695953608@qq.com"
toaddr = "1261225782@qq.com"
body = "%s" % content
msg=MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = "今天上饶天气预报"
msg['From'] = fromaddr
msg['To'] = toaddr
try:
	server = smtplib.SMTP("smtp.qq.com")
	server.connect(fromaddr, 465)
	server.login(fromaddr, "WULIUXIN20110801")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print "邮件发送成功"
except:
	print "Error:无法发送邮件"