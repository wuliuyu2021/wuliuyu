#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
#Basedir = '/thinker/nfs5/public/rawdata/dir_cat'

def rawfq(rawdir1):
	pattern1 = re.compile(r"(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz|.fastq.gz)$")
	srs1 = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(rawdir1)))
	print('%s' % srs1)
	return srs1

def seqcsv(csv):
	d1={}
	for line in open(csv):
		lst = re.split('[,\t]',line.strip())
		d1[lst[0]] = lst[1]
		
	return d1

def rename(rawdir1, csv):
	srs1=rawfq(rawdir1)
	dn=seqcsv(csv)
	for sr1_1 in srs1:
		sr1_2 = sr1_1.replace("_R1", "_R2")
		sr1_3 = sr1_1.replace("_R1", "_R3")
		if os.path.exists(rawdir1+"/"+sr1_2) and not os.path.exists(rawdir1+"/"+sr1_3)：
			if sr1_1.split('_')[0] in dn.keys() :
			#print('%s = %s' % (sr1_1.split('_')[2], sr2_1.split('_')[2]))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_1, rawdir1, dn[sr1_1.split('_')[0]], '_'.join(sr1_1.split('_')[1:])))
				print('%s moves to %s_%s' % (sr1_1, dn[sr1_1.split('_')[0]], '_'.join(sr1_1.split('_')[1:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_2, rawdir1, dn[sr1_2.split('_')[0]], '_'.join(sr1_2.split('_')[1:])))
				print('%s moves to %s_%s' % (sr1_2, dn[sr1_2.split('_')[0]], '_'.join(sr1_2.split('_')[1:])))

			elif sr1_1.split('_')[2]  in dn.keys() :
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_1, rawdir1, dn[sr1_1.split('_')[2]], '_'.join(sr1_1.split('_')[3:])))
				print("%s moves to %s_%s" % (sr1_1, dn[sr1_1.split('_')[2]], '_'.join(sr1_1.split('_')[3:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_2, rawdir1, dn[sr1_2.split('_')[2]], '_'.join(sr1_2.split('_')[3:])))
				print("%s moves to %s_%s" % (sr1_2, dn[sr1_2.split('_')[2]], '_'.join(sr1_2.split('_')[3:])))

			elif sr1_1.split('_')[0] not in dn.keys() or sr1_1.split('_')[2] not in dn.keys():
				print("%s: No need to change the name!!!" % sr1_1)
				print("%s: No need to change the name!!!" % sr1_2)

		if os.path.exists(rawdir1+"/"+sr1_2) and os.path.exists(rawdir1+"/"+sr1_3)：
			if sr1_1.split('_')[0] in dn.keys() :
			#print('%s = %s' % (sr1_1.split('_')[2], sr2_1.split('_')[2]))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_1, rawdir1, dn[sr1_1.split('_')[0]], '_'.join(sr1_1.split('_')[1:])))
				print('%s moves to %s_%s' % (sr1_1, dn[sr1_1.split('_')[0]], '_'.join(sr1_1.split('_')[1:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_2, rawdir1, dn[sr1_2.split('_')[0]], '_'.join(sr1_2.split('_')[1:])))
				print('%s moves to %s_%s' % (sr1_2, dn[sr1_2.split('_')[0]], '_'.join(sr1_2.split('_')[1:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_3, rawdir1, dn[sr1_3.split('_')[0]], '_'.join(sr1_3.split('_')[1:])))
				print('%s moves to %s_%s' % (sr1_3, dn[sr1_3.split('_')[0]], '_'.join(sr1_3.split('_')[1:])))

			elif sr1_1.split('_')[2]  in dn.keys() :
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_1, rawdir1, dn[sr1_1.split('_')[2]], '_'.join(sr1_1.split('_')[3:])))
				print("%s moves to %s_%s" % (sr1_1, dn[sr1_1.split('_')[2]], '_'.join(sr1_1.split('_')[3:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_2, rawdir1, dn[sr1_2.split('_')[2]], '_'.join(sr1_2.split('_')[3:])))
				print("%s moves to %s_%s" % (sr1_2, dn[sr1_2.split('_')[2]], '_'.join(sr1_2.split('_')[3:])))
				os.system('mv %s/%s %s/%s_%s' % (rawdir1, sr1_3, rawdir1, dn[sr1_3.split('_')[2]], '_'.join(sr1_3.split('_')[3:])))
				print("%s moves to %s_%s" % (sr1_3, dn[sr1_3.split('_')[2]], '_'.join(sr1_3.split('_')[3:])))

			elif sr1_1.split('_')[0] not in dn.keys() or sr1_1.split('_')[2] not in dn.keys():
				print("%s: No need to change the name!!!" % sr1_1)
				print("%s: No need to change the name!!!" % sr1_2)
				print("%s: No need to change the name!!!" % sr1_3)

def main():
	rawdir1=sys.argv[1]
	csv=sys.argv[2]
	rename(rawdir1, csv)

if __name__ == '__main__':
	main()
