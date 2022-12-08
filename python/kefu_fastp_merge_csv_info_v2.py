#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from collections import Counter
from optparse import OptionParser


def parse_cmd():
	usage="To make Hapyun csv!"
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-i","--infile",dest="infile",default=None,help="info csv")
	parser.add_option("-t","--dictcsv",dest="dictcsv",default=None,help="input dictionary csv")
	parser.add_option("-o","--outdir",dest="outdir",default=None,help="the outfile path")
	parser.add_option("-a","--adapter",dest="adapter",default=None,help="input the adapter type:IDT/UPM/MGI")
	
	return parser.parse_args()

def dict_maker(options):
	ds={}
	if options.dictcsv:
		for line in open(options.dictcsv, 'r'):
			lst = re.split('[,\t]',line.strip())
			ds[lst[0]]=lst[1]
			if lst[1].find("-") != -1 or lst[1][0].isdigit() == True:
				print("%s %s group were illegal" % (lst[0], lst[1]))
	return ds

def get_files(options):
	d={}
	lts=[]
	dn={}
	dt={}
	if options.infile:
		for line in open(options.infile, 'r'):
			lst = re.split('[,\t]',line.strip())
			#if lst[0] in ds.keys():
			con="%s=%s" % (lst[0], lst[1])
			lts.append(lst[0])
			d[lst[1].replace("oss://sz-","/")] = lst[0]
	print(d)
	slts=Counter(lts)
	dn=sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True)
	print(dn)
	for k,v in dn:

		if int(v) >0:
			d3=[k1 for k1,v1 in d.items() if v1==k]
			dt[k]=";".join(d3)
		
	print(dt)
	return dt

def info_maker():
	(options, args) = parse_cmd()
	outfile = os.path.join(options.outdir, "data.csv")
	lst=[]
	if os.path.exists(outfile):
		os.remove(outfile)
	ds=get_files(options)
	dst=dict_maker(options)
	with open(outfile, 'w') as f:
		spbol=";"
		for sample_pre,path in ds.items():
			if sample_pre in dst.keys():
				sample = dst[sample_pre]
				if spbol in path:
					if options.adapter:
						f.write("%s_R1_001.fastq.gz,%s_R2_001.fastq.gz,%s,%s\n" % (path.replace(";","_R1_001.fastq.gz;"), path.replace(";","_R2_001.fastq.gz;"), sample,options.adapter))
					else:
						f.write("%s_R1_001.fastq.gz,%s_R2_001.fastq.gz,%s\n" % (path.replace(";","_R1_001.fastq.gz;"), path.replace(";","_R2_001.fastq.gz;"), sample))		
				if spbol not in path:
					if options.adapter:
						f.write("%s_R1_001.fastq.gz,%s_R2_001.fastq.gz,%s,%s\n" % (path, path, sample,options.adapter))
					else:
						f.write("%s_R1_001.fastq.gz,%s_R2_001.fastq.gz,%s\n" % (path, path, sample))
			else:
				print("\033[31;1mWrong, %s can not find the values in dictionary, please check!\033[0m" % sample_pre)
	f.close()

def main():
	info_maker()
	

if __name__ == "__main__":
	main()
