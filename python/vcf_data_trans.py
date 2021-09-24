#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

csv=sys.argv[1]
out=sys.argv[2]

outfile=os.path.join(out, "%s_tmp" % os.path.basename(csv))
#fcid=os.path.basename(csv).split(".csv")[0].split("sequence_")[-1]
#if os.path.exists(outfile):
#	os.remove(outfile)
outopen=open(outfile, "w")

for line in open(csv, "r", encoding='gbk').readlines()[0:]:
	lst=line.strip().split(",")
	if lst[27].find("vcf") != -1:
		print("%s: %s-%s-%s" % (lst[0],lst[1],lst[16],lst[18]))
		if lst[2].find(str(lst[16])) != -1 and lst[2].find(str(lst[18])) != -1:
			continue
		else:	
			outopen.write("%s,%s-%s-%s,%s\n" % (lst[0],lst[1],lst[16],lst[18],",".join(lst[2:])))
	else:
		outopen.write(",".join(lst[0:])+"\n")
outopen.close()

os.system("iconv -f utf-8 -t gbk %s -o %s/%s" % (outfile, out, os.path.basename(csv)))
