#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from collections import Counter
#from optparse import OptionParser
import pandas as pd
import numpy as np
import math

indir=sys.argv[1]
log2FC=sys.argv[2]
pvalue=sys.argv[3]
outdir=sys.argv[4]

pattern = re.compile(r"(.+)(.All.txt)$")
srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))

for sr in srs:
	out=os.path.join(outdir, "%s.log2FC%s.Pvalue%s.txt" % (os.path.basename(sr).split(".All.txt")[0], log2FC, pvalue))
	out_open=open(out, "w")
	head_prefix=open(indir+"/"+sr, "r").readlines()[0]
	head="%s\t%s\t%s\t%s\tStyle\t%s" % (head_prefix.split("\t")[0],head_prefix.split("\t")[1],head_prefix.split("\t")[2],head_prefix.split("\t")[3],"\t".join(head_prefix.split("\t")[4:]))
	out_open.write(head)
	print(head)
	for line in open(indir +"/"+ sr, 'r').readlines()[1:]:
		lst = line.strip().split("\t")
		if str(lst[1]) == "NA" or str(lst[2]) == "NA":
			continue
		if  float(lst[1]) > float(log2FC) or  float(lst[1]) < -float(log2FC):
			if  float(lst[2]) < float(pvalue) and float(lst[1]) > 0:
				#print(float(lst[1]))
				out_open.write("%s\t%s\t%s\t%s\tup\t%s\n" %(lst[0],lst[1],lst[2],lst[3],"\t".join(lst[4:])))
			if float(lst[2]) < float(pvalue) and float(lst[1]) < 0:
				out_open.write("%s\t%s\t%s\t%s\tdown\t%s\n" %(lst[0],lst[1],lst[2],lst[3],"\t".join(lst[4:])))
	out_open.close()