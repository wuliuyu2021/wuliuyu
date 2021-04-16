#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv
from multiprocessing import Pool


def sample_contact(seqcsv, lib_type):
	d=[]
	d1=[]
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		if lst.libtype == lib_type:
			zh="%s_%s_%s" % (lst.ordID, lst.projectID, lst.libID)
			d.append(zh)
			d1.append(lst.libID)
	if d is None:
		print('Warning, Wrong lib_type, Please check!!!' * 3)

	return d,d1


def get_dirnames(indir, pID, seqcsv, lib_type):
	srs_new=[]
	data_lst=sample_contact(seqcsv, lib_type)[0]
	pattern = re.compile(r"(^S)(.+)(_%s_)(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if '_'.join(sr.split("_")[0:3]) in data_lst:
			sr_new=sr
			srs_new.append(sr_new)

	return  srs_new

def cp_to_usbdir(indir, f, usbdir):
	if os.path.abspath(indir).split('/')[2] == 'dstore':
		os.system('ds cp %s/%s %s/%s' % (indir, f, usbdir, f))
	else:
		os.system('cp %s/%s %s/%s' % (indir, f, usbdir, f))

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
	usbdir = sys.argv[2]#/data/longrw/mnt/20180227A1B1_3
	seqcsv = sys.argv[3]
	lib_type = sys.argv[4]
	pID = sys.argv[5]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	sr1s=get_dirnames(indir, pID, seqcsv, lib_type)
	for sr1 in sr1s:
		args.append((indir, sr1, usbdir))
		sr2=sr1.replace("_R1_001", "_R2_001")
		args.append((indir, sr2, usbdir))
	multi_process(cp_to_usbdir_multi, args, 4)
	dn=sample_contact(seqcsv, lib_type)[1]
	for d in sorted(set(dn)):
		os.system("mkdir -p %s/Rawdata/%s" % (usbdir, d))
		#print("%s/%s_%s_%s/Rawdata/%s\n" (usbdir, lib_type, pID, d))
	for root, dirs, fs in os.walk(usbdir):
		fs.sort()
		for f in fs:
			#if f.endswith("fastq.gz") and not os.path.exists('%s/%s_%s_%s/Rawdata/%s' %(usbdir, lib_type, pID, f.split('_')[2])):
			#	print("Please check the %s of %s and %s!!!\n" %(f.split('_')[2], lib_type, os.path.basename(seqcsv)))
			#	sys.exit(-1)
			if f.endswith("fastq.gz") and os.path.exists('%s/Rawdata/%s' %(usbdir, f.split('_')[2])):
				os.system('mv %s/%s %s/Rawdata/%s/%s' %(usbdir, f, usbdir, f.split('_')[2], '_'.join(f.split('_')[2:8])))
	os.chdir(usbdir)
	os.system('md5sum Rawdata/*/* > md5')
	os.system('md5sum -c md5 > md5.check')
		
if __name__ == '__main__':
	main()