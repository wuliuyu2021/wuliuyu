#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os, re, sys, csv


def table_split(csv1):
	d={}
	for line in open(csv1):
		indexID=line.strip().split(',')[0]
		indexseq=line.strip().split(',')[1]
		d[indexID]=indexseq
	return d


def main():
	csv1=sys.argv[1]
	csv2=sys.argv[2]
	dn=table_split(csv1)
	csv3=open("index_check.csv", "a")
	indexseqs=[]
	a={}
	for line in open(csv2):
		indexID=line.strip().split(',')[2]
		nID=line.strip().split(',')[0]
		if indexID in dn.keys():
			indexseq=dn[indexID]
			sampleinfo= '_'.join([nID, indexID])
			#print('%s\n' % sampleinfo)
			csv3.write("%s,%s\n" % (sampleinfo, dn[indexID]))
			indexseqs.append(indexseq)
	for i in indexseqs:
		if indexseqs.count(i) > 1:
			a[i] = indexseqs.count(i)
		print("%s\n" % a)
	csv3.close()

			
if __name__ == '__main__':
	main()