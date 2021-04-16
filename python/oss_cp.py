#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, time
from multiprocessing import Pool

def sample_contact(seqcsv, contact_id):
	cons=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")
		if lst[5] == contact_id:
			con="%s_%s_%s_%s" % (lst[0], lst[7], lst[1], os.path.basename(seqcsv).split('.csv')[0].split('_')[-1])
			cons.append(con)
	return cons

def get_file(rawdir, pID):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir)))
	return srs

def oss_cp(rawdir, pID, ossdir, to, seqcsv, contact_id, parallel):
	cons=sample_contact(seqcsv, contact_id)
	srs=get_file(rawdir, pID)
	for sr1 in srs:
		sr2=sr1.replace("_R1_001", "_R2_001")
		if '_'.join(sr1.split('_')[0:4]) in  cons:
			if to == 'sz':
				os.system('ossutil cp -ru --parallel=%s %s/%s %s' % (parallel, rawdir, sr1, ossdir))
				os.system('ossutil cp -ru --parallel=%s %s/%s %s' % (parallel, rawdir, sr2, ossdir))
			if to == 'bj':
				os.system('ossutil cp -e oss-cn-beijing.aliyuncs.com -ru --parallel=%s %s/%s %s' % (parallel, rawdir, sr1, ossdir))
				os.system('ossutil cp -e oss-cn-beijing.aliyuncs.com -ru --parallel=%s %s/%s %s' % (parallel, rawdir, sr2, ossdir))
			

def main():
	rawdir=sys.argv[1]
	ossdir=sys.argv[2]
	seqcsv=sys.argv[3]
	contact_id=sys.argv[4]
	pID=sys.argv[5]
	to = sys.argv[6]
	parallel = sys.argv[7]
	time1=time.time()
	oss_cp(rawdir, pID, ossdir, to, seqcsv, contact_id, parallel)
	time2=time.time()
	print('Time used: %s' % str(time2 - time1))

if __name__ == '__main__':
	main()