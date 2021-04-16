#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import csv



def hgc_info_split():
	dn={}
	for line in open('/thinker/nfs5/public/wuliuyu/wuliuyu/csv_file/HGC-info.csv'):
		lst = line.strip().split(',')
		dn[lst[1]] = lst[4]
	return dn

def csv_maker(seqcsv, runid, outdir):
	dn=hgc_info_split()
	if runid == '_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:]):
		csv = os.path.join(outdir, '%s.csv' % os.path.basename(seqcsv).split('.csv')[0])
		csv_read=open(csv, 'w')
		for line in open(seqcsv, 'r'):
			one_line = line.strip().split(',')
			if one_line[6] in dn.keys() and dn[one_line[6]] != '':
				client = ('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (one_line[0],
					one_line[1],one_line[2],one_line[3],one_line[4],one_line[5],one_line[6],dn[one_line[6]],one_line[8],one_line[9],one_line[10],one_line[11],
					one_line[12],one_line[13],one_line[14],one_line[15],one_line[16],one_line[17],one_line[18],one_line[19],one_line[20],one_line[21],
					one_line[22],one_line[23],one_line[24],one_line[25],one_line[26],one_line[27],one_line[28],one_line[29],one_line[30]))
				csv_read.write(client)
				print('%s %s %s' % (one_line[0], one_line[6], dn[one_line[6]]))
			elif one_line[6] not in dn.keys():
				client = ('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (one_line[0],
					one_line[1],one_line[2],one_line[3],one_line[4],one_line[5],one_line[6],one_line[7],one_line[8],one_line[9],one_line[10],one_line[11],
					one_line[12],one_line[13],one_line[14],one_line[15],one_line[16],one_line[17],one_line[18],one_line[19],one_line[20],one_line[21],
					one_line[22],one_line[23],one_line[24],one_line[25],one_line[26],one_line[27],one_line[28],one_line[29],one_line[30]))
				csv_read.write(client)
				print('%s %s None' % (one_line[0], one_line[6]))
				print('There is new client: %s, please add!!!\n' % one_line[6])
			elif one_line[6] in dn.keys() and dn[one_line[6]] == '':
				print('Warning, No pid to client, Please check HGC-info.csv!!!\n' * 3)
				sys.exit(1)
		csv_read.close()
	else:
		print('Warning, Wrong runid, Please check!!!\n' * 3)
		sys.exit(1)

def main():
	runid=sys.argv[1]
	seqcsv=sys.argv[2]
	outdir=sys.argv[3]
	csv_maker(seqcsv, runid, outdir)

if __name__ == '__main__':
	main()