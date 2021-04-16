#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, time
from multiprocessing import Pool

def sample_contact(seqcsv):
	cons={}
	for line in open(seqcsv):
		lst = line.strip().split(",")	
		cons[lst[0]]=int(lst[2])
	print(cons)
	return cons

def get_dirnames(indir):
	srs_new=[]
	pattern = re.compile(r"(.+)(_R1)(.+)(fastq.gz|fq.gz|good.fastq.gz|good.fq.gz|fq|fastq)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		sr_new=sr
		srs_new.append(sr_new)

	return  srs_new

def fastp_split(indir, outdir, sr1, num):
	sid = sr1.split("_R1_")[0]
	rf1 = os.path.join(indir, sr1)
	gf1 = os.path.join(outdir, sr1.replace("_001.", "_001.good."))
	sr2 = sr1.replace('_R1_001', '_R2_001')
	rf2 = os.path.join(indir, sr2)
	gf2 = os.path.join(outdir, sr2.replace("_001.", "_001.good."))
	jf = os.path.join(outdir, "%s.json" % sid)
	hf = os.path.join(outdir, "%s.html" % sid)
	if os.path.exists('/thinker/nfs2/longrw/mygit/fastp/fastp'):
		os.system("/thinker/nfs2/longrw/mygit/fastp/fastp -i %s -I %s -o %s -O %s  -j %s -h %s -Q -A -G --reads_to_process %s --dont_overwrite" % (rf1, rf2, gf1, gf2, jf, hf, num))
	if os.path.exists('/usr/local/bin/fastp'):
		os.system("/usr/local/bin/fastp -i %s -I %s -o %s -O %s  -j %s -h %s -Q -A -G --reads_to_process %s --dont_overwrite" % (rf1, rf2, gf1, gf2, jf, hf, num))


def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()

def fastp_split_multi(args):
	indir=args[0]
	outdir=args[1]
	sr1=args[2]
	num=args[3]
	fastp_split(indir, outdir, sr1, num)

def main():
	indir=sys.argv[1]
	seqcsv=sys.argv[2]
	outdir=sys.argv[3]
	nums=sys.argv[4]
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	sr1s=get_dirnames(indir)
	cons=sample_contact(seqcsv)
	args=[]
	for sr1 in sr1s:
		if sr1.split("_R1_")[0] in cons.keys():	
			num = cons[sr1.split("_R1_")[0]]
			args.append((indir, outdir, sr1, num))
		else:
			print('Wrong, %s not found in dir.keys!!!' % sr1.split("_R1_")[0])
			
	multi_process(fastp_split_multi, args, int(nums))



if __name__ == '__main__':
	main()