#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
#Basedir = '/thinker/nfs5/public/rawdata/dir_cat'

def rawfq1(rawdir1):
	pattern = re.compile(r"(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz)$")
	srs1 = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir1)))
	#print('%s' % srs)
	return srs1

def rawfq2(rawdir2):
	pattern = re.compile(r"(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz)$" )
	srs2 = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir2)))
	#print('%s' % srs)
	return srs2

def catdirs(rawdir1, rawdir2):
	srs1=rawfq1(rawdir1)
	srs2=rawfq2(rawdir2)
	i=0
	for sr1_1 in srs1:
		sr1_2 = sr1_1.replace("_R1_001", "_R2_001")
		for sr2_1 in srs2:
			sr2_2 = sr2_1.replace("_R1_001", "_R2_001") 
			if ('%s' % sr1_1.split('_')[0]) == ('%s' % sr2_1.split('_')[0]):
				#print('%s = %s' % (sr1_1.split('_')[2], sr2_1.split('_')[2]))
				os.system('cat %s/%s >> %s/%s' % (rawdir1, sr1_1, rawdir2, sr2_1))
				print('%s/%s merged with %s/%s' % (rawdir1, sr1_1, rawdir2, sr2_1))
				i=i+1
				os.system('cat %s/%s >> %s/%s' % (rawdir1, sr1_2, rawdir2, sr2_2))
				print('%s/%s merged with %s/%s' % (rawdir1, sr1_2, rawdir2, sr2_2))
				i=i+1
	print(i)


def main():
	rawdir1=sys.argv[1]
	rawdir2=sys.argv[2]
	catdirs(rawdir1, rawdir2)

if __name__ == '__main__':
	main()