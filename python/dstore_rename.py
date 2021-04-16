#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

def get_dirnames(indir, pID1):
	lst=[]
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pID1)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		lst.append(sr)

	return  lst

def dstore_rename(indir, pID1, pID2):
	sr1s=get_dirnames(indir, pID1)
	for sr1 in sr1s:
		sr2=sr1.replace("_R1_001", "_R2_001")
		sr1_new='%s_%s_%s' % (sr1.split('_')[0], pID2, '_'.join(sr1.split('_')[2:]))
		os.system('ds mv %s %s' % (sr1, sr1_new))
		sr2_new='%s_%s_%s' % (sr2.split('_')[0], pID2, '_'.join(sr2.split('_')[2:]))
		os.system('ds mv %s %s' % (sr2, sr2_new))

if __name__ == '__main__':
	indir=sys.argv[1]
	pID1=sys.argv[2]
	pID2=sys.argv[3]
	dstore_rename(indir, pID1, pID2)