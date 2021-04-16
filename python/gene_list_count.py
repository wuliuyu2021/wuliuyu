#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import time
from collections import Counter
import pandas as pd
import numpy as np

def table_info(indir):
	pattern=re.compile(r"(.+)(anno)(.+)(multianno.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	print(tabs)

	return tabs

def read_table(indir):
	lts=[]
	tabs=table_info(indir)
	for tab in tabs:
		csv_header=("%s_gene_list,%s_gene_counter" %(os.path.basename(tab).split('.anno.vcf.')[0], os.path.basename(tab).split('.anno.vcf.')[0]))
		csv=os.path.join(indir, "%s.csv" % (os.path.basename(tab).split('.xls')[0]))
		#
		if os.path.exists(csv):
			os.remove(csv)
		#
		csv_open=open(csv, "w")
		#
		csv_open.write(csv_header+'\n')
		#row_csv_open.write(csv_header)
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				lts.append(lst[6])
		result = Counter(lts)
		for k,v in sorted(Counter(lts).items(), key=lambda item:item[1], reverse=True):
			#print(k+":"+str(v))
			csv_open.write("%s,%s\n" %(str(k), str(v)))
		#	row_csv_open.write("%s,%s" %(str(k), str(v)))
		csv_open.close()
		row_csv=os.path.join(indir,"%s_row.csv" %(os.path.basename(tab).split('.xls')[0]))
		if os.path.exists(row_csv):
			os.remove(row_csv)
		df = pd.read_csv(csv)
		data = df.values
		index1 = list(df.keys())
		#data = df.as_matrix()
		data = list(map(list,zip(*data)))
		data = pd.DataFrame(data, index=index1)
		data.to_csv(row_csv,header=0)
		#row_csv_open.close()
	

'''def csv_info(indir):
	pattern=re.compile(r"(.+)(anno)(.+)(multianno.csv)$")
	csvs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))

	return csvs

def csv_trans(indir):
	csvs=csv_info(indir)
	print(csvs)
	for csv in csvs:
		#print(df.dtypes)'''

def main():
	indir=sys.argv[1]
	#table=sys.argv[2]
	time1=time.time()
	read_table(indir)
	#csv_trans(indir)
	time2=time.time()
	print("Time used: %s" %(str(time2-time1)))


if __name__ == '__main__':
	main()