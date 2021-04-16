#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

dn={}
infile=sys.argv[1]
outdir=sys.argv[2]
out=os.path.join(outdir,"result.xls")
outopen=open(out, "w")
head="chr_id\ttype\tstart\tend\tgene_id\ttranscript_id\tT1\tM1\tM2\tM3\tT2\tT3\n"
outopen.write(head)
for lin in open(sys.argv[3], "r").readlines()[1:]:
	lst=lin.strip().split("\t")
	dn[lst[0]]="\t".join(lst[1:])

for line in open(infile, "r").readlines()[2:]:
	lst=line.strip().split("\t")
	ch=lst[0]
	ty=lst[2]
	start=lst[3]
	end=lst[4]
	gene_id=lst[-1].split('\"')[1]
	transcript_id=lst[-1].split('\"')[3]
	if ty == "transcript" and transcript_id.startswith("MS"):
			if transcript_id in dn.keys():
				outopen.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (ch,ty,start,end,gene_id,transcript_id,dn[transcript_id].split("\t")[0],
					dn[transcript_id].split("\t")[1],
					dn[transcript_id].split("\t")[2],
					dn[transcript_id].split("\t")[3],
					dn[transcript_id].split("\t")[4],
					dn[transcript_id].split("\t")[5]))
			else:
				outopen.write("%s\t%s\t%s\t%s\t%s\t%s0\t0\t0\t0\t0\t0\n" % (ch,ty,start,end,gene_id,transcript_id))
outopen.close()