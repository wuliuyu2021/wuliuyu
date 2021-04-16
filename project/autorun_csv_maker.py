#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv


def index_csv(basicdir):
	dl = {}
	if basicdir == 'sr':
		for line in open('/thinker/nfs5/public/wuliuyu/wuliuyu/csv_file/all_Indexs.csv'):
			lst = line.strip().split(",")
			index_ID=lst[0]
			index_seq=lst[1]
			dl[index_ID]=index_seq

	if basicdir == 'sz':
		for line in open('/data/users/wuliuyu/wuliuyu/csv_file/all_Indexs.csv'):
			lst = line.strip().split(",")
			index_ID=lst[0]
			index_seq=lst[1]
			dl[index_ID]=index_seq

	return dl

def sample_info(seqcsv, outdir, basicdir):
	dl=index_csv(basicdir)
	d_lane=[]
	ls_lane=[]
	d_projectID=[]
	ls_projectID=[]
	lst_lane_indexs=[]
	d_pid_sample={}
	d_pid_count={}
	sample_info_csv=os.path.join(outdir, 'sample_info.csv')
	csv3=open(sample_info_csv, 'w')
	indexseq=''
	sample_if=''
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		sample_lst="%s_%s_%s_%s" % (lst.ordID, lst.projectID, lst.libID, os.path.basename(seqcsv).split('.csv')[0].split('_')[-1])
		if lst.indexID != '' and lst.indexID in dl.keys():
			indexseq=dl[lst.indexID]
		elif lst.indexID == '' and lst.indexSeq != "":
			indexseq=lst.indexSeq
		if not lst.libID.startswith('HGC') and lst.sample_num == '':
			sample_if=lst.libID
		elif lst.libID.startswith('HGC') and lst.sample_num != '':
			sample_if=lst.sample_num
		csv3.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (sample_lst, lst.whereFromID, os.path.basename(seqcsv).split('.csv')[0].split('_')[-1],
			lst.laneID, indexseq, lst.index2Seq, lst.poolID, lst.projectID, sample_if))
		d_lane.append(lst.laneID)
		d_projectID.append(lst.projectID)
		d_pid_sample[lst.ordID]=lst.projectID
		#d_lane_i7[lst.laneID]=str(len(indexseq))
		if lst.index2Seq != '':
			lst_lane_index='%s-%s-%s' % (lst.laneID, str(len(indexseq)), str(len(lst.index2Seq)))
			lst_lane_indexs.append(lst_lane_index)
		else:
			lst_lane_index='%s-%s-0' % (lst.laneID, str(len(indexseq)))
			lst_lane_indexs.append(lst_lane_index)
	csv3.close()
	ls_lane=sorted(set(d_lane))
	ls_projectID=sorted(set(d_projectID))
	for project in ls_projectID:
		d_pid_count[project]={
		"num":0
		}
	for sample_ord in d_pid_sample.keys():
		d_pid_count[d_pid_sample[sample_ord]]["num"] += 1

	return ls_lane, ls_projectID, lst_lane_indexs, d_pid_sample, d_pid_count


def csv_writer(seqcsv,outdir,basicdir,mismatch):
	fc_time=os.path.basename(seqcsv).split('.csv')[0].split('_')[1][0:4]
	fc='_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5])
	qc_md5_batch_v1_0_1_header=("sample_csv,contract_id,flag,if_deliver,instance_count,oss_outdir,outdir,project_dir,reads_to_process,sample")
	nova_bcl2fastq_by_lane_header=("rawseqfile,SampleSheet,barcode_mismatches,basesmask,create_fastq_for_index_reads,index_name,is_clinic,"
	"lane,mask_short_adapter_reads,minimum_trimmed_read_length,no_lane_splitting,tiles,sample")
	nova_bcl2fastq_by_lane_csv=os.path.join(outdir, 'nova_bcl2fastq_by_lane.csv')
	qc_md5_batch_v1_0_1_csv=os.path.join(outdir, 'qc_md5_batch_v1_0_1.csv')
	csv1=open(nova_bcl2fastq_by_lane_csv, 'w')
	csv2=open(qc_md5_batch_v1_0_1_csv, 'w')
	ls_lane=sample_info(seqcsv, outdir, basicdir)[0]
	ls_projectID=sample_info(seqcsv, outdir, basicdir)[1]
	lst_lane_indexs=sample_info(seqcsv, outdir, basicdir)[2]
	d_pid_sample=sample_info(seqcsv, outdir, basicdir)[3]
	d_pid_count=sample_info(seqcsv, outdir, basicdir)[4]
	csv1.write('%s\n' % nova_bcl2fastq_by_lane_header)
	csv2.write('%s\n' % qc_md5_batch_v1_0_1_header)
	ls=[]
	print(sorted(set(lst_lane_indexs)))
	for sli in sorted(set(lst_lane_indexs)):
		if sli.split('-')[-1] == '0' and sli.split('-')[1] =='8':
			csv1.write('oss://sz-hapseq/rawseq/20%s/%s/RunInfo.xml,oss://sz-hapbin/runPipelineInfo/20%s/%s/SampleSheet_lane%s_I8-0.csv,%s,"--use-bases-mask Y150n,I8,N*,Y150n",,I8-0,0,%s,,,,s_[1-8],%s_Lane%s_I8-0\n' % 
				(fc_time,fc,fc_time,fc,sli.split('-')[0],mismatch,sli.split('-')[0],fc,sli.split('-')[0]))
		elif sli.split('-')[-1] == '0' and sli.split('-')[1] =='6':
			csv1.write('oss://sz-hapseq/rawseq/20%s/%s/RunInfo.xml,oss://sz-hapbin/runPipelineInfo/20%s/%s/SampleSheet_lane%s_I6-0.csv,%s,"--use-bases-mask Y150n,I6nn,N*,Y150n",,I6-0,0,%s,,,,s_[1-8],%s_Lane%s_I6-0\n' % 
				(fc_time,fc,fc_time,fc,sli.split('-')[0],mismatch,sli.split('-')[0],fc,sli.split('-')[0]))
		elif sli.split('-')[-1] == '8' and sli.split('-')[1] =='8':
			csv1.write('oss://sz-hapseq/rawseq/20%s/%s/RunInfo.xml,oss://sz-hapbin/runPipelineInfo/20%s/%s/SampleSheet_lane%s_I8-8.csv,%s,"--use-bases-mask Y150n,I8,I8,Y150n",,I8-8,0,%s,,,,s_[1-8],%s_Lane%s_I8-8\n' % 
				(fc_time,fc,fc_time,fc,sli.split('-')[0],mismatch,sli.split('-')[0],fc,sli.split('-')[0]))
		elif sli.split('-')[-1] == '6' and sli.split('-')[1] =='8':
			csv1.write('oss://sz-hapseq/rawseq/20%s/%s/RunInfo.xml,oss://sz-hapbin/runPipelineInfo/20%s/%s/SampleSheet_lane%s_I8-6.csv,%s,"--use-bases-mask Y150n,I8,I6nn,Y150n",,I8-6,0,%s,,,,s_[1-8],%s_Lane%s_I8-6\n' % 
				(fc_time,fc,fc_time,fc,sli.split('-')[0],mismatch,sli.split('-')[0],fc,sli.split('-')[0]))
		elif sli.split('-')[-1] == '8' and sli.split('-')[1] =='6':
			csv1.write('oss://sz-hapseq/rawseq/20%s/%s/RunInfo.xml,oss://sz-hapbin/runPipelineInfo/20%s/%s/SampleSheet_lane%s_I6-8.csv,%s,"--use-bases-mask Y150n,I6nn,I8,Y150n",,I6-8,0,%s,,,,s_[1-8],%s_Lane%s_I6-8\n' % 
				(fc_time,fc,fc_time,fc,sli.split('-')[0],mismatch,sli.split('-')[0],fc,sli.split('-')[0]))
		else:
			print('No such indexs, Please check!!!')
	csv1.close()
	print(ls_projectID)
	for projectID in ls_projectID:
		if projectID in  sorted(set(d_pid_sample.values())):
			csv2.write('oss://sz-hapbin/runPipelineInfo/20%s/%s/oss_qc_csv/%s_%s_oss_qc.csv,,%s,no,%s,%s,%s,,42000000,%s_%s\n' % (fc_time,fc,fc.split('_')[-1],projectID,projectID, d_pid_count[projectID]["num"],fc,fc,fc,projectID))
			ls *= 0
	csv2.close()

def main():
	seqcsv=sys.argv[1]
	outdir=sys.argv[2]
	mismatch=sys.argv[3]
	basicdir=sys.argv[4]
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	csv_writer(seqcsv,outdir,basicdir,mismatch)

if __name__ == '__main__':
	main()