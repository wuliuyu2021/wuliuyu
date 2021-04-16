#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import time
#from collections import Counter
#import pandas as pd
#import numpy as np

def table_info(indir,outdir):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	os.chdir(outdir)
	os.system("rm -f *tmp*")
	pattern=re.compile(r"(.+)(snp.anno)(.+)(multianno.xls)$")
	tabs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for snp in tabs:
		indel=snp.replace("snp", "indel")
		s_xls=os.path.join(outdir,"%s.snp.tmp.xls" % os.path.basename(snp).split('_snp.anno.vcf')[0])
		i_xls=os.path.join(outdir,"%s.indel.tmp.xls" % os.path.basename(indel).split('_indel.anno.vcf')[0])
		snp_open=open(s_xls,"w")
		indel_open=open(i_xls,"w")
		for line in open(indir+"/"+snp):
			snp_open.write("snp\t%s" % "\t".join(line.split("\t")[:]))
		for line in open(indir+"/"+indel):
			indel_open.write("indel\t%s" % "\t".join(line.split("\t")[:]))
		snp_open.close()
		indel_open.close()
		os.system("sed -i '1d' %s/%s.indel.tmp.xls" % (outdir, os.path.basename(indel).split('_indel.anno.vcf')[0]))
		os.system("cat %s/%s.snp.tmp.xls %s/%s.indel.tmp.xls > %s/%s_tmp.xls" % (outdir,os.path.basename(snp).split('_snp.anno.vcf')[0],
			outdir, os.path.basename(indel).split('_indel.anno.vcf')[0], 
			outdir, os.path.basename(snp).split('_snp.anno.vcf')[0]))
	pattern2=re.compile(r"(.+)(_tmp.xls)$")
	tab2s = sorted(filter(lambda x: re.match(pattern2, x), os.listdir(outdir)))
	print(tab2s)
	return tab2s


def read_table(indir,outdir):

	tabs=table_info(indir, outdir)
	for tab in tabs:
		print(tab)
		head=open(outdir+"/"+tab, "r").readlines()[0]
		header="Type\t%s\tVAF\n" % "\t".join(head.strip().split("\t")[1:])
		csv1=os.path.join(outdir, "%s.anno.vcf.hg19_multianno.xls" % (os.path.basename(tab).split('_tmp.xls')[0]))
		csv1_open=open(csv1, "w")
		csv1_open.write(header)
		with open("%s/%s" %(outdir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				AD=lst[71].split(" ")[-1].split(':')[1].split(",")[-1]
				DP=lst[71].split(" ")[-1].split(':')[2]
				if  int(AD) !=0 and int(DP) != 0 :
					VAF=float("%.4f" % (float(AD)/float(DP)))
					csv1_open.write("%s\t%s\n" % ("\t".join(line.strip().split("\t")[:]),str(VAF)))
				if   int(AD) ==0 or  int(DP) == 0:
					csv1_open.write("%s\t0\n" % ("\t".join(line.strip().split("\t")[:])))
			
		csv1_open.close()



def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]
	time1=time.time()
	table_info(indir,outdir)
	read_table(indir,outdir)
	time2=time.time()
	print("Time used: %s" %(str(time2-time1)))


if __name__ == '__main__':
	main()