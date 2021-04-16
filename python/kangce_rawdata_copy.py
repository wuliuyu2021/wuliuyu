#!/usr/bin/python
# -*- coding: utf-8 -*-
'''copy files from hdfs/dstore to usb and add index_seq(or other infomation) to filename!!!'''

import os
import sys
import re
from multiprocessing import Pool

all_index_csv='/thinker/nfs5/public/wuliuyu/wuliuyu/csv_file/all_Indexs.csv'

def index_csv(all_index_csv):
	dl = {}
	for line in open(all_index_csv):
		lst = line.strip().split(",")
		index_ID=lst[0]
		index_seq=lst[1]
		dl[index_ID]=index_seq
	return dl

def table_split(seqcsv, all_index_csv):
	d = {}
	dl=index_csv(all_index_csv)
	for line in open(seqcsv):
		lst = line.strip().split(",")
		sample_id = lst[0]
		index_ID = lst[12]
		index_seq = lst[13]
		if index_seq == "":
			d[sample_id] = dl[index_ID]
		else:
			d[sample_id] = index_seq

	return d

def sample_contact(seqcsv, contact_id):
	lt=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")
		if lst[5] == contact_id:
			lt.append(lst[0])
	return lt


def get_dirnames(indir, seqcsv, contact_id, pid, all_index_csv):
	'''dn={old:new}'''
	dn = {}
	d = table_split(seqcsv, all_index_csv)
	lt=sample_contact(seqcsv, contact_id)
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pid)
	sr1s = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	print sr1s
	for sr1 in sr1s:
		sr2 = sr1.replace("_R1_001", "_R2_001")
		if sr1.split('_')[0] in lt:	
			index_seq1 = d[sr1.split("_")[0]]
			sr1_new=sr1
			sr1_new1 = sr1_new.replace("_L00", "_%s_L00" % index_seq1)
			dn[sr1_new] = sr1_new1
		if sr2.split('_')[0] in lt:
			index_seq1 = d[sr2.split("_")[0]]
			sr2_new=sr2
			sr2_new1 = sr2_new.replace("_L00", "_%s_L00" % index_seq1)
			dn[sr2_new] = sr2_new1

	return dn


def cp_to_usbdir(r, usbdir):
	os.system("md5sum %s > %s/%s.md5" % (r, usbdir, r))
	os.system("ds cp %s %s/%s" % (r, usbdir, r))


def cp_to_usbdir_multi(args):
	r = args[0]
	usbdir = args[1]
	cp_to_usbdir(r, usbdir)


def multi_process(func, args, n=None):
	p = Pool(n)
	p.map(func, args)
	p.close()
	p.join()


def main():
	indir = sys.argv[1]
	usbdir = sys.argv[2]
	seqcsv = sys.argv[3]
	contact_id = sys.argv[4]
	pid = sys.argv[5]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	dn = get_dirnames(indir, seqcsv, contact_id, pid, all_index_csv)
	os.chdir(indir)
	args = []
	for r in dn.keys():
		args.append((r, usbdir))
	multi_process(cp_to_usbdir_multi, args, 4)
	os.chdir(usbdir)
	os.system("cat *.fastq.gz.md5 > old_name.md5")
	for old in dn.keys():
		os.system("mv %s %s" % (old, dn[old]))
	md5 = open("md5", "a")
	for line in open("old_name.md5"):
		lst = line.strip().split("  ")
		if lst[1] in dn.keys():
			md5.write("%s  %s\n" % (lst[0], dn[lst[1]]))
		else:
			md5.write("error!!!\n")
	md5.close()
	os.system("md5sum -c md5 > md5.check")
	os.system("rm old_name.md5 *.fastq.gz.md5")



if __name__ == "__main__":
	main()