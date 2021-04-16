#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
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

def sample_pooling(seqcsv, pooling_id):
	lt=[]
	dl=[]
	dlp=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")
		if  lst[1] != '' and lst[24] == pooling_id:
			dl.append(lst[11])
			lt.append(lst[0])
	dlp=list(set(dl))
	#print(dlp)

	return lt, dlp

def get_dirnames(indir, pID, seqcsv, pooling_id):
	srs_new=[]
	data_lst=sample_pooling(seqcsv, pooling_id)[0]
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_001.fastq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	undetermineds = filter(lambda x: re.match(r'Undetermined(.+)(_001.fastq.gz)', x), os.listdir(indir))
	for sr in srs:
		if sr.split("_")[0] in data_lst:
			sr_new=sr
			srs_new.append(sr_new)

	return  srs_new, undetermineds

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
	indir = sys.argv[1]
	usbdir = sys.argv[2]
	seqcsv = sys.argv[3]
	pooling_id = sys.argv[4]
	pID = sys.argv[5]
	#lane = sys.argv[6]
	lt=sample_pooling(seqcsv, pooling_id)[0]
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	sr1s=get_dirnames(indir, pID, seqcsv, pooling_id)[0]
	for sr1 in sr1s:
		args.append((indir, sr1, usbdir))
		sr2=sr1.replace("_R1_001", "_R2_001")
		args.append((indir, sr2, usbdir))
	multi_process(cp_to_usbdir_multi, args, 4)
	d=table_split(seqcsv, all_index_csv)[0]
	dn=table_split(seqcsv, all_index_csv)[1]
	os.chdir(usbdir)
	for root, dirs, fs in os.walk(usbdir):
		for f in fs:
			if f.split('_')[1] == pID and f.endswith("fastq.gz"):
				os.system("mv %s %s_%s_%s_%s" % (f, f.split('_')[2], pooling_id, d[f.split('_')[0]], '_'.join(f.split('_')[6:])))
	os.chdir(usbdir)
	for root, dirs, fs in os.walk(usbdir):
		for f in fs:
			if f.endswith("fastq.gz"):
				os.system('md5sum %s > %s.md5' % (f, f))
	md5=open('md5', 'a')
	os.system('cat *.fastq.gz.md5 > md5')
	os.system('rm *.fastq.gz.md5')
	#os.system('md5sum -c md5 > md5.check')
	md5.close()
	undetermineds=get_dirnames(indir, pID, seqcsv, pooling_id)[1]
	dlp=sample_pooling(seqcsv, pooling_id)[1]
	for undetermined in undetermineds:
		if undetermined.split('_')[2] == 'L00%s' % dlp[0]:
			if os.path.abspath(indir).split('/')[2] == 'dstore':
				os.system('ds cp %s/%s %s/%s' % (indir, undetermined, usbdir, undetermined))
			else:
				os.system('cp %s/%s %s/%s' % (indir, undetermined, usbdir, undetermined))
	os.chdir(usbdir)
	os.system('md5sum Undetermined* >> md5')
		
if __name__ == '__main__':
	main()