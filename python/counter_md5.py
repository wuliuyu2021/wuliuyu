#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import re
import sys
from multiprocessing import Pool


def table_spliter(seq_csv, pID):
	d={}
	for line in open(seq_csv):
		pid = line.strip().split(',')[23]
		cID = line.strip().split(',')[5]
		sampleID = line.strip().split(',')[0]
		if pid == "%s" % pID:
			d[sampleID] = cID
	return d


def get_file(rawdir):
	sampleIDs=[]
	pattern = re.compile(r"(^S\d+)(.+)(_R1_001_R1)(_001.good.fastq.gz)$")
	sr1s = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir)))
	for sr1 in sr1s:
		sampleID = sr1.split('_')[0]
		sampleIDs.append(sampleID)
	return sr1s, sampleIDs


def cp_to_usb(rawdir, usbdir, cID):
	sampleIDs=get_file(rawdir)[1]
	for sampleID in sampleIDs:
		if sampleID == d.keys():
			os.chdir(usbdir)
			os.system("mkdir %s" % cID)



def multi_process(func, args, n=None):
	p = Pool(n)
	p.map(func, args)
	p.close()
	p.join()


def cp_to_usb_multi(args):
	rawdir=args[0]
	md5dir=args[1]
	usbdir=args[2]
	cp_to_usb(rawdir, md5dir, usbdir)


def main():
	rawdir=sys.argv[1]
	md5dir=sys.argv[2]
	usbdir=sys.argv[3]
	seq_csv=sys.argv[4]
	pID=sys.argv[5]
	cID=sys.argv[6]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	cp_to_usb(rawdir, md5dir, usbdir)
	args=[]
	d=table_spliter(seq_csv, pID)
	f1s=get_file(rawdir)[0]
		for f1 in f1s:
			os.system("cp %s %s/%s" % (f1s, usbdir, cID))
			f2s=f1s.replace("_R1_001.good.fastq.gz", "_R2_001.good.fastq.gz")
			os.system("cp %s %s/%s" % (f2s, usbdir, cID))
	args.append((rawdir, usbdir, cID))
	multi_process(cp_to_usb_multi, args, 4)
	os.chdir(md5dir)
	md5 = open(os.path.join(usbdir, "%s.md5" % cID), "a")
	for line in open("%s/All.md5" % md5dir, "r"):
		md5code=line.strip().split('/')[0]
		samplename=line.strip().split('/')[-1]
		md5.write("%s%s" % (md5code, samplename))
	md5.close()


if __name__ == '__main__':
	main()