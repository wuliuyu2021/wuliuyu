#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys



def sample_info(seqcsv, pID):
	d=[]
	dn={}
	for line in open(seqcsv):
		lst = line.strip().split(",")
		dn[lst[1]]=lst[3]
		fcid=os.path.basename(seqcsv).split('.csv')[0].split('_')[-1]
		sampleinfo='_'.join((lst[0],pID,lst[1],fcid))
		d.append(sampleinfo)
		#print(d)
	return dn, d

def get_files(indir, pID, seqcsv):
	data_lst=sample_info(seqcsv, pID)[1]
	srs_new=[]
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.good.fastq.gz|_001.fastq.gz|_001.fq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	#print('%s' % srs)
	for sr in srs:
		if '_'.join(sr.split("_")[:4]) in data_lst:
			sr_new=sr
			srs_new.append(sr_new)
			
	return srs_new


def main():
	indir = sys.argv[1]
	fc = sys.argv[2]
	pID = sys.argv[3]
	time="20%s" % fc.split('_')[0][0:4]
	seqcsv_sr="/thinker/nfs2/longrw/runPipelineInfo/%s/%s/sequence_%s.csv" % (time, fc, fc)
	seqcsv_sz1="/data/users/hapseq/runPipelineInfo/%s/%s/sequence_%s.csv" % (time, fc, fc)
	seqcsv_sz2="/data/users/longrw/runPipelineInfo/%s/%s/sequence_%s.csv" % (time, fc, fc)
	if os.path.exists(seqcsv_sr):
		seqcsv = seqcsv_sr
	if os.path.exists(seqcsv_sz1):
		seqcsv = seqcsv_sz1
	if os.path.exists(seqcsv_sz2):
		seqcsv = seqcsv_sz2
	dn = sample_info(seqcsv, pID)[0]
	sr1s = get_files(indir, pID, seqcsv)
	os.chdir(indir)
	for sr1 in sr1s:
		sr2 = sr1.replace("_R1_001", "_R2_001")
		if sr1.split('_')[2].startswith("HGC") and sr1.split('_')[2] in dn.keys():
			fr=sr1.split('_')[2]
			ft=dn[fr]
			sr1_new=sr1.replace('%s' % fr, '%s' % ft)
			os.system('mv %s %s' % (sr1, sr1_new))
			print('%s moves to %s'% (sr1, sr1_new))
		elif sr1.split('_')[2].startswith("HGC") and sr1.split('_')[2] not in dn.keys():
			print('HGC: %s not in Seqcsv, Please Check!!!' % sr1.split('_')[2])
		if sr2.split('_')[2].startswith("HGC") and sr2.split('_')[2] in dn.keys():
			fr=sr2.split('_')[2]
			ft=dn[fr]
			sr2_new=sr2.replace('%s' % fr, '%s' % ft)
			os.system('mv %s %s' % (sr2, sr2_new))
			print('%s moves to %s'% (sr2, sr2_new))
		elif sr2.split('_')[2].startswith("HGC") and sr2.split('_')[2] not in dn.keys():
			print('HGC: %s not in Seqcsv, Please Check!!!' % sr2.split('_')[2])

if __name__ == '__main__':
	main()