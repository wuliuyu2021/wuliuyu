#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys



def sample_info(seqcsv):
	
	dn={}
	for line in open(seqcsv):
		lst = line.strip().split(",")
		sam_info="%s_%s_%s_%s" % (lst[0], lst[2], lst[3], lst[4])
		dn[lst[1]]=sam_info
		
	return dn

def files_change(indir, seqcsv):
	dn=sample_info(seqcsv)
	srs_new=[]
	pattern = re.compile(r"(.+)(_R1)(_001.good.fastq.gz|_001.fastq.gz|_001.fq.gz)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	#print('%s' % srs)
	for sr1 in srs:
		sr2 = sr1.replace("_R1_001", "_R2_001")
		if sr1.split("_")[0] in dn.keys():
			sr1_new="%s_%s" % (dn[sr1.split("_")[0]], "_".join(sr1.split("_")[1:]))
			os.system('mv %s/%s %s/%s' % (indir, sr1, indir, sr1_new))
			print("%s/%s moves to %s/%s" % (indir, sr1, indir, sr1_new))
		if sr2.split("_")[0] in dn.keys():
			sr2_new="%s_%s" % (dn[sr2.split("_")[0]], "_".join(sr2.split("_")[1:]))
			os.system('mv %s/%s %s/%s' % (indir, sr2, indir, sr2_new))
			print("%s/%s moves to %s/%s" % (indir, sr2, indir, sr2_new))
			


def main():
	indir = sys.argv[1]
	seqcsv = sys.argv[2]
	files_change(indir, seqcsv)

if __name__ == '__main__':
	main()