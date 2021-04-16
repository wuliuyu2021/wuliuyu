#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import re
import sys
import os, csv
from xlrd import open_workbook

def table_csv(index_csv):
	d={}
	for line in open(index_csv):
		lst = line.strip().split(",")
		indexID=lst[0]
		indexseq=lst[1]
		d[indexID]=indexseq
	#print("%s %s\n" % (d.keys(), d.values()))
	return d


def read_excel(file, index_csv, sheet_index=0):
	d=table_csv(index_csv)
	workbook=xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(sheet_index)
	print("工作表名称:", sheet.name, "行数:", sheet.nrows, "列数:", sheet.ncols)
	indexseq=sheet.col_values(13)
	indexid=sheet.col_values(12)
	laneid=sheet.col_values(11)
	sampleid=sheet.col_values(0)
	csv=("C:\\Users\\User\\Desktop\\index_info.csv")
	if os.path.exists(csv):
		os.remove(csv)
	with open(csv, 'a') as f:
		for i in range(len(laneid)):
			if indexid[i] in d.keys():
				index=d[indexid[i]]
			else:
				index=indexseq[i]
			f.write("%s_%s,%s,%s\n" % (sampleid[i], laneid[i], indexid[i], index))
	f.close()
	
	return csv

def dict_maker(file, index_csv, sheet_index=0, pattern="xten"):
	dn={}
	csv=read_excel(file, index_csv, sheet_index=0)
	if pattern == "xten":
		for line in open(csv):
			laneID=line.strip().split(',')[0]
			indexseq=line.strip().split(',')[2]
			dn[indexseq]=laneID
		#print("%s %s" % (len(dn.keys(), set(len(str(dn.keys()))))))
	else:
		sys.exit(1)
	return dn
	
def checker(file, index_csv, sheet_index=0, pattern="xten"):
	indexseqs=[]
	dn = dict_maker(file, index_csv, sheet_index=0, pattern="xten")
	#for info in dn.values():
	print("%s,%s" % (dn.keys(), dn.values()))
		#indexseqs.append(indexseq)
	#print("%s\n" % len(indexseqs))
	#print("%s\n" % sorted(set(indexseqs[:])))
	#if len(indexseqs) != len(set(indexseqs)):
	#	print("ERROR: duplicated index! Please check indexseq:%s!!!\n" % indexseq)
	#	sys.exit(1)
	#else:
	#	print("Correctly, No duplication!!!")
		
def main():
	index_csv=sys.argv[1]
	file=sys.argv[2]
	pattern=sys.argv[3]
	checker(file, index_csv, sheet_index=0, pattern="xten")


if __name__ == '__main__':
	main()