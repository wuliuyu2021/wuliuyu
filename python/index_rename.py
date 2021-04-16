#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re

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
	dn = {}
	dl=index_csv(all_index_csv)
	for line in open(seqcsv):
		lst = line.strip().split(",")
		sample_id = lst[0]
		index_ID = lst[12]
		index_seq1 = lst[13]
		index_seq2 = lst[15]
		if index_seq1 != "" and index_seq2 != "":
			lst = '%s_%s' % (index_seq1, index_seq2)
			dn[sample_id] = lst
		if index_seq1 == "" and index_seq2 != "":
			lst = '%s_%s' % (dl[index_ID], index_seq2)
			dn[sample_id] = lst
		if index_seq1 == "" and index_seq2 == "":
			d[sample_id] = dl[index_ID]
		if index_seq1 != "" and index_seq2 == "":
			d[sample_id] = index_seq1
			
	return d, dn


def sample_contact(seqcsv, contact_id):
	lt=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")
		if lst[5] == contact_id:
			lt.append(lst[0])
	return lt

def rename(indir, seqcsv, contact_id, pid, all_index_csv):
	d = table_split(seqcsv, all_index_csv)[0]
	dn = table_split(seqcsv, all_index_csv)[1]
	lt=sample_contact(seqcsv, contact_id)
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz)$" % pid)
	sr1s = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr1 in sr1s:
		sr2 = sr1.replace("_R1_001", "_R2_001")
		if sr1.split('_')[0] in lt:
			if dn[sr1.split("_")[0]] != "":
				os.system("mv %s %s_%s_%s" % (sr1, '_'.join(sr1.split('_')[0:5]), dn[sr1.split("_")[0]], '_'.join(sr1.split('_')[5:])))
			else:
				os.system("mv %s %s_%s_%s" % (sr1, '_'.join(sr1.split('_')[0:5]), d[sr1.split("_")[0]], '_'.join(sr1.split('_')[5:])))
		if sr2.split('_')[0] in lt:
			if dn[sr2.split("_")[0]] != "":
				os.system("mv %s %s_%s_%s" % (sr2, '_'.join(sr2.split('_')[0:5]), dn[sr2.split("_")[0]], '_'.join(sr2.split('_')[5:])))
			else:
				os.system("mv %s %s_%s_%s" % (sr2, '_'.join(sr2.split('_')[0:5]), d[sr2.split("_")[0]], '_'.join(sr2.split('_')[5:])))


if __name__ == '__main__':
	indir=sys.argv[1]
	seqcsv=sys.argv[2]
	contact_id=sys.argv[3]
	pid=sys.argv[4]
	rename(indir, seqcsv, contact_id, pid, all_index_csv)