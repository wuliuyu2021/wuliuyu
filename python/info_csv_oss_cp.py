#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, time
from multiprocessing import Pool

def sample_contact(seqcsv):
	cons=[]
	for line in open(seqcsv):
		lst = line.strip().split(",")	
		con="%s<=>%s" % (lst[0], lst[2])
		cons.append(con)
	return cons

def oss_cp(seqcsv, outdir, flag):
	cons=sample_contact(seqcsv)
	for con in sorted(cons):
		if flag == 'mid':
			os.system('ossutil cp -ru %s --include *%s* %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))
			print('%s*%s* osscped to %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))
		if flag == 'bf':
			os.system('ossutil cp -ru %s --include %s* %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))
			print('%s%s* osscped to %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))
		if flag == "bh":
			os.system('ossutil cp -ru %s --include *%s %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))
			print('%s*%s osscped to %s' % (con.split("<=>")[1], con.split("<=>")[0], outdir))

def main():
	seqcsv=sys.argv[1]
	outdir=sys.argv[2]
	flag=sys.argv[3]
	oss_cp(seqcsv, outdir, flag)


if __name__ == '__main__':
	main()