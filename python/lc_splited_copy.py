#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from multiprocessing import Pool


def table_split(seqcsv):
	d={}
	poolID=[]
	for line in open(seqcsv):
		ls0 = line.strip().split(",")[0]
		#lst1 = line.strip().split(",")[1]
		lst6 = line.strip().split(",")[6]
		lst24 = line.strip().split(",")[24]
		#poolID = sort(set(lst11))
		if lst6 == 'LIANchuan-L':
			d[ls0]=lst24
	return d


def getfiles(indir, pID, seqcsv, poolid):
	sam1s=[]
	dn={}
	d=table_split(seqcsv)
	match = re.compile(r"(^S\d+)(_%s_)(.+)(_R1_001)(_R1_001.good.fastq.gz)$" % pID)
	fq1s = sorted(filter(lambda x: re.match(match, x), os.listdir(indir)))
	for fq1 in fq1s:
		fq2 = fq1.replace('_R1_001_R1_001', '_R1_001_R2_001')
		sam1 = fq1.split('_')[0]
		l1 = "_".join(fq1.split('_')[2:])
		l2 = "_".join(fq2.split('_')[2:])
		if sam1 in d.keys() and d[sam1] == poolid:
			dn[fq1]=l1
			dn[fq2]=l2
			sam1s.append(sam1)
	return dn, sam1s

def cp_md5_usbdir(md5dir, usbdir, indir, pID, seqcsv, poolid):
	sam1s=getfiles(indir, pID, seqcsv, poolid)[1]
	match_md5 = re.compile(r"(^S\d+)(_%s_)(.+)(_001.good.fastq.gz.md5)$" % pID)
	fs = sorted(filter(lambda x: re.match(match_md5, x), os.listdir(md5dir)))
	for f in fs:
		if f.endswith('gz.md5'):
			os.system('cp %s %s' % (f, usbdir))



def cp_to_usbdir(f, usbdir):
	#os.system('md5sum %s > %s/%s.md5' % (f, usbdir, f))
	os.system('cp %s %s' % (f, usbdir))

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
	md5dir = sys.argv[4]
	poolid = sys.argv[5]
	pID = sys.argv[6]
	dn=getfiles(indir, pID, seqcsv, poolid)[0]
	if not os.path.exists(usbdir):
		try:
			os.makedirs(usbdir)
		except:
			print("Warning: the directory exists!!!")
	args=[]
	for f in dn.keys():
		args.append((f, usbdir))
	multi_process(cp_to_usbdir_multi, args, 4)
	cp_md5_usbdir(md5dir, usbdir, indir, pID, seqcsv, poolid)
	os.chdir(usbdir)
	for old in dn.keys():
		os.system("mv %s %s" % (old, dn[old]))
	os.chdir(usbdir)
	os.system("rename _R1_001_R _R *")
	md5=open('md5', 'a')
	os.system('cat *gz.md5 > old.md5')
	for line in open("old.md5"):
		lst1 = line.strip().split("  ")[0]
		lst2 = line.strip().split("  ")[1].split('/')[-1]
		seq = '_'.join([lst2.strip().split('_R1_001_')[0], lst2.strip().split('_R1_001_')[1]])
		if seq in dn.keys():
			md5.write("%s  %s\n" % (lst1[0], dn[seq]))
		else:
			md5.write("error!!!")
	md5.close()
	os.system('rm *.gz.md5 old.md5')
	os.system('md5sum -c md5 > md5.check')
	md5.close()
		
if __name__ == '__main__':
	main()