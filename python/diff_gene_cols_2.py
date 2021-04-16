#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys



def sample_info(seqcsv):
	dn={}
	for line in open(seqcsv):
		lst = line.strip().split("\t")
		dn[lst[0]]=lst[1]
		#print(d)
	return dn



def main():
	
	seqcsv = sys.argv[1]
	outdir = sys.argv[2]
	dn = sample_info(seqcsv)
	new_csv=os.path.join(outdir, "new_%s" % os.path.basename(seqcsv))
	csv=open(new_csv, 'w')
	for key in dn.keys():
		csv.write('%s\t%s\n' % (key, 2))
	csv.close()

if __name__ == '__main__':
	main()