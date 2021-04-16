#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

def hgc_sample(seqcsv):
	dn={}
	for line in open(seqcsv):
		lst = line.strip().split(",")
		hgc = lst[1]
		sample = lst[3]
		if hgc.startswith('HGC'):
			dn[hgc]=sample
	return dn

def info_change(seqcsv, md5_old):
	if os.path.exists('md5_new'):
		os.remove('md5_new')
	dn=hgc_sample(seqcsv)
	md5=open('md5_new', 'a')
	with open(md5_old, 'r') as f:
		for line in f:
			lst = line.strip().split("_")
			if lst[2].startswith('HGC'):
				md5.write('%s_%s_%s\n' % ('_'.join(lst[0:2]), dn[lst[2]], '_'.join(lst[3:])))
			else:
				md5.write('%s\n' % '_'.join(lst[:]))
	md5.close()

def main():

	seqcsv=sys.argv[1]
	md5_old=sys.argv[2]
	info_change(seqcsv, md5_old)

if __name__ == '__main__':
	main()