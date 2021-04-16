#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse
from fastp_info import Fastp



def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to make fastp json passed csvs.')
	parser.add_argument('-i','--indir',dest='indir', required=True, help='The input directory contains all json files')
		
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains all result files')
	
	args = parser.parse_args()
	
	return args

def info_write(indir, outdir):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	sam_f=os.path.join(outdir, 'passed.csv')
	head="Sample,raw_reads_num,passed_filter_reads,low_quality_reads,too_many_N_reads,too_short_reads,too_long_reads,adapter_trimmed_reads\n"
	sam_f_open=open(sam_f, "w")
	sam_f_open.write(head)
	pattern = re.compile(r"(.+)(.json)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		print(sr)
		f=open(sr, 'r')
		fastp=Fastp(f)
		sam_f_open.write("%s,%s,%s %.4f%%,%s %.4f%%,%s %.4f%%,%s %.4f%%,%s %.4f%%,%s %.4f%%\n" %
			(os.path.basename(sr).split(".json")[0],fastp.raw_reads_num,
			fastp.passed_filter_reads, float(fastp.passed_filter_reads) / float(fastp.raw_reads_num) * 100,
			fastp.low_quality_reads, float(fastp.low_quality_reads) / float(fastp.raw_reads_num) *100,
			fastp.too_many_N_reads, float(fastp.too_many_N_reads) / float(fastp.raw_reads_num) *100,
			fastp.too_short_reads, float(fastp.too_short_reads) / float(fastp.raw_reads_num) *100,
			fastp.too_long_reads, float(fastp.too_long_reads) / float(fastp.raw_reads_num) *100,
			fastp.adapter_trimmed_reads, float(fastp.adapter_trimmed_reads) / float(fastp.raw_reads_num) *100))
	sam_f_open.close()



def main():
	args = getCommands()
	indir, outdir=args.indir,args.outdir
	info_write(indir, outdir)
	

	

if __name__ == "__main__":
	main()
