#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re 
import sys
from sr_seqcsv import Seqcsv
from fastp_info import Fastp
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
	'''parser.add_option(
		"-s", "--seqcsv", dest="seqcsv",
		help="the seqinfo csv")'''
	'''parser.add_option(
		"-p", "--pid", dest="pid", default=None,
		help="specify the project id, default is None")'''

	return parser.parse_args()

'''def sample_info_preparation(options):
	ld=[]
	for line in open(options.seqcsv):
		lst = Seqcsv(line.strip().split(','))
		if lst.pID == options.pid:
			l_info='%s_%s_%s' % (lst.ordID, lst.pID, lst.libID)
			ld.append(l_info)
	if ld is None:
		print('Warning, Wrong pid, Please check!!!' * 3)
	return ld

	def get_dirnames(options):
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_001.fastq|_001.fastq.gz|_001.fq.gz)$" % options.pid)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))
	return srs'''

def get_jsons(options):
	pattern = re.compile(r"(.+).json$" )
	js = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.jsondir)))
	return js

def info_writer():
	(options, args) = parse_cmd()
	#ld=sample_info_preparation(options)
	js=get_jsons(options)
	head_sample_line=('Sample,Raw_Yield(G),Raw_Reads_Num(M),Raw_Q30(%),Raw_Q20(%),'
		'Raw_GC(%),Clean_Yield(G),Clean_Reads_Num(M),Clean_Q30(%),Clean_Q20(%),Clean_GC(%),Effective(%),'
		'Duplication_Rate(%)')
	sam_f=os.path.join(options.outdir, 'qc_sample.csv')
	sam_lst=open(sam_f, 'w')
	sam_lst.write(head_sample_line+'\n')
	os.chdir(options.jsondir)
	js.sort()
	for j in js:
		if j.split('.json')[0] != "":
			f=open(j, 'r')
			fastp=Fastp(f)
			sam_lst.write('%s,%.4f,%.2f,%.2f,%.2f,%.2f,%.4f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n' % 
				( 
				os.path.basename(j).split('.json')[0], 
				float(fastp.raw_bases_num) / 1000**3,
				float(fastp.raw_reads_num) / 1000**2,
				float(fastp.raw_q30_rate) * 100,
				float(fastp.raw_q20_rate) * 100,
				float(fastp.raw_gc_content) * 100,
				float(fastp.clean_bases_num) / 1000**3,
				float(fastp.clean_reads_num) / 1000**2,
				float(fastp.clean_q30_rate) * 100,
				float(fastp.clean_q20_rate) * 100,
				float(fastp.clean_gc_content) * 100, 
				(float(fastp.clean_bases_num) / float(fastp.raw_bases_num)) * 100,
				float(fastp.dup_rate) * 100))
	sam_lst.close()

def main():
	info_writer()
	
if __name__ == '__main__':
	main()