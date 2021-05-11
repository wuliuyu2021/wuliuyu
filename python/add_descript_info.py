#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys, re, json, csv
import time
import argparse
import pandas as pd
import numpy as np

def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to add description to annofiles.')
	parser.add_argument('-d','--descript_file',type=str,dest='descript_file', required=True
				, help='The input description file')
	parser.add_argument('-n','--anno_file',type=str,dest='anno_file',required=True
				, help='The input anno file')
	parser.add_argument('-o', '--outdir', type=str,dest='outdir',required=True, help='The output dir')
	args = parser.parse_args()
	return args

def descript_file_info(des):
	dp={}
	with open(des, "r") as f:
		for line in f.readlines()[1:]:
			
			lst=line.strip().split("\t")
			
			
			if len(lst) < 2:
				dp[lst[0]]="NA"
			else:
				dp[lst[0]]=lst[1]
			
	print(dp)
	return dp

def out_write(des, ann, outdir):
	outfile=os.path.join(outdir, "newfile.txt")
	outfile_open=open(outfile, "w")
	dp=descript_file_info(des)
	head="EnsemblID\tGeneName\tGeneID\tchromosome\tstart\tend\tstrand\tBiological_Process\tMolecular_Function\tCellular_Component\tKO\tPathway\tPathwayName\tDescription\n"
	outfile_open.write(head)
	for line in open(ann, "r").readlines()[1:]:
		lst=line.strip().split("\t")
		gene=lst[0]
		if gene in dp.keys():
			outfile_open.write("%s\t%s\t%s\n" % (gene,"\t".join(lst[1:14]),dp[gene]))
			print("\t".join(lst[1:14]))
		else:
			outfile_open.write("%s\t'NA'\n" % "\t".join(lst[:14]))
	outfile_open.close()

def main():
	args = getCommands()
	des = args.descript_file
	
	ann = args.anno_file
	outdir=args.outdir
	time1=time.time()
	out_write(des, ann, outdir)
	time2=time.time()
	print("Time used: %s" %(str(time2-time1)))

if __name__ == '__main__':
	main()
