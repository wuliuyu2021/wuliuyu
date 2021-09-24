#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

csv=sys.argv[1]
out=sys.argv[2]

outfile=os.path.join(out, "%s_tmp" % os.path.basename(csv))
#if os.path.exists(outfile):
#	os.remove(outfile)
outopen=open(outfile, "w")

for line in open(csv, encoding='gbk').readlines()[0:]:
	lst=line.strip().split(",")
	if lst[27].find("vcf") != -1:
		print("%s-%s-%s" % (lst[1],lst[16],lst[18]))
		outopen.write("%s,%s-%s-%s,%s\n" % (lst[0],lst[1],lst[16],lst[18],",".join(lst[2:])))
	else:
		outopen.write(",".join(lst[0:])+"\n")
outopen.close()

os.system("mv %s/%s %s/%s_old" % (out, csv, out, os.path.basename(csv)))
os.system("mv %s %s/%s" % (outfile, out, os.path.basename(csv)))