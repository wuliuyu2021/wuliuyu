#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys, re, json, csv
import time
import argparse
import pandas as pd
import numpy as np

def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to figure out the common and different genes between the wes/wgs snp and indel anno results.')
	parser.add_argument('-i','--input',type=str,dest='inputDir', required=True
				, help='The input directory contains all sample files')
	parser.add_argument('-o','--output',type=str,dest='outputDir',required=True
				, help='The output directory contains all result files')
	args = parser.parse_args()
	return args

def table_info(indir):
	pattern=re.compile(r"(.+)(anno)(.+)(multianno.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	print(tabs)

	return tabs

def venn_cmd(indir,outdir):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	tabs=table_info(indir)
	work=os.path.join(outdir, "work.sh")
	if os.path.exists(work):
		os.remove(work)
	work_open=open(work, "w")
	for tab in tabs:
		if os.path.basename(tab).split('.anno.')[0].endswith("snp"):
			work_open.write('Rscript venn.R %s, out\n\n' % (os.path.basename(tab).split('.anno.')[0]))
		if os.path.basename(tab).split('.anno.')[0].endswith("indel"):
			work_open.write('Rscript venn.R %s, out\n\n' % (os.path.basename(tab).split('.anno.')[0]))

def read_table(indir):
	tabs=table_info(indir)
	header="geneID"
	for tab in tabs:
		csv1=os.path.join(indir, "%s.txt" % (os.path.basename(tab).split('.anno.')[0]))
		if os.path.exists(csv1):
			os.remove(csv1)
		csv1_open=open(csv1, "w")
		csv1_open.write(header+"\t"+"\n")
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				ch_info=lst[0]
				ch_s=lst[1]
				ch_e=lst[2]
				ch_r=lst[3]
				ch_a=lst[4]
				csv1_open.write(ch_info+"_"+ch_s+"_"+ch_e+"_"+ch_r+"_"+ch_a+"\t"+"\n")
		csv1_open.close()
	print(">>>All gene split complete!\n")

def genetable_tmp_maker(indir):
	
	lt=[]
	ls=[]
	#if  os.path.exists(outdir):
	#	os.remove(outdir)
	#if not os.path.exists(outdir):
	#	os.makedirs(outdir)
	#genetable=os.path.join(outdir,'genetable.xls')
	#if os.path.exists(genetable):
	#	os.remove(genetable)
	pattern=re.compile(r"(.+)(txt)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	for tab in tabs:
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				lt.append(lst[0])
	for tab in tabs:
	
		header="geneID"+"\t"+os.path.basename(tab).split('.txt')[0]
		csv2=os.path.join(indir, "%s.txt.tmp" % (os.path.basename(tab).split('.txt')[0]))
		if os.path.exists(csv2):
			os.remove(csv2)
		csv2_open=open(csv2, "w")
		csv2_open.write(header+"\t"+"\n")
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				ls.append(lst[0])
			for x in sorted(set(lt)):
				if x in ls:
					csv2_open.write("%s\t%s\n"% (x, 1))
				else:
					csv2_open.write("%s\t%s\n"% (x, 0))
		ls=[]
		csv2_open.close()

def genetable_merge_maker(indir,outdir):
	dfs = []
	df_count = 0
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	genetable=os.path.join(outdir,'genetable.xls')
	#if os.path.exists(genetable):
	#	os.remove(genetable)
	pattern=re.compile(r"(.+)(txt.tmp)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	for tab in tabs:
		df= pd.read_csv(indir+"/"+tab, sep = "\t",encoding='utf-8')
		dfs.append(df)
	#genetable_open=open(genetable, "w")
	for dfg in dfs:
		df_count += 1
		if df_count == 1:
			df = dfg
		else:
			df = pd.merge(df,dfg,how='inner',on="geneID")
	#genetable_open.write(merge_df)
	#genetable_open.close()
		to_drop = [x for x in df if '_y' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '_x_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '1_x' in x]
		#df.drop(to_drop, axis=1, inplace=True)
		#to_drop = [x for x in df if '2' in x]
		df.drop(to_drop, axis=1, inplace=True)
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
		df.to_csv(genetable,index=None,sep = '\t',encoding='utf-8')
		#print(dfs.head(5))




def main():
	args = getCommands()
	indir = args.inputDir
	outdir = args.outputDir
	time1=time.time()
	read_table(indir)
	genetable_tmp_maker(indir)
	genetable_merge_maker(indir, outdir)
	venn_cmd(indir,outdir)
	time2=time.time()
	print("Time used: %s" %(str(time2-time1)))

if __name__ == '__main__':
	main()
