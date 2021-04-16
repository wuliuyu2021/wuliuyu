#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import gzip


def change_info(fq,outdir,a1,a2,a3,a4,flag):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	
	
	gz=gzip.open(fq,'rb')
	out=gzip.open('%s/new_%s' % (outdir, os.path.basename(fq)),'wb', compresslevel=4)
	for line in gz:
		if line.startswith('%s' % flag):
			out.write('%s:%s:%s:%s:%s\n' % (a1, a2, a3, a4, ':'.join(line.strip().split(':')[4:])))
		else:
			out.write(line)

def main():
	fq=sys.argv[1]
	outdir=sys.argv[2]
	#laneid=sys.argv[3]
	a1=sys.argv[3]
	a2=sys.argv[4]
	a3=sys.argv[5]
	a4=sys.argv[6]
	flag=sys.argv[7]
	change_info(fq,outdir,a1,a2,a3,a4,flag)

if __name__ == '__main__':
	main()