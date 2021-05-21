#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
#sys.argv[1]:All.KEGG_Enrich.xls
#sys.argv[2]:pathwayname,hsa04010
#sys.argv[3]:diff_file,log2FC1.0.Pvalue0.05.txt
#sys.argv[4]:outdir
lts=[]
out=os.path.join("%s/%s.%s.diff.gene.xls" %(sys.argv[4], sys.argv[2], os.path.basename(sys.argv[1])))#file name
out_open=open(out,"w")
for line in open(sys.argv[1], "r").readlines()[1:]:#path csv

	lst=line.strip().split("\t")
	if  len(sys.argv[2].split(",")) == 1 and lst[0] == sys.argv[2]:#gene ID
		for gene in lst[7].split("/"):
			out_open.write("%s\n" % gene)
	if len(sys.argv[2].split(",")) > 1 and lst[0] in sys.argv[2].split(","):
		for path in sys.argv[2].split(","):
			for gene in lst[7].split("/"):
				lts.append(gene)
head_list=open(sys.argv[3], "r").readlines()[0]
head="\t".join(head_list.split("\t"))
for line in open(sys.argv[1], "r").readlines()[1:]:
	lst=line.strip().split("\t")
	if lst[0] in sorted(set(lts)):
		out_open.write("%s\n" % "\t".join(lst))
		
out_open.close()