#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv
from multiprocessing import Pool


def sample_contact(seqcsv, contact_id):
	d=[]
	d1={}
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		if lst.sample_num != "":
			d1[lst.libID] = lst.sample_num
		if lst.contractID == contact_id:
			d.append(lst.ordID)
	if d is None:
		print('Warning, Wrong contact_id, Please check!!!' * 3)

	return d, d1


def get_dirnames(indir, pID, seqcsv, contact_id):
	srs_new=[]
	data_lst=sample_contact(seqcsv, contact_id)[0]
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if sr.split("_")[0] in data_lst:
			sr_new=sr
			srs_new.append(sr_new)

	return  srs_new

def cp_to_usbdir(indir, f, usbdir):
	os.system('ds cp %s/%s %s/%s' % (indir, f, usbdir, f))

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
	indir = sys.argv[1]	
	usbdir = sys.argv[2]
	seqcsv = sys.argv[3]
	contact_id = sys.argv[4]
	pID = sys.argv[5]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	sr1s=get_dirnames(indir, pID, seqcsv, contact_id)
	for sr1 in sr1s:
		args.append((indir, sr1, usbdir))
		sr2=sr1.replace("_R1_001", "_R2_001")
		args.append((indir, sr2, usbdir))
	multi_process(cp_to_usbdir_multi, args, 4)
	os.chdir(usbdir)
	dn = sample_contact(seqcsv, contact_id)[1]
	for root, dirs, fs in os.walk(usbdir):
		for f in fs:
			if f.endswith("fastq.gz") and f.split('_')[2].startswith("HGC"):
				fr=f.split('_')[2]
				ft=dn[fr]
				f1=f.replace('%s' % fr, '%s' % ft)
				os.system('mv %s/%s %s/%s' % (usbdir, f, usbdir, f1))
	for root, dirs, fs in os.walk(usbdir):
		for f1 in fs:
			if f1.endswith('_R1_001.fastq.gz') or f.endswith('_R1_001.good.fastq.gz'):
				f2=f1.replace("_R1_001", "_R2_001")
				os.system('mv %s/%s %s/%s.reads1.fastq.gz' % (usbdir, f1, usbdir, f1.split('_')[2]))
				os.system('mv %s/%s %s/%s.reads2.fastq.gz' % (usbdir, f2, usbdir, f2.split('_')[2]))
	os.chdir(usbdir)			
	for root, dirs, fs in os.walk(usbdir):
		for f in fs:
			if f.endswith("fastq.gz"):
				os.system('md5sum %s > %s.md5' % (f, f))
	md5=open('md5', 'a')
	os.system('cat *.fastq.gz.md5 > md5')
	os.system('rm *.fastq.gz.md5')
	os.system('md5sum -c md5 > md5.check')
	md5.close()
		
if __name__ == '__main__':
	main()