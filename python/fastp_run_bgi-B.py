#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, re
import sys
from multiprocessing import Pool

def get_file(indir, pid):
	pattern=re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pid)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	return srs

def fastp(outdir, indir, pid, clean_dir, sr1):
	sid = sr1.split("_R1_")[0]
	rf1 = os.path.join(indir, sr1)
	gf1 = os.path.join(clean_dir, sr1.replace("_001.", "_001.good."))
	sr2 = sr1.replace('_R1_001', '_R2_001')
	rf2 = os.path.join(indir, sr2)
	gf2 = os.path.join(clean_dir, sr2.replace("_001.", "_001.good."))
	jf = os.path.join(outdir, "%s.json" % sid)
	hf = os.path.join(outdir, "%s.html" % sid)
	if os.path.exists('/thinker/nfs2/longrw/mygit/fastp/fastp'):
		os.system('/thinker/nfs2/longrw/mygit/fastp/fastp -i %s -I %s -o %s -O %s  -j %s -h %s -l 150 -n 2 -q 0 -u 40 --disable_adapter_trimming -g --poly_g_min_len 50 -x --poly_x_min_len 10' % (rf1, rf2, gf1, gf2, jf, hf))
	if os.path.exists('/thinker/storage/users/hanjie/tools/fastp/fastp'):
		os.system('/thinker/storage/users/hanjie/tools/fastp/fastp -i %s -I %s -o %s -O %s  -j %s -h %s -l 150 -n 2 -q 0 -u 40 --disable_adapter_trimming -g --poly_g_min_len 50 -x --poly_x_min_len 10' % (rf1, rf2, gf1, gf2, jf, hf))

def fastp_multi(args):
	outdir=args[0]
	indir=args[1]
	pid=args[2]
	clean_dir=args[3]
	sr1=args[4]
	fastp(outdir, indir, pid, clean_dir, sr1)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()

def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]
	pid=sys.argv[3]
	clean_dir=sys.argv[4]
	srs=get_file(indir, pid)
	args=[]
	for sr1 in srs:
		args.append((outdir, indir, pid, clean_dir, sr1))
	multi_process(fastp_multi, args, 4)

if __name__ == '__main__':
	main()