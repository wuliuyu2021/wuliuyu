#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

dt=[]
#out=os.path.join("%s/%s.%s.diff.gene.xls" %(sys.argv[4], os.path.basename(sys.argv[1]), sys.argv[2]))#file name
#out_open=open(out,"w")
for line in open(sys.argv[1], "r").readlines()[0:]:#path csv
	lst=line.strip().split("\t")
	lst[0]=dt[lst[1]]
print(dt)
pattern = re.compile(r"(.+)(.network.txt)$")
srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(sys.argv[1])))
for sr in srs:

head_list=open(sys.argv[3], "r").readlines()[0]
head="\t".join(head_list.split("\t"))
out_open.write(head)
for line in open(sys.argv[3], "r").readlines()[1:]:
	lst=line.strip().split("\t")
	if lst[0] in sorted(set(lts)):
		out_open.write("%s\n" % "\t".join(lst))
		
out_open.close()