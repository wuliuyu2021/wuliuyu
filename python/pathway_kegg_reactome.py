#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
#sys.argv[1]:All.KEGG_Enrich.xls
#sys.argv[2]:genepathway,hsa04010
#sys.argv[3]:outdir
lts=[]
out=os.path.join("%s/%s.gene.list.xls",(sys.argv[3], os.path.basename(sys.argv[1])))#file name
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
for gene in sorted(set(lts)):
	out_open.write("%s\n" % gene)
		
out_open.close()