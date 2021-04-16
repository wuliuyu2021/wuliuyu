#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys


def get_dirnames(indir):
	pattern = re.compile(r"(.+)(R1)(.+)(fastq.gz|fq.gz)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr1 in srs:
		sr2=sr1.replace('_R1', '_R2')
		os.system("mv %s/%s %s/%s_%s" % (indir, sr1, indir, sr1.split('_')[0], sr1.split('_')[-1]))
		os.system("mv %s/%s %s/%s_%s" % (indir, sr2, indir, sr2.split('_')[0], sr2.split('_')[-1]))

def main():
	indir = sys.argv[1]#/thinker/dstore/rawfq/180512_E00603_0109_BHLHL7CCXY	
	get_dirnames(indir)
		
if __name__ == '__main__':
	main()