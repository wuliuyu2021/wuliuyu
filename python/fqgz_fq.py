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

def main():
	seqcsv = sys.argv[1]
	outdir = sys.argv[2]
	num = sys.argv[3]

	dn = sample_info(seqcsv)
	for key in dn.keys():
		os.system("less %s | head -n %s > %s/%s.fastq" % (dn[key], int(num), outdir, key))
		print("%s/%s.fastq was from %s :head -n %s" % (outdir, key, dn[key], int(num)))
	

if __name__ == '__main__':
	main()