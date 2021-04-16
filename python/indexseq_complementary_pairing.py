#!/usr/bin/python
# -*- coding = utf-8 -*-


import os, sys, re
from optparse import OptionParser
import time

#csv1='/thinker/nfs5/public/wuliuyu/index/roche-pair.csv'
#csv2='/thinker/nfs5/public/wuliuyu/index/IDT.csv'

d={"A":"T", "T":"A", "C":"G", "G":"C"}
Head="indexID,icp_I5_index\n"

def parse_cmd():
	usage=("Complementary pairing of indexseqs.\n"
		"CMD: python %prog <-c csv1> <-s csv2> <-o outdir>\n")
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-c", "--csv1", dest="csv1",
		help="the first index csv")
	parser.add_option("-s", "--csv2", dest="csv2",
		help="the second insex csv")
	parser.add_option("-o", "--outdir", dest="outdir", 
		help="the output directory")

	return parser.parse_args()


def reverse_index(csv1, csv2):
	lst1s=[]
	lst2s=[]
	#lst1_i7s=[]
	#lst2_i7s=[]
	dn={}
	if os.path.exists(csv1):
		for line in open(csv1):
			indexID1=line.strip().split(',')[0]
			indexseq1=line.strip().split(',')[1]
			#indexseqs1_i7=line.strip().split(',')[2]
			reverse_indexseq1=indexseq1[::-1]
			lst1s.append(indexID1)
			#lst1_i7s.append(indexseqs1_i7)
			dn[indexID1]=reverse_indexseq1
	if os.path.exists(csv2):
		for line in open(csv2):
			indexID2=line.strip().split(',')[0]
			indexseq2=line.strip().split(',')[1]
			#indexseqs2_i7=line.strip().split(',')[2]
			reverse_indexseq2=indexseq2[::-1]
			lst2s.append(indexID2)
			#lst2_i7s.append(indexseqs2_i7)
			dn[indexID2]=reverse_indexseq2
		
	return lst1s, lst2s, dn


def reverse_index_writer(csv1, csv2, outdir):
	lst1s=reverse_index(csv1, csv2)[0]
	lst2s=reverse_index(csv1, csv2)[1]
	#lst1_i7s=reverse_index(options)[3]
	#lst2_i7s=reverse_index(options)[4]
	dn=reverse_index(csv1, csv2)[2]
	c1=os.path.join(os.path.dirname(outdir), "reverse_roche-pair_i5.csv")
	c2=os.path.join(os.path.dirname(outdir), "reverse_IDT_i5.csv")
	if os.path.exists(c1):
		os.remove(c1)
	if os.path.exists(c2):
		os.remove(c2)
	with open(c1, "a") as f1:
		f1.write(str(Head))
		for lst1 in lst1s:
			cp_seq1="%s%s%s%s%s%s%s%s" % (d[dn[lst1][0]], d[dn[lst1][1]],d[dn[lst1][2]],d[dn[lst1][3]],
				d[dn[lst1][4]],d[dn[lst1][5]],d[dn[lst1][6]],d[dn[lst1][7]])
			f1.write("%s,%s\n" % (lst1, cp_seq1))
	f1.close()
	with open(c2, "a") as f2:
		f2.write(str(Head))
		for lst2 in lst2s:
			cp_seq2="%s%s%s%s%s%s%s%s" % (d[dn[lst2][0]], d[dn[lst2][1]],d[dn[lst2][2]],d[dn[lst2][3]],
				d[dn[lst2][4]],d[dn[lst2][5]],d[dn[lst2][6]],d[dn[lst2][7]])
			f2.write("%s,%s\n" % (lst2, cp_seq2))
	f2.close()

def main():
	time1=time.time()
	(options, args) = parse_cmd()
	csv1=options.csv1
	csv2=options.csv2
	outdir=options.outdir
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	reverse_index_writer(csv1, csv2, outdir)
	time2=time.time()
	print("Time used: %s" % str(time2 - time1))


if __name__ == '__main__':
	main()