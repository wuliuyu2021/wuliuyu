#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys, re, json, csv
import time
import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='A script to make genetables.')
parser.add_argument('-i','--input',type=str,dest='inputDir', required=True, help='The input directory contains all sample files')
parser.add_argument('-o','--output',type=str,dest='outputDir',required=True, help='The output directory contains all result files')
parser.add_argument("-f", "--flag",type=str,dest='flag',required=True, help='The end flag of match files' )
args = parser.parse_args()

indir = args.inputDir
outdir = args.outputDir
flag = args.flag

dfs = []
df_count = 0
if not os.path.exists(outdir):
	os.makedirs(outdir)
genetable=os.path.join(outdir,'genetable.xls')
#if os.path.exists(genetable):
#	os.remove(genetable)
pattern=re.compile(r"(.+)(%s)$" % flag)
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