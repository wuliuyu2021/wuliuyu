#!/usr/bin python
# -*- coding: utf-8 -*-

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Pecheck(object):

	def __init__(self, json_f):
		data=json.load(json_f)
		self.read1_num=data["read1_num"]
		self.read2_num=data["read2_num"]
		self.read1_bases=data["read1_bases"]
		self.read2_bases=data["read2_bases"]
		self.result=data["result"]

if __name__ == '__main__':
	json_f=sys.argv[1]
	f=open(json_f, 'r')
	pecheck=Pecheck(f)