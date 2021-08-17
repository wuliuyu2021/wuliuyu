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
	parser.add_option("-o","--outdir",dest="outdir",default=None,help="the outfile path")
	parser.add_option("-a","--adapter",dest="adapter",default=None,help="input the adapter type:IDT/UPM/MGI")
	#parser.add_option("-d","--ddd",dest="ddd",default=None,help="input ddd")
	
	return parser.parse_args()

def get_files(options):
	d={}
	lts=[]
	dn={}
	dt={}
	if options.infile:
		for line in open(options.infile, 'r'):
			lst = re.split('[,\t]',line.strip())
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
	with open(outfile, 'w') as f:
		spbol=";"
		for sample,path in ds.items():
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
				
		f.close()

def main():
	info_maker()
	

if __name__ == "__main__":
	main()
