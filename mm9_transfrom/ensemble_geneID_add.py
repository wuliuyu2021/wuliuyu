#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from optparse import OptionParser


def parse_cmd():
	usage="Ensemble geneID add of mm9"
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-i","--indir",dest="indir",default=None,help="files as form of txt")
	parser.add_option("-o","--outdir",dest="outdir",default=None,help="new files with anno")
	#parser.add_option("-f","--flag",dest="flag",default=None,help="the end flag of files")
	#parser.add_option("-c","--ccc",dest="ccc",default=None,help="input ccc")
	#parser.add_option("-d","--ddd",dest="ddd",default=None,help="input ddd")
	
	return parser.parse_args()

def get_files():
	(options, args) = parse_cmd()
	if not os.path.exists(options.outdir):
		os.makedirs(options.outdir)
	#pattern = re.compile(r"(.+)(All|VS|HTSeq)(.+)")
	pattern = re.compile(r"(.+)(txt)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))
	for sr in srs:	
		os.system("perl /thinker/nfs5/public/wuliuyu/wuliuyu/mm9_transfrom/get_all_match_geneID_readscount.pl /thinker/nfs5/public/wuliuyu/wuliuyu/mm9_transfrom/all_mm9_match_ensemble_geneID.txt %s/%s %s/%s.with_anno.txt" 
			%(options.indir, sr, options.outdir, sr.split(".txt")[0]))
		print("%s/%s transformed to %s/%s.with_anno.txt" %(options.indir, sr, options.outdir, sr.split(".txt")[0]))



def main():
	get_files()
	

if __name__ == "__main__":
	main()
