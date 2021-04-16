#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re 
import sys
from sr_seqcsv import Seqcsv
from pecheck_info import Pecheck
from optparse import OptionParser

def parse_cmd():
	usage = (
		"Quality Control for Illumina raw fastq reads data\n"
		"CMD: python %prog <-j jsondir> <-o outdir> <-p pid> <-s seqcsv>\n")
	version = "%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	'''parser.add_option(
		"-i", "--indir", dest="indir",
		help="the raw fastq files directory")'''
	parser.add_option(
		"-j", "--jsondir", dest="jsondir",
		help="the json files directory")
	parser.add_option(
		"-o", "--outdir", dest="outdir", default=None,
		help="the output directory")
	parser.add_option(
		"-s", "--seqcsv", dest="seqcsv",
		help="the seqinfo csv")
	parser.add_option(
		"-p", "--pid", dest="pid", default=None,
		help="specify the project id, default is None")

	return parser.parse_args()

def sample_info_preparation(options):
	ld=[]
	for line in open(options.seqcsv):
		lst = Seqcsv(line.strip().split(','))
		if lst.pID == options.pid:
			l_info='%s_%s_%s' % (lst.ordID, lst.pID, lst.libID)
			ld.append(l_info)
	if ld is None:
		print('Warning, Wrong pid, Please check!!!' * 3)
	return ld

'''def get_dirnames(options):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_001.fastq|_001.fastq.gz|_001.fq.gz)$" % options.pid)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))
	return srs'''

def get_jsons(options):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+).json$" % options.pid)
	js = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.jsondir)))
	return js

def info_writer():
	(options, args) = parse_cmd()
	ld=sample_info_preparation(options)
	js=get_jsons(options)
	os.chdir(options.jsondir)
	head_sample_line=('seqID,LaneID,Sample,libID,read1_bases,read2_bases,passed/failed,Yeild(G)')
	sam_f=os.path.join(options.outdir, '%s_%s_sample.csv' % ('_'.join(os.path.basename(options.seqcsv).split('.csv')[0].split('_')[1:5]), options.pid))
	sam_lst=open(sam_f, 'w')
	sam_lst.write(head_sample_line+'\n')
	js.sort()
	for j in js:
		if '_'.join(j.split('_')[:3]) in ld:
			f=open(j, 'r')
			pecheck=Pecheck(f)
			if pecheck.result == 'passed':
				sam_lst.write('%s,%s,%s,%s,%s,%s,%s,%.4f\n' % ('_'.join(os.path.basename(options.seqcsv).split('.csv')[0].split('_')[1:5]), os.path.basename(j).split('_')[5][-1], 
					os.path.basename(j).split('_')[0], os.path.basename(j).split('_')[2], pecheck.read1_bases, pecheck.read2_bases, pecheck.result, 
					(float(pecheck.read1_bases) + float(pecheck.read2_bases)) / 1000**3))
			elif pecheck.result == 'failed':
				print('Warning, R1_read_num was not equal to R2_read_num, please check!!!'*3)
	sam_lst.close()

def main():
	info_writer()
	
if __name__ == '__main__':
	main()