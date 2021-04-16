#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os, re, sys
from os import path


def get_files(indir):
	pattern = re.compile(r"(^S\d+)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if path.isdir('%s/%s' % (indir, sr)):
			print('Dirs Exist!!!')
		else:
			sys.exit(0)
	return srs


def find_cover_report(sedir):
	datalist1=[]
	datalist2=[]
	srs=get_files(indir)
	csv1=open('%s_total_count.csv' % sedir, 'a')
	csv2=open('%s_target_count.csv' % sedir, 'a')
	for sr in srs:
		report1 = open('%s/stat/coverage.report' % sr, 'r')
		for line in report1.readlines()[26:27]:
			curline_total=line.strip().split()
			datalist1.append((sr, curline_total))
	for x in datalist1:
		csv1.write("%s\n" % (x,))
	csv1.close()
	for sr in srs:
		report2 = open('%s/stat/coverage.report' % sr, 'r')
		for line in report2.readlines()[29:30]:
			curline_target=line.strip().split()
			datalist2.append((sr, curline_target))
	for y in datalist2:
		csv2.write("%s\n" % (y,))
	csv2.close()
	


def main():
	global indir
	indir = sys.argv[1]
	sedir = sys.argv[2]
	srs = get_files(indir)
	find_cover_report(sedir)
	os.chdir(indir)
	os.system('cat %s_target_count.csv %s_total_count.csv > %s_count.csv' % (sedir, sedir, sedir))
	os.system('rm -f %s_target_count.csv %s_total_count.csv' % (sedir, sedir))
	
if __name__ == '__main__':
	main()




