#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse
import json


def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to get stats json info.')
	parser.add_argument('-i','--indir',dest='indir', required=True, help='The input directory contains input files')
	#parser.add_argument('-i','--outdir',dest='outdir',required=True, help='The input directory contains all  files')
	
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains result files')
	
	args = parser.parse_args()
	
	return args

def get_jsons(indir):
	pattern = re.compile(r"(^Stats)(.+).json$")
	sjs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	return sjs

def info_write(indir, outdir):
	sjs=get_jsons(indir)
	for sj in sjs:
		f=open(sj)
		data=json.load(f)
		for sample in data["ConversionResults"]["DemuxResults"]["SampleName"]:
			print(sample)

def main():
	args = getCommands()
	indir, outdir=args.indir, args.outdir

	info_write(indir, outdir)
	

if __name__ == "__main__":
	main()
