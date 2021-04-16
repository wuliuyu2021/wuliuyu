#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import argparse

def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to figure out the mapp-rate between the mapping results.')
	parser.add_argument('-i','--input',type=str,dest='inputDir', required=True
				, help='The input directory contains all sample files')
	parser.add_argument('-o','--output',type=str,dest='outputDir',required=True
				, help='The output directory contains all result files')
	args = parser.parse_args()
	return args

def table_info(indir):
	lst=[]
	for root,ds,fs in os.walk(indir):
		for f in fs:
			if f.endswith("mapping.statistics.xls"):		
				lst.append(f)
	
	print(lst)

	return lst

def writer_info(indir, outdir):
	
	header="Sample\tAll\tMapped\tMappedRate\tUniqueMapped\tUniqueMappedRate"
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	tabs=table_info(indir)
	mapp=os.path.join(outdir, "mapping.xls")
	if os.path.exists(mapp):
		os.remove(mapp)
	mapp_open=open(mapp, "w")
	mapp_open.write(header+"\n")
	lt=[]
	for tab in tabs:
		
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")

				if lst[0] == "All":
					ltr=lst[0]+"\t"+lst[1]
					lt.append(ltr)
				if lst[0] == "Mapped":
					ltr=lst[0]+"\t"+lst[1]
					lt.append(ltr)
				if lst[0] == "MappedRate":
					ltr=lst[0]+"\t"+lst[1]
					lt.append(ltr)
				if lst[0] == "UniqueMapped":
					ltr=lst[0]+"\t"+lst[1]
					lt.append(ltr)
				if lst[0] == "UniqueMappedRate":
					ltr=lst[0]+"\t"+lst[1]
					lt.append(ltr)

		print(sorted(set(lt)))
		lit=sorted(set(lt))
		mapp_open.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (os.path.basename(tab).split(".mapping.statistics.xls")[0],lit[0].split("\t")[1], lit[1].split("\t")[1],lit[2].split("\t")[1],lit[3].split("\t")[1],lit[4].split("\t")[1]))
		lt=[]
	mapp_open.close()

def main():
	args = getCommands()
	indir = args.inputDir
	outdir = args.outputDir
	writer_info(indir, outdir)

if __name__ == '__main__':
	main()