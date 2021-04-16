#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re



lts=[]
out=os.path.join(sys.argv[3],"gene.xls")
out_open=open(out,"w")
head_list=open(sys.argv[1], "r").readlines()[0]
head="\t".join(head_list.split("\t"))
out_open.write(head)
for line in open(sys.argv[2], "r"):
	lst=line.strip().split("\n")
	lts.append(lst[0])
for line in open(sys.argv[1], "r").readlines()[1:]:

	lst=line.strip().split("\t")
	if lst[0] in lts:
		out_open.write("%s\n" % "\t".join(lst))
		
out_open.close()