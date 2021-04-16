#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys
import re


def table_split(seq_csv):
	pcs1=[]
	pcs2=[]
	d={}
	for line in open(seq_csv):
		lID=line.strip().split(',')[2]
		pnID=line.strip().split(',')[4]
		cnID=line.strip().split(',')[5]
		pID = line.strip().split(",")[23]
		if pID == 'bgi-A':
			pc="%s-%s" % (cnID, pnID)
		d[lID]=pc
		pcs1.append(pc)
	pcs2=list(set(pcs1))
	return pcs2, d


def get_files(indir):
	lIDs=[]	
	pattern1 = re.compile(r"(^S\d+)(_bgi-A_)(.+)(_R1)(_001.good.fastq.gz)$")
	pattern2 = re.compile(r"(^S\d+)(_bgi-A_)(.+)(_R2)(_001.good.fastq.gz)$")
	sr1s = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(indir)))
	sr2s = sorted(filter(lambda x: re.match(pattern2, x), os.listdir(indir)))
	for sr1 in sr1s:
		lID=sr1.split('_')[2]
		lIDs.append(lID)		
	return sr1s, lIDs, sr2s
 

def main():
	indir=sys.argv[1]
	seq_csv=sys.argv[2]
	pcs=table_split(seq_csv)[0]
	dn=table_split(seq_csv)[1]
	sr1s=get_files(indir)[0]
	lIDs=get_files(indir)[1]
	sr2s=get_files(indir)[2]
	for pc in pcs:
		os.system('mkdir %s' % pc)
	for i in range(len(sr1s)):
		if dn[lIDs[i]] in pcs:
			os.system('mv %s %s %s' % (sr1s[i], sr2s[i], dn[lIDs[i]]))


if __name__ == '__main__':
	main()







