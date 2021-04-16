#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import gzip

def get_number(fqdir, laneid):
	lst=[]
	for root,dirs,fs in os.walk(fqdir):
		fs.sort()
		for f in fs:
			if f.endswith('gz') and f.split('_')[5][-1] == laneid:
				lst.append(f)
	return lst

def change_info(fqdir,laneid,outdir,a1,a2,a3,a4,flag):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	lst=get_number(fqdir,laneid)
	for f in lst:
		gz=gzip.open('%s/%s' % (fqdir, f),'rb')
		out=gzip.open('%s/new_%s' % (outdir, f),'wb', compresslevel=4)
		for line in gz:
			if line.startswith('%s' % flag):
				out.write('%s:%s:%s:%s:%s\n' % (a1, a2, a3, a4, ':'.join(line.strip().split(':')[4:])))
			else:
				out.write(line)
def main():
	fqdir=sys.argv[1]
	outdir=sys.argv[2]
	laneid=sys.argv[3]
	a1=sys.argv[4]
	a2=sys.argv[5]
	a3=sys.argv[6]
	a4=sys.argv[7]
	flag=sys.argv[8]
	change_info(fqdir,laneid,outdir,a1,a2,a3,a4,flag)

if __name__ == '__main__':
	main()