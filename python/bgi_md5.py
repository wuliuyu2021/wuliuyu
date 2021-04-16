#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
indir=sys.argv[1]
outdir= sys.argv[2]
md5=os.path.join(outdir, 'md5.txt')
if os.path.exists(md5):
	os.remove(md5)
md5cat=open(md5, 'a')


for root,ds,fs in os.walk(indir):
	fs.sort()
	for f in fs:
		if f.endswith('md5'):
			for line in open('%s/%s' %(indir, f)):
				lst=line.strip().split("  ")
				md5code = lst[0]
				md5path = lst[1]
				md5file = '_'.join(md5path.split("/")[-1].split("_")[2:])
				md5cat.write("%s  Rawdata/%s/%s\n" % (md5code, md5path.split("/")[-1].split("_")[2], md5file))
md5cat.close()
#修改