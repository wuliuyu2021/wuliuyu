#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse
import pandas as pd
import numpy as np
import json


def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to merge maf and CNVs.')
	parser.add_argument('-m','--maf',dest='maf', required=True, help='The maf file')
	#parser.add_argument('-i','--outdir',dest='outdir',required=True, help='The input directory contains all  files')
	parser.add_argument('-c','--cnvdir',dest='cnvdir',required=True, help='The dirs contains all sample CNVs.')
	#parser.add_argument('-g','--group',dest='group',required=True, type=str, 
	#	help='The strs contains all info sample group with comma split symbol,such as AVSB,BVSC,AVSC')
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains all result files')
	
	args = parser.parse_args()
	
	return args

def info_write(maf, cnvdir, outdir):
	lt=[]
	for line in open(maf,"r").readlines()[1:]:
		lst = line.strip().split("\t")
		lt.append(lst[15])
	lt=sorted(set(lt))

	for t in lt:
		tmp_open1=open(outdir+"/"+"%s.tmp1.txt" % t, "w")
		tmp_open2=open(outdir+"/"+"%s.tmp2.txt" % t, "w")
		
		for line in open(maf,"r").readlines()[1:]:
			lst = line.strip().split("\t")
			if lst[15] == os.path.basename(t).split(".tmp.txt")[0]: 
				cnv_open=open(cnvdir+"/"+"%s.sorted.rmdup.pileup.gz_CNVs" % lst[15])
				lnt=[]
				for ln in cnv_open:
					
					lns=ln.strip().split("\t")
					if lst[4] == ("chr%s" % lns[0]) and int(lns[1]) < int(lst[5]) and int(lns[2]) > int(lst[6]):
						tmp_open1.write("%s\t%s/%s\n" % (lst[0], lst[8], lns[4]))
					else:
						lnt.append("%s\t%s" % (lst[0], lst[8]))
				for l in set(lnt):
					tmp_open2.write(l+"\n")
				lnt=[]
		tmp_open1.close()
		tmp_open2.close()
		
	pattern = re.compile(r"(.+)(tmp1.txt)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(outdir)))
	for sr in srs:
		sr3=sr.replace("tmp1", "tmp3")
		tmp_open3=open(outdir+"/"+sr3, "w")
		line2=[line.strip().split("/")[0] for line in open(outdir+"/"+sr)]
		print(line2)
		if line2 != "":
			sr2=sr.replace("tmp1", "tmp2")
			for line in open(outdir+"/"+sr2 ,"r"):
				lst=line.strip()
				if lst not in line2:
					tmp_open3.write(lst+"\n")
		else:
			continue
		
		tmp_open3.close()
		#os.system("sort -n %s/%s.tmp1.txt | uniq >  %s/%s.tmp1_uniq.txt" %  (outdir, t, outdir, t))	
		#os.system("sort -n %s/%s.tmp2.txt | uniq >  %s/%s.tmp2_uniq.txt" %  (outdir, t, outdir, t))
		os.system("cat %s/%s  %s/%s > %s/%s.tmp.txt" %  (outdir, sr, outdir, sr3, outdir, os.path.basename(sr).split(".tmp1.txt")[0]))
		#temp="Gene\t%s" % os.path.basename(sr).split(".tmp1.txt")[0]
		#os.system("echo -e '%s' > %s/%s.temp.txt" %  (temp, outdir, os.path.basename(sr).split(".tmp1.txt")[0]))
		os.system("sort -n %s/%s.tmp.txt > %s/%s.temp.txt" %  (outdir, os.path.basename(sr).split(".tmp1.txt")[0], outdir, os.path.basename(sr).split(".tmp1.txt")[0]))
	os.system("rm -f %s/*tmp*" % outdir)

def tmp_maker(outdir):
	
	lt=[]
	ls=[]

	pattern=re.compile(r"(.+)(temp.txt)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(outdir)))
	for tab in tabs:
		with open("%s/%s" %(outdir, tab), "r") as f:
			lines = f.readlines()[:]
			for line in lines:
				lst = line.strip().split("\t")
				lt.append((lst[0]+"=="+lst[1]))
	print(lt)
	for tab in tabs:
	
		temper="Gene"+"\t"+os.path.basename(tab).split('.temp.txt')[0]
		csv2=os.path.join(outdir, "%s.temp.txt.tmp" % (os.path.basename(tab).split('.temp.txt')[0]))
		if os.path.exists(csv2):
			os.remove(csv2)
		csv2_open=open(csv2, "w")
		csv2_open.write(temper+"\n")
		with open("%s/%s" %(outdir, tab), "r") as f:
			lines = f.readlines()[:]
			for line in lines:
				lst = line.strip().split("\t")
				ls.append((lst[0]+"=="+lst[1]))
			for x in sorted(set(lt)):
				if x in ls:
					csv2_open.write("%s\t%s\n"% (x.split("==")[0], x.split("==")[1]))
				else:
					csv2_open.write("%s\t.\n"% x.split("==")[0])
		ls=[]
		csv2_open.close()

def cols_merge(outdir):
	pattern=re.compile(r"(.+)(temp.txt.tmp)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(outdir)))
	lst=["%s/%s" % (outdir, tab) for tab in tabs] 
	strs=" ".join(lst)
	os.system("paste %s > %s/maf_cnv.xls" % (strs, outdir))
	#os.system("rm -f %s/*temp* " % outdir)
	print("paste %s > %s/maf_cnv.xls" % (strs, outdir))

	'''dfs = []
	df_count = 0
	genetable=os.path.join(outdir,'maf_cnv.xls')
	#if os.path.exists(genetable):
	#	os.remove(genetable)
	pattern=re.compile(r"(.+)(temp.txt.tmp)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(outdir)))
	for tab in tabs:
		df= pd.read_csv(outdir+"/"+tab, sep = "\t",encoding='utf-8')
		dfs.append(df)
	#genetable_open=open(genetable, "w")
	for dfg in dfs:
		df_count += 1
		if df_count == 1:
			df = dfg
		else:
			df = pd.merge(df,dfg,how='inner',on="Gene")
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
		#print(dfs.temp(5))'''

def main():
	args = getCommands()
	maf, cnvdir, outdir=args.maf, args.cnvdir, args.outdir
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	info_write(maf, cnvdir, outdir)
	tmp_maker(outdir)
	cols_merge(outdir)
	

	

if __name__ == "__main__":
	main()
