#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
#Basedir = '/thinker/nfs5/public/rawdata/dir_cat'

def rawfq1(rawdir1, pID):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1_001.fastq|_R1_001.fastq.gz|_R1.fq.gz|_R1_001.good.fastq.gz|_R1.fastq.gz)$" % pID)
	srs1 = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir1)))
	#print('%s' % srs)
	return srs1

def rawfq2(rawdir2, pID):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1_001.fastq|_R1_001.fastq.gz|_R1.fq.gz|_R1_001.good.fastq.gz|_R1.fastq.gz)$" % pID)
	srs2 = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir2)))
	#print('%s' % srs)
	return srs2

def catdirs(rawdir1, rawdir2, pID):
	srs1=rawfq1(rawdir1, pID)
	srs2=rawfq2(rawdir2, pID)
	i=0
	for sr1_1 in srs1:
		sr1_2 = sr1_1.replace("_R1", "_R2")
		for sr2_1 in srs2:
			sr2_2 = sr2_1.replace("_R1", "_R2") 
			if ('%s' % sr1_1.split('_')[2]) == ('%s' % sr2_1.split('_')[2]):
				#print('%s = %s' % (sr1_1.split('_')[2], sr2_1.split('_')[2]))
				os.system('cat %s/%s >> %s/%s' % (rawdir1, sr1_1, rawdir2, sr2_1))
				print('%s/%s merged with %s/%s' % (rawdir1, sr1_1, rawdir2, sr2_1))
				i=i+1
				os.system('cat %s/%s >> %s/%s' % (rawdir1, sr1_2, rawdir2, sr2_2))
				print('%s/%s merged with %s/%s' % (rawdir1, sr1_2, rawdir2, sr2_2))
				i=i+1
		ir1_1 = sr1_1.replace("_R1_001", "_I1_001")
		ir1_2 = sr1_2.replace("_R2_001", "_I2_001")
		if os.path.exists(rawdir1+"/"+ir1_1) and os.path.exists(rawdir1+"/"+ir1_2):
			for sr2_1 in srs2:
				sr2_2 = sr2_1.replace("_R1_001", "_R2_001")
				ir2_1 = sr2_1.replace("_R1_001", "_I1_001")
				ir2_2 = sr2_2.replace("_R2_001", "_I2_001")
				if os.path.exists(rawdir2+"/"+ir2_1) and os.path.exists(rawdir2+"/"+ir2_2):
					if ('%s' % ir1_1.split('_')[2]) == ('%s' % ir2_1.split('_')[2]):
						os.system('cat %s/%s >> %s/%s' % (rawdir1, ir1_1, rawdir2, ir2_1))
						print('%s/%s merged with %s/%s' % (rawdir1, ir1_1, rawdir2, ir2_1))
						i=i+1
						os.system('cat %s/%s >> %s/%s' % (rawdir1, ir1_2, rawdir2, ir2_2))
						print('%s/%s merged with %s/%s' % (rawdir1, ir1_2, rawdir2, ir2_2))
						i=i+1
		if os.path.exists(rawdir1+"/"+ir1_1) and not os.path.exists(rawdir1+"/"+ir1_2):
			for sr2_1 in srs2:
				ir2_1 = sr2_1.replace("_R1_001", "_I1_001")
				if os.path.exists(rawdir2+"/"+ir2_1):
					if ('%s' % ir1_1.split('_')[2]) == ('%s' % ir2_1.split('_')[2]):
						os.system('cat %s/%s >> %s/%s' % (rawdir1, ir1_1, rawdir2, ir2_1))
						print('%s/%s merged with %s/%s' % (rawdir1, ir1_1, rawdir2, ir2_1))
						i=i+1
		sr1_3 = sr1_1.replace("_R1_001", "_R3_001")
		if os.path.exists(rawdir1+"/"+sr1_3):
			for sr2_1 in srs2:
				sr2_3 = sr2_1.replace("_R1_001", "_R3_001")
				if os.path.exists(rawdir1+"/"+sr2_3):
					if ('%s' % sr1_1.split('_')[2]) == ('%s' % sr2_1.split('_')[2]):
						#print('%s = %s' % (sr1_1.split('_')[2], sr2_1.split('_')[2]))
						os.system('cat %s/%s >> %s/%s' % (rawdir1, sr1_3, rawdir2, sr2_3))
						print('%s/%s merged with %s/%s' % (rawdir1, sr1_3, rawdir2, sr2_3))
						i=i+1
	print(i)


def main():
	rawdir1=sys.argv[1]
	rawdir2=sys.argv[2]
	pID=sys.argv[3]
	catdirs(rawdir1, rawdir2, pID)

if __name__ == '__main__':
	main()