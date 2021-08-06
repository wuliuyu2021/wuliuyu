#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

infile=sys.argv[1]
indir=sys.argv[2]
outdir=sys.argv[3]

def dict_maker(infile):
	dt={}
	for line in open(infile, "r").readlines()[:]:#path csv
		lst=line.strip().split("\t")
		lst[0]=dt[lst[1]]
	return dt
	print(dt)


def info_write(indir,outdir):
	dt=dict_maker(infile)
	pattern = re.compile(r"(.+)(.network.txt)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		file=os.path.join(outdir,"%s_result.txt" % os.path.basename(sr))
		file_open=open(file, "w")
		head=open(indir+"/"+sr, "r").readlines()[0]
		file_open.write(head+"\n")
		for i,element in enumerate(head):
			x=""
			if element == "to":
				x=int(i)
		for line in open(indir+"/"+sr, "r").readlines()[1:]:
			lst=line.strip().split("\t")
			if lst[x] not in dt.keys():
				file_open.write(line+"\n")
			else:
				file_open.write("\t".join(lst[0:x])+"\t"+"\t".join(lst[(x+1):]+"\n"))
		file_open.close()

def main():
	infile=sys.argv[1]
	indir=sys.argv[2]
	outdir=sys.argv[3]
	info_write(indir,outdir)

if __name__ == '__main__':
	main()