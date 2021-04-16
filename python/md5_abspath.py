#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

d=sys.argv[1]
out=sys.argv[2]

for root,dirs,fs in os.walk(d):
	fs.sort()
	for f in fs:
		if f.endswith('gz'):
			os.system('md5sum %s/%s > %s/%s.md5' %(d,f,out,f))