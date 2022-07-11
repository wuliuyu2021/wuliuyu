#!/usr/bin/python
# -*- coding:utf-8 -*-
from dingtalkchatbot.chatbot import DingtalkChatbot
import sys
#zj="18702215856"
#fxq="15579320613"
#wly="13732927526"
#yqx="18070596187"
#hp="19907900057"
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=9a4ec03d21a840f399e7e92b6e3f9544fff5e4a062f3b6bcd2f52be98065146d'
webhook2 = "https://oapi.dingtalk.com/robot/send?access_token=2232ce68dc30d6e6b0912574101081ea6c1c1ece9d049d3b3a36c6bd7e2b3044"
xiaoding = DingtalkChatbot(webhook2)
if sys.argv[2] == 'zj':
	at_mobiles = ["18702215856"]
if sys.argv[2] == 'fxq':
	at_mobiles = ["15579320613"]
if sys.argv[2] == 'wly':
	at_mobiles = ["13732927526"]
if sys.argv[2] == 'yqx':
	at_mobiles = ["18070596187"]
if sys.argv[2] == 'yzx':
	at_mobiles = ["18379867231"]
if sys.argv[2] == 'lsy':
	at_mobiles = ["18679857621"]
if sys.argv[2] == 'hxq':
	at_mobiles = ["18270374396"]
#print(at_mobiles)
text_pre=sys.argv[1]
'''if  "," in text_pre and "/n"  in text_pre:
	text=text_pre.replace(","," ").replace("/n","\n")
elif "," in text_pre:
	text=text_pre.replace(","," ")
elif "/n"  in text_pre:
	text=text_pre.replace("/n","\n")
elif  "," not in text_pre and "/n" not in text_pre:
	text=text_pre
print(text)'''
text=text_pre
xiaoding.send_text(msg=text,at_mobiles=at_mobiles)
