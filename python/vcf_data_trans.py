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
		print("There is vcf sample: %s" % lst[0])
		if lst[18] == "" and lst[16] != "":
			#print(lst[2])
			if lst[1].find("%s" % str(lst[16])) != -1:
				#print(lst[0])
				outopen.write(",".join(lst[0:])+"\n")	
			else:	
				outopen.write("%s,%s-%s-%s,%s\n" % (lst[0],lst[1],lst[16],lst[18],",".join(lst[2:])))
		if lst[18] != "" and lst[16] != "":
			#print(lst[2])
			if lst[1].find("%s-%s" % (str(lst[16]), str(lst[18]))) != -1:
				#print(lst[0])
				outopen.write(",".join(lst[0:])+"\n")
			else:
				outopen.write("%s,%s-%s-%s,%s\n" % (lst[0],lst[1],lst[16],lst[18],",".join(lst[2:])))
		if lst[16] == "":
			print("Warning, %s:sampletype is null" % lst[0])
	else:
		outopen.write(",".join(lst[0:])+"\n")
outopen.close()

os.system("iconv -f utf-8 -t gbk %s -o %s/%s" % (outfile, out, os.path.basename(csv)))
os.system("rm -f %s" % outfile)
