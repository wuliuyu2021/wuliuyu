#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from multiprocessing import Pool


def sample_contact(seqcsv, contact_id):
	d=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")
		if lst[5] == contact_id:
			d.append(lst[0])
	return d


def get_dirnames(indir, pID, seqcsv, contact_id):
	srs_new=[]
	data_lst=sample_contact(seqcsv, contact_id)
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if sr.split("_")[0] in data_lst:
			sr_new=sr
			srs_new.append(sr_new)

	return  srs_new

def cp_to_usbdir(f, usbdir):
	#os.system('md5sum %s > %s/%s.md5' % (f, usbdir, f))
	os.system('ds cp %s %s' % (f, usbdir))

def cp_to_usbdir_multi(args):
	f=args[0]
	usbdir=args[1]
	cp_to_usbdir(f, usbdir)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()


def main():
	indir = sys.argv[1]#/thinker/dstore/rawfq/180512_E00603_0109_BHLHL7CCXY	
	usbdir = sys.argv[2]#/data/longrw/mnt/20180227A1B1_3
	seqcsv = sys.argv[3]
	contact_id = sys.argv[4]
	pID = sys.argv[5]
	#anlongen-A
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	sr1s=get_dirnames(indir, pID, seqcsv, contact_id)
	for sr1 in sr1s:
		args.append((sr1, usbdir))
		sr2=sr1.replace("_R1_001", "_R2_001")
		args.append((sr2, usbdir))
	multi_process(cp_to_usbdir_multi, args, 20)
	
		
if __name__ == '__main__':
	main()