#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re



lts=[]
out=os.path.join(sys.argv[3],"out.xls")
out_open=open(out,"w")
for line in open(sys.argv[1], "r").readlines()[1:]:

	lst=line.strip().split("\t")
	if  len(sys.argv[2].split(",")) == 1 and lst[0] == sys.argv[2]:
		for gene in lst[6].split("/"):
			out_open.write("%s\n" % gene)
	if len(sys.argv[2].split(",")) > 1 and lst[0] in sys.argv[2].split(","):
		for path in sys.argv[2].split(","):
			for gene in lst[6].split("/"):
				lts.append(gene)
for gene in sorted(set(lts)):
	out_open.write("%s\n" % gene)
		
out_open.close()