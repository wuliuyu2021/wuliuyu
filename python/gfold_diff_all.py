#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse



def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to make gfold diff csvs.')
	parser.add_argument('-i','--indir',dest='indir', required=True, help='The input directory contains all sample files')
		
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains all result files')
	
	args = parser.parse_args()
	
	return args

def info_write(indir, outdir):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	head="AccID\tlog2FC\n"
	pattern = re.compile(r"(.+)(.diff)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		samcsv=os.path.join(outdir ,"%s.all.txt" % os.path.basename(sr).split(".diff")[0])
		samopen=open(samcsv, "w")
		samopen.write(head)
		for line in open(indir+"/"+sr, "r").readlines()[11:]:
			lst=line.strip().split("\t")
			if lst[2] == "0" :
				continue
			else:
				samopen.write("%s\t%s\n"% (lst[1], lst[2]))
		samopen.close()



def main():
	args = getCommands()
	indir, outdir=args.indir,args.outdir
	info_write(indir, outdir)
	

	

if __name__ == "__main__":
	main()
