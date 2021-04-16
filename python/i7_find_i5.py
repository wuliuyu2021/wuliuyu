#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

def untop_csv(untop):
	dn={}
	for line in open(untop, 'r'):
		lst = line.strip().split(',')
		dn[lst[0]]=lst[1]
	return dn


def seq_csv(csv, untop, outdir):
	dn=untop_csv(untop)
	lt=os.path.join(outdir, 'new_i7_i5_info.csv')
	f=open(lt,'w')
	for line in open(csv, 'r'):
		lst = line.strip().split(',')
		li7 = lst[13]
		if li7 in dn.keys():
			f.write('%s_%s,%s\n' %(lst[0], li7, dn[li7]))
	f.close()

def main():
	csv=sys.argv[1]
	untop=sys.argv[2]
	outdir=sys.argv[3]
	seq_csv(csv, untop, outdir)

if __name__ == '__main__':
	main()