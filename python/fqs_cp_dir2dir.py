#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from multiprocessing import Pool


def get_dirnames(indir):
	srs_new=[]
	pattern = re.compile(r"(.+)(_R1)(.+)(fastq.gz|fq.gz|good.fastq.gz|good.fq.gz|fq|fastq)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		sr_new=sr
		srs_new.append(sr_new)

	return  srs_new

def cp_to_usbdir(indir, f, outdir):
	#if f.split('_')[2].startswith('HGC'):
	os.system('cp %s/%s %s/%s' % (indir, f, outdir, f))
	print('%s/%s copied to %s/%s' %(indir, f, outdir, f))

def cp_to_usbdir_multi(args):
	indir=args[0]
	f=args[1]
	usbdir=args[2]
	cp_to_usbdir(indir, f, usbdir)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()


def main():
	indir = sys.argv[1]#/thinker/dstore/rawfq/180512_E00603_0109_BHLHL7CCXY	
	outdir = sys.argv[2]
	cp_nums = sys.argv[3]
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	args=[]
	sr1s=get_dirnames(indir)
	for sr1 in sr1s:
		args.append((indir, sr1, outdir))
		sr2=sr1.replace("_R1", "_R2")
		args.append((indir, sr2, outdir))
	multi_process(cp_to_usbdir_multi, args, int(cp_nums))
	
		
if __name__ == '__main__':
	main()