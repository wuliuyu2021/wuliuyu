#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re 
import random




def get_filesname(indir):	
	pattern1 = re.compile(r"(^S\d+)(.+)(_R1)(_001.fastq.gz)$")
	pattern2 = re.compile(r"(^S\d+)(.+)(_R2)(_001.fastq.gz)$")
	sr1s = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(indir)))
	sr2s = sorted(filter(lambda x: re.match(pattern2, x), os.listdir(indir)))
	sampleID1s = [sr1.split('_')[0] for sr1 in sr1s]
	sampleID2s = [sr2.split('_')[0] for sr2 in sr2s]
	return sr1s, sr2s, sampleID1s

def table_maker():
	sample = get_filesname(indir)
	sr1s = sample[0]
	sr2s = sample[1]
	sampleID1s = sample[2]
	d = os.path.abspath(indir)
	

	sample = open('sample.txt', 'w')
	lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	
	for j in range(len(sr1s)):
		l = random.choice(lst)
		

		sample.write("%s\t%s\t%s/%s\t%s/%s\n" % (sampleID1s[j], l, d, sr1s[j], d, sr2s[j]))
		lst.remove(l)
	sample.close()
if __name__ == '__main__':
	indir = sys.argv[1]	
	table_maker()














