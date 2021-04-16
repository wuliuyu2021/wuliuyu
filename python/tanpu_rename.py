#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re
import sys

def get_file(indir, pid):
	pattern=re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pid)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	return srs

def rename(indir, outdir, pid):
	srs=get_file(indir, pid)
	for sr1 in srs:
		sr2=sr1.replace("_R1_001", "_R2_001")
		os.system('mv %s/%s %s/%s.reads1.fastq.gz' % (indir, sr1,outdir, sr1.split('_')[2]))
		print('%s/%s moved to %s/%s.reads1.fastq.gz' % (indir, sr1, outdir, sr1.split('_')[2]))
		os.system('mv %s/%s %s/%s.reads2.fastq.gz' % (indir, sr2, outdir, sr2.split('_')[2]))
		print('%s/%s moved to %s/%s.reads2.fastq.gz' % (indir, sr2, outdir, sr2.split('_')[2]))


def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]
	pid=sys.argv[3]
	rename(indir, outdir, pid)

if __name__ == '__main__':
	main()