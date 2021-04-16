#!/usr/bin/python
# -*- coding: utf-8 -*- 
''' copy wes web to outdir and pull to locality '''

import os, re, sys
from os import path


def table_split(seq_csv):
	sn={}
	for line in open(seq_csv):
		sampleID = line.strip().split(',')[0]
		sample_name = line.strip().split(',')[2]
		tag = line.strip().split(',')[12]
		data_pattern = line.strip().split(',')[15]
		for i in range(len(sampleID)):
			if tag == 'WES' and data_pattern == 'fastq/vcf':
				sn[sampleID]=sample_name
	return  sn


def get_files(indir):
	pattern = re.compile(r"(^S\d+)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if path.isdir('%s/%s' % (indir, sr)):
			print('Dirs Exist!!!')
		else:
			print('No dirs,please check!!!')
	return srs


def main():
	indir=sys.argv[1]#/thinker/nfs5/rawdatausera/test/wes_test/180316_E00602_0083_BHK2NVCCXY
	seq_csv=sys.argv[2]#/thinker/nfs2/longrw/runPipelineInfo/180316_E00602_0083_BHK2NVCCXY/sequence_180316_E00602_0083_BHK2NVCCXY.csv
	outdir=sys.argv[3]#/thinker/nfs5/rawdatausera/test/wes_web
	seq_ID=sys.argv[4]#180316_E00602_0083_BHK2NVCCXY
	sn=table_split(seq_csv)
	srs=get_files(indir)
	os.chdir(indir)
	for sr  in srs:
		if sr in sn.keys():
			os.chdir(outdir)
			os.system("mkdir -p %s/%s_%s" % (seq_ID, sr, sn[sr]))
			os.system("cp -r %s/%s/web %s/%s/%s_%s" % (indir, sr, outdir, seq_ID, sr, sn[sr]))


if __name__ == '__main__':
	main()













