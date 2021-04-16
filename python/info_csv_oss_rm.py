#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, time


def sample_contact(seqcsv):
	cons=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")	
		con="%s<=>%s" % (lst[0], lst[1])
		cons.append(con)
	return cons

def cp_rm(seqcsv, ossdir, rm_yes_no):
	cons=sample_contact(seqcsv)
	for con in sorted(cons):
		if rm_yes_no == "yes":
			os.system('ossutil cp -ru %s%s_R1_001.fastq.gz %s%s_R1_001.fastq.gz' % (con.split("<=>")[1], con.split("<=>")[0], ossdir, con.split("<=>")[0]))
			os.system('ossutil cp -ru %s%s_R2_001.fastq.gz %s%s_R2_001.fastq.gz' % (con.split("<=>")[1], con.split("<=>")[0], ossdir, con.split("<=>")[0]))
			print('ossutil cp -ru %s%s %s' % (con.split("<=>")[1], con.split("<=>")[0], ossdir))
			os.system('ossutil rm -rf %s%s'% (con.split("<=>")[1], con.split("<=>")[0]))
			print('ossutil rm -rf %s%s'% (con.split("<=>")[1], con.split("<=>")[0]))
		if rm_yes_no == "no":
			os.system('ossutil cp -ru %s%s_R1_001.fastq.gz %s%s_R1_001.fastq.gz' % (con.split("<=>")[1], con.split("<=>")[0], ossdir, con.split("<=>")[0]))
			os.system('ossutil cp -ru %s%s_R2_001.fastq.gz %s%s_R2_001.fastq.gz' % (con.split("<=>")[1], con.split("<=>")[0], ossdir, con.split("<=>")[0]))
			print('ossutil cp -ru %s%s %s' % (con.split("<=>")[1], con.split("<=>")[0], ossdir))

		

def main():
	seqcsv=sys.argv[1]
	ossdir=sys.argv[2]
	rm_yes_no=sys.argv[3]
	cp_rm(seqcsv, ossdir, rm_yes_no)


if __name__ == '__main__':
	main()