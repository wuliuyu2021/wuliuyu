#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv
import time


'''def sample_info(seqcsv):
	dlt=[]
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		fcid=os.path.basename(seqcsv).split('.csv')[0].split('_')[-1]
		sampleinfo='_'.join((lst.ordID, lst.projectID, lst.libID, fcid))
		dlt.append(sampleinfo)
	
	return sorted(set(sample_info(seqcsv)))'''


def get_files(seqcsv, indir):
	#dlt=sample_info(seqcsv)[0]
	data_lst=[]
	pattern = re.compile(r"(^S\d+)(.+)(_R1)(_001.good.fastq.gz|_001.fastq.gz|_001.fq.gz)$")
	#pattern2 = re.compile(r"(^S\d+)(_%s_)(.+)(_R2)(_001.good.fastq.gz|_001.fastq.gz|_001.fq.gz)$" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr1 in srs:
		sr2 =  sr1.replace("_R1_001", "_R2_001")
		#if '_'.join(sr1.split("_")[:4]) in dlt:
		if  os.path.exists('%s/%s' % (indir, sr1)) and os.path.exists('%s/%s' % (indir, sr2)):
			sr_new='_'.join(sr1.split("_")[:4])
			data_lst.append(sr_new)
	
	return data_lst


def monitor(seqcsv, indir, seqcsv_raws):
	
	while True:
		lsts=sorted(set(get_files(seqcsv, indir)))
		if len(lsts) == int(seqcsv_raws):
			time1=time.time()
			print("[%s]: success, samples qc start!!!" % time.ctime())
			os.system("sh %s/%s_sample_qc.sh" % (seqcsv.split('/sequence')[0], os.path.basename(seqcsv).split('sequence_')[-1].split('.csv')[0]))
			time2=time.time()
			print('Time used: %s' % str(time2 - time1))
			break
		else:
			print("[%s]: failed, rawfq are not ready, please wait!!!" % time.ctime())
			time.sleep(600)
			continue
		return False

def main():
	seqid=sys.argv[1]
	indir=sys.argv[2]
	seqcsv_raws=sys.argv[3]
	if not os.path.exists(indir):
		print('Warning, NO seqdir, please check!!!')
		os.exit(0)
	srcsv = "/thinker/nfs2/longrw/runPipelineInfo/20%s/%s/sequence_%s.csv" % (seqid.split('_')[0][0:4], seqid, seqid)
	bjcsv = "/thinker/storage/runPipelineInfo/20%s/%s/sequence_%s.csv" % (seqid.split('_')[0][0:4], seqid, seqid)
	if os.path.exists(srcsv):
		print('SR_csv: sequence_%s.csv exists' % seqid)
		seqcsv=srcsv
	if os.path.exists(bjcsv):
		print('BJ_csv: sequence_%s.csv exists' % seqid)
		seqcsv=bjcsv
	if not os.path.exists(srcsv) and not os.path.exists(bjcsv):
		print('Warning, NO seqcsv or PipelineInfo dir, please check!!!')
		os.exit(0)
	if not os.path.exists("%s/%s_sample_qc.sh" % (seqcsv.split('/sequence')[0], seqid)):
		print('Warning, NO %s_sample_qc.sh, please check!!!' % seqcsv.split('/sequence')[0])
		os.exit(0)
	monitor(seqcsv, indir, seqcsv_raws)



if __name__ == '__main__':
	main()