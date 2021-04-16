#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from multiprocessing import Pool

def get_dirnames(indir, pID):
	lsts=[]
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.P.1.fq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		lsts.append(sr)
		#print('%s' % os.path.abspath(sr))
	return lsts

def fastqc(usbdir, f):
	os.system('/thinker/nfs5/public/wuliuyu/software_usage/FastQC/fastqc -o %s %s' % (usbdir, f))

def fastqc_mult(args):
	usbdir=args[0]
	f=args[1]
	fastqc(usbdir, f)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()

def main():
	indir=sys.argv[1]
	usbdir=sys.argv[2]
	pID=sys.argv[3]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	lsts=get_dirnames(indir, pID)
	for lst1 in lsts:
		args.append((usbdir, lst1))
		lst2=lst1.replace("_001.P.1", "_001.P.2")
		args.append((usbdir, lst2))
	multi_process(fastqc_mult, args, 2)

if __name__ == '__main__':
	main()