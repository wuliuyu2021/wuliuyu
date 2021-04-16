#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re
from multiprocessing import Pool

def table_split(seq_csv):
	d={}
	d1={}
	poolID=[]
	for line in open(seq_csv):
		ls0 = line.strip().split(",")[0]
		#lst1 = line.strip().split(",")[1]
		lst6 = line.strip().split(",")[6]
		lst24 = line.strip().split(",")[24]
		if lst6 == 'HANGzhoulianchuan-K':
			d[ls0]=lst24
			d1[ls0]=lst24

	return d, d1

def getfiles(rawdir, pID, seq_csv, poolid):
	dn={}
	d=table_split(seq_csv)[0]
	d1=table_split(seq_csv)[1]
	match = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pID)
	fq1s = sorted(filter(lambda x: re.match(match, x), os.listdir(rawdir)))
	for fq1 in fq1s:	
		fq2 = fq1.replace('_R1_001.fastq.gz', '_R2_001.fastq.gz')
		sam1 = fq1.split('_')[0]
		l1 = "_".join(fq1.split('_')[2:])
		l2 = "_".join(fq2.split('_')[2:])
		#print('%s' % d1[sam1])
		if sam1 in d.keys() and d1[sam1] == poolid:
			dn[fq1]="_".join([d[sam1], l1])
			dn[fq2]="_".join([d[sam1], l2])
		else:
			print('No pattern data!!!')
	return dn


def cp_to_usb(f, usbdir):
	os.system("md5sum %s > %s/%s.md5" % (f, usbdir, f))
	os.system("ds cp %s %s/%s" % (f, usbdir, f))

def cp_to_usb_multi(args):
	f = args[0]
	usbdir = args[1]
	cp_to_usb(f, usbdir)

	
def multi_process(func, args, n=None):
	p = Pool(n)
	p.map(func, args)
	p.close()
	p.join()

	
def main():
	rawdir=sys.argv[1]#/thinker/dstore/rawfq/180512_E00603_0109_BHLHL7CCXY
	usbdir=sys.argv[2]#/data/longrw/mnt/1
	seq_csv=sys.argv[3]#/thinker/nfs2/longrw/runPipelineInfo/180519_E00603_0113_BHLK73CCXY/sequence_180519_E00603_0113_BHLK73CCXY.csv
	poolid=sys.argv[4]
	pID=sys.argv[5]#lc-bio-A
	dn=getfiles(rawdir, pID, seq_csv, poolid)
	if not os.path.exists(usbdir):
		try:
			os.makedirs(usbdir)
		except:
			print("Warning: the directory exists!!!")
	args=[]
	for f in dn.keys():
		args.append((f, usbdir))
	multi_process(cp_to_usb_multi, args, 4)
	os.chdir(usbdir)
	for old in dn.keys():
		os.system("mv %s %s" % (old, dn[old]))	
	md5=open('md5', 'a')
	os.system("cat *.fastq.gz.md5 > old.md5")
	for line in open("old.md5"):
		lst = line.strip().split("  ")
		if lst[1] in dn.keys():
			md5.write("%s  %s\n" % (lst[0], dn[lst[1]]))
		else:
			md5.write("error!!!")
	md5.close()
	os.system("rm *.fastq.gz.md5 old.md5")
	os.system("md5sum -c md5 > md5.check")

if __name__ == '__main__':
	main()