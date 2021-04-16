#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys



def sample_info(seqcsv):
	dn={}
	for line in open(seqcsv):
		lst = line.strip().split(",")
		dn[lst[0]]=lst[1]
		#print(d)
	return dn

def get_files(indir, seqcsv):
	data_lst=sample_info(seqcsv)
	srs_new=[]
	pattern = re.compile(r"(.+)(_R1)(_001.good.fastq.gz|_001.fastq.gz|_001.fq.gz)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	#print('%s' % srs)
	
			
	return srs


def main():
	indir = sys.argv[1]
	seqcsv = sys.argv[2]
	dn = sample_info(seqcsv)
	sr1s = get_files(indir, seqcsv)
	os.chdir(indir)
	for sr1 in sr1s:
		sr2 = sr1.replace("_R1_001", "_R2_001")
		if sr1.split('_')[0] in  dn.keys():
			os.system('mv %s/%s %s/%s_%s' % (indir, sr1, indir, dn[sr1.split('_')[0]], '_'.join(sr1.split('_')[1:])))
			print('%s/%s movers to %s/%s_%s'% (indir, sr1, indir,dn[sr1.split('_')[0]], '_'.join(sr1.split('_')[1:])))
			os.system('mv %s/%s %s/%s_%s' % (indir, sr2, indir, dn[sr2.split('_')[0]],'_'.join(sr2.split('_')[1:])))
			print('%s/%s movers to %s/%s_%s'% (indir, sr2, indir, dn[sr2.split('_')[0]],'_'.join(sr2.split('_')[1:])))

if __name__ == '__main__':
	main()