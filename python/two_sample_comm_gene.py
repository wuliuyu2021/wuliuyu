#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re



def info_all(infile,outdir,n1,n2):
	ds={}
	head=open(infile, "r").readlines()[0]
	
	#print(clt)
	#print(rlt)
	
	for index,sam in enumerate(head.strip().split("\t")):
		ds[sam]=index
	print(ds)
	if n1 not in ds.keys() or n2 not in ds.keys():
		print("Input samples are wrong!!!")

	if n1 in ds.keys() and n2 in ds.keys():
		print(ds[n1], ds[n2])

		return ds[n1], ds[n2]


def info_write(infile,outdir,n1, n2):
	m1=info_all(infile,outdir,n1,n2)[0]
	m2=info_all(infile,outdir,n1,n2)[1]
	print(int(m1),int(m2))
	csv=os.path.join(outdir+"/"+"%sVS%s.txt" % (n1, n2))
	csv_open=open(csv,"w")
	head="GeneID\t%sVS%s\n" % (n1,n2)
	csv_open.write(head)
	for line in open(infile, "r").readlines()[1:]:
		lst=line.strip().split("\t")
		if lst[int(m1)] != "0" and lst[int(m2)] != "0":
			csv_open.write("%s\t1\n" %lst[0])
	csv_open.close()



def main():
	infile=sys.argv[1]
	outdir=sys.argv[2]
	n1=sys.argv[3]
	n2=sys.argv[4]
	info_write(infile,outdir,n1, n2)

	

if __name__ == "__main__":
	main()
