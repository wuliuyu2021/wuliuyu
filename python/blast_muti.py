#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, re
import sys
from multiprocessing import Pool

def get_file(outdir):
	pattern=re.compile(r"(.+)(fastq|fq)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(outdir)))
	print(srs)
	return srs

def blast(outdir, sample):
	if os.path.exists("/thinker/nfs5/public/wuliuyu/wuliuyu/shell/blast_work.sh"):
		os.system("sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/blast_work.sh %s %s" % (outdir, sample))
		print("sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/blast_work.sh %s %s" % (outdir, sample))
	if os.path.exists("/data/users/wuliuyu/wuliuyu/shell/blast_work.sh"):
		os.system("sh /data/users/wuliuyu/wuliuyu/shell/blast_work_sz.sh %s %s" % (outdir, sample))
		print("sh  /data/users/wuliuyu/wuliuyu/shell/blast_work_sz.sh %s %s" % (outdir, sample))

def blast_multi(args):
	outdir=args[0]
	sample=args[1]
	blast(outdir, sample)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()


def main():
	outdir=sys.argv[1]
	num=sys.argv[2]
	srs=get_file(outdir)
	args=[]
	for sr in srs:
		sample=os.path.basename("%s/%s" %(outdir, sr)).split('.')[0]
		#print(sample)
		args.append((outdir, sample))
	multi_process(blast_multi, args, int(num))


if __name__ == '__main__':
	main()