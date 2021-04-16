#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from collections import Counter
from optparse import OptionParser
import pandas as pd
import numpy as np


def parse_cmd():
	usage="To make select onco csv!"
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-i","--indir",dest="indir",default=None,help="info csv dir")
	parser.add_option("-o","--outdir",dest="outdir",default=None,help="the outfile path")
	#parser.add_option("-e","--outfile",dest="outfile",default=None,help="input ccc")
	#parser.add_option("-d","--ddd",dest="ddd",default=None,help="input ddd")
	
	return parser.parse_args()

def get_files1(options):
	d={}
	lts=[]
	dn={}
	dt={}
	pattern = re.compile(r"(.+)(.anno.vcf)(.+)(multianno.xls)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))

	
	for line in open(srs[0], 'r').readlines()[1:]:
		lst = line.strip().split("\t")
		con="%s\t%s" % (lst[6], lst[8])
		lts.append(lst[6])
		d[lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]] = con
	#print(d)
	slts=Counter(lts)
	dn=sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True)
	print(dn)
	for k,v in dn:

		if int(v) >0:
			d3=[v1.split("\t")[1] for k1,v1 in d.items() if v1.split("\t")[0]==k]
			dt[k]=";".join(set(d3))
		
	#print(dt)
	outfile1 = os.path.join(options.outdir, "%s.tmp.csv" % srs[0].split("/")[-1].split(".anno.")[0])
	lst=[]
	
	with open(outfile1, 'wr') as f:
		for gene,tp in dt.items():
			f.write("%s\t%s\n" % (gene, tp))		
	f.close()
	return dt,srs

def get_files2(options):
	d={}
	lts=[]
	dn={}
	dt={}
	pattern = re.compile(r"(.+)(.anno.vcf)(.+)(multianno.xls)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))

	
	for line in open(srs[1], 'r').readlines()[1:]:
		lst = line.strip().split("\t")
		con="%s\t%s" % (lst[6], lst[8])
		lts.append(lst[6])
		d[lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]] = con
	#print(d)
	slts=Counter(lts)
	dn=sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True)
	print(dn)
	for k,v in dn:

		if int(v) >0:
			d3=[v1.split("\t")[1] for k1,v1 in d.items() if v1.split("\t")[0]==k]
			dt[k]=";".join(set(d3))
		
	outfile1 = os.path.join(options.outdir, "%s.tmp.csv" % srs[1].split("/")[-1].split(".anno.")[0])
	lst=[]
	
	with open(outfile1, 'wr') as f:
		for gene,tp in dt.items():
			f.write("%s\t%s\n" % (gene, tp))		
	f.close()
	return dt

def get_files3(options):
	d={}
	lts=[]
	dn={}
	dt={}
	pattern = re.compile(r"(.+)(.anno.vcf)(.+)(multianno.xls)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))

	
	for line in open(srs[2], 'r').readlines()[1:]:
		lst = line.strip().split("\t")
		con="%s\t%s" % (lst[6], lst[8])
		lts.append(lst[6])
		d[lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]] = con
	#print(d)
	slts=Counter(lts)
	dn=sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True)
	print(dn)
	for k,v in dn:

		if int(v) >0:
			d3=[v1.split("\t")[1] for k1,v1 in d.items() if v1.split("\t")[0]==k]
			dt[k]=";".join(set(d3))
		
	outfile1 = os.path.join(options.outdir, "%s.tmp.csv" % srs[2].split("/")[-1].split(".anno.")[0])
	lst=[]
	
	with open(outfile1, 'wr') as f:
		for gene,tp in dt.items():
			f.write("%s\t%s\n" % (gene, tp))		
	f.close()
	return dt

def get_files4(options):
	d={}
	lts=[]
	dn={}
	dt={}
	pattern = re.compile(r"(.+)(.anno.vcf)(.+)(multianno.xls)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.indir)))

	
	for line in open(srs[3], 'r').readlines()[1:]:
		lst = line.strip().split("\t")
		con="%s\t%s" % (lst[6], lst[8])
		lts.append(lst[6])
		d[lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]] = con
	#print(d)
	slts=Counter(lts)
	dn=sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True)
	print(dn)
	for k,v in dn:

		if int(v) >0:
			d3=[v1.split("\t")[1] for k1,v1 in d.items() if v1.split("\t")[0]==k]
			dt[k]=";".join(set(d3))
		
	outfile1 = os.path.join(options.outdir, "%s.tmp.csv" % srs[3].split("/")[-1].split(".anno.")[0])
	lst=[]
	
	with open(outfile1, 'wr') as f:
		for gene,tp in dt.items():
			f.write("%s\t%s\n" % (gene, tp))		
	f.close()
	return dt

	

def info_maker():
	ld=[]
	d1,d2,d3,d4={},{},{},{}
	dfs = []
	df_count = 0
	(options, args) = parse_cmd()
	get_files1(options)
	get_files2(options)
	get_files3(options)
	get_files4(options)
	srs=get_files1(options)[1]
	pattern1 = re.compile(r"(.+)(tmp.csv)$")
	ss = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(options.outdir)))
	for s in ss:
		for line in open(s, 'r'):
			lst = line.strip().split("\t")
			ld.append(lst[0])

	for line in open(ss[0], 'r'):
		lst = line.strip().split("\t")
		d1[lst[0]]=lst[1]
	for line in open(ss[1], 'r'):
		lst = line.strip().split("\t")
		d2[lst[0]]=lst[1]
	for line in open(ss[2], 'r'):
		lst = line.strip().split("\t")
		d3[lst[0]]=lst[1]
	for line in open(ss[3], 'r'):
		lst = line.strip().split("\t")
		d4[lst[0]]=lst[1]

	head="ref_gene\t%s\t%s\t%s\t%s\n" % (srs[0].split("/")[-1].split(".anno.")[0],
		srs[1].split("/")[-1].split(".anno.")[0],
		srs[2].split("/")[-1].split(".anno.")[0],
		srs[3].split("/")[-1].split(".anno.")[0])
	onco=os.path.join(options.outdir, "onco.csv")
	#onco_open=open(onco,"w")
	#onco_open.write(head)
	c1 = os.path.join(options.outdir, "%s.tmp_csv" % srs[0].split("/")[-1].split(".anno.")[0])
	h1 ="ref_gene\t%s\n" % srs[0].split("/")[-1].split(".anno.")[0]
	c1o= open(c1, "w")
	c1o.write(h1)
	c2 = os.path.join(options.outdir, "%s.tmp_csv" % srs[1].split("/")[-1].split(".anno.")[0])
	h2 ="ref_gene\t%s\n" % srs[1].split("/")[-1].split(".anno.")[0]
	c2o= open(c2, "w")
	c2o.write(h2)
	c3 = os.path.join(options.outdir, "%s.tmp_csv" % srs[2].split("/")[-1].split(".anno.")[0])
	h3 ="ref_gene\t%s\n" % srs[2].split("/")[-1].split(".anno.")[0]
	c3o= open(c3, "w")
	c3o.write(h3)
	c4 = os.path.join(options.outdir, "%s.tmp_csv" % srs[3].split("/")[-1].split(".anno.")[0])
	h4 ="ref_gene\t%s\n" % srs[3].split("/")[-1].split(".anno.")[0]
	c4o= open(c4, "w")
	c4o.write(h4)
	for ref_gene in sorted(set(ld)):
		if ref_gene in d1.keys():
			c1o.write("%s\t%s\n" % (ref_gene, d1[ref_gene]))
		else:
			c1o.write("%s\t.\n" % ref_gene)
	for ref_gene in sorted(set(ld)):
		if ref_gene in d2.keys():
			c2o.write("%s\t%s\n" % (ref_gene, d2[ref_gene]))
		else:
			c2o.write("%s\t.\n" % ref_gene)
	for ref_gene in sorted(set(ld)):
		if ref_gene in d3.keys():
			c3o.write("%s\t%s\n" % (ref_gene, d3[ref_gene]))
		else:
			c3o.write("%s\t.\n" % ref_gene)
	for ref_gene in sorted(set(ld)):
		if ref_gene in d4.keys():
			c4o.write("%s\t%s\n" % (ref_gene, d4[ref_gene]))
		else:
			c4o.write("%s\t.\n" % ref_gene)
	c1o.close()
	c2o.close()
	c3o.close()
	c4o.close()

	pattern2=re.compile(r"(.+)(tmp_csv)$")
	tabs=sorted(filter(lambda x:re.match(pattern2, x), os.listdir(options.outdir)))
	for tab in tabs:
		df= pd.read_csv(options.outdir+"/"+tab, sep = "\t",encoding='utf-8')
		dfs.append(df)
	#genetable_open=open(genetable, "w")
	for dfg in dfs:
		df_count += 1
		if df_count == 1:
			df = dfg
		else:
			df = pd.merge(df,dfg,how='inner',on="ref_gene")
	#genetable_open.write(merge_df)
	#genetable_open.close()
		to_drop = [x for x in df if '_y' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '_x_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '1_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		#to_drop = [x for x in df if '2' in x]
		#df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '2_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '3_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '4_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '5_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '6_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		df.to_csv(onco,index=None,sep = '\t',encoding='utf-8')



def main():
	info_maker()
	

if __name__ == "__main__":
	main()
