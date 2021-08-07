#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

def dict_maker(infile):
	dt={}
	for line in open(infile, "r").readlines()[:]:#path csv
		lst=line.strip().split("\t")
		dt[lst[0]]=lst[1]
	#print(dt)
	return dt
	
def info_write(infile,indir,outdir):
	dt=dict_maker(infile)
	pattern = re.compile(r"(.+)(network.txt)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		dx={}
		x=""
		file=os.path.join(outdir,"%s_result.txt" % os.path.basename(sr))
		file_open=open(file, "w")
		head=open(indir+"/"+sr, "r").readlines()[0]
		head_list=open(indir+"/"+sr, "r").readlines()[0].strip().split("\t")
		file_open.write(head)
		for i,element in enumerate(head_list):
			dx[element]=i
		if "to" in dx.keys():
				x=dx["to"]
				print(x)
		for line in open(indir+"/"+sr, "r").readlines()[1:]:
			lst=line.strip().split("\t")
			y=int(x)
			if lst[y] not in dt.keys():
				file_open.write(line)
			else:
				file_open.write("\t".join(lst[0:y])+"\t"+lst[y]+"\t"+"\t".join(lst[(y+1):])+"\n")
		file_open.close()

def main():
	infile=sys.argv[1]
	indir=sys.argv[2]
	outdir=sys.argv[3]
	info_write(infile,indir,outdir)

if __name__ == '__main__':
	main()