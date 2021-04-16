#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse
import pandas as pd
import numpy as np


def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to make gfold diff csvs.')
	parser.add_argument('-c','--countfile',dest='countfile', required=True, help='The Readcount csv contains all sample files')
	parser.add_argument('-r','--rpkmfile',dest='rpkmfile',required=True, help='The output directory contains all result files')
	parser.add_argument('-l','--lst',dest='lst',required=True, type=str, 
		help='The strs contains all info sample name with comma split symbol, such as A,B,C')
	parser.add_argument('-g','--group',dest='group',required=True, type=str, 
		help='The strs contains all info sample group with comma split symbol,such as AVSB,BVSC,AVSC')
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains all result files')
	
	args = parser.parse_args()
	
	return args

def info_write(countfile, rpkmfile, lst, outdir):

	head="GeneSymbol\tGeneName\tRead_Count\tGene_exon_length\tRPKM\n"
	chead=open(countfile, "r").readlines()[0]
	clt=chead.strip().split("\t")
	rhead=open(countfile, "r").readlines()[0]
	rlt=rhead.strip().split("\t")
	#print(clt)
	#print(rlt)
	
	for index,sam in enumerate(lst.split(",")):
		
		samcsv=os.path.join(outdir ,"%s.read_cnt" % sam)
		samopen=open(samcsv, "w")
		samopen.write(head)
		if sam not in clt and sam not in rlt:
			continue
		if sam in clt and sam in rlt:
			for x,y in zip(open(countfile, "r").readlines()[1:], open(rpkmfile, "r").readlines()[1:]):
				samopen.write("%s\t%s\t%s\t10\t%s\n"% (x.split("\t")[0],x.split("\t")[0],x.split("\t")[int(index)+1],y.split("\t")[int(index)+1]))
		samopen.close()
def work_cmd(group ,outdir):

	if os.path.exists(outdir+"/"+"work.sh"):
		os.remove(outdir+"/"+"work.sh")
	work=os.path.join(outdir,"work.sh")

	for g in group.split(","):

		os.system("echo '/thinker/nfs5/public/heww/GFOLD/gfold.V1.1.4/gfold diff -s1 %s.read_cnt -s2 %s.read_cnt -o %s.diff\n' >> %s/work.sh" % 
			(g.split("VS")[0],g.split("VS")[-1],g,outdir))



def main():
	args = getCommands()
	countfile, rpkmfile, lst, group, outdir=args.countfile, args.rpkmfile, args.lst, args.group, args.outdir
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	info_write(countfile, rpkmfile, lst, outdir)
	work_cmd(group ,outdir)

	

if __name__ == "__main__":
	main()
