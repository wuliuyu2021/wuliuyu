#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, re

Head = ("Lane,Sample_ID,Sample_Name,Sample_Plate,Sample_Well,I7_Index_ID,index,Sample_Project,Description\n")

outpath = sys.argv[1]
double_index = sys.argv[2]

def check_str(string):
	if not re.match("^[a-zA-Z0-9][a-zA-Z0-9-]+$", string):
		print('Warning: %s!!! check it!!!\n' % (string, string)) * 3

def table_split(dirname):
	infos = []
	table = os.path.join(dirname, 'sequence_%s.csv' % os.path.basename(dirname))
	for line in open(table):
		clientID = line.strip().split(',')[2]
		check_str(clientID)
		pID = line.strip().split(',')[23]
		check_str(pID)
		ordID = line.strip().split(',')[0]
		sampleID = '_'.join([ordID, pID, clientID])
		indexID = line.strip().split(',')[8]
		index_seq = line.strip().split(',')[9]
		estimated_yield = line.strip().split(',')[13]
		lane = int(line.strip().split(',')[7])
		infos.append((sampleID, indexID, index_seq, estimated_yield, lane))
	return infos

def outwriter(path):
	SampleSheet = os.path.join(path, 'SampleSheet.csv')
	estimated_yield =  os.path.join(path, 'estimated_yield.csv')
	with open(SampleSheet, 'w') as f:
		f.write(Head)
	return SampleSheet, estimated_yield

def SampleSheet_maker(outpath, double_index="F"):
	infos = table_split(outpath)
	out = outwriter(outpath)
	for info in infos:
		(sampleID, indexID, index_seq, data, lane) = (info[0], info[1], info[2], info[3], info[4])
		sample = '%s,%s,%s,,,%s,%s,,\n' % (lane, sampleID, sampleID, indexID, index_seq)
		estimated_yield = sampleID + "," + data + "\n"
		if double_index == 'F':
			with open(out[0], 'a') as f:
				f.write(sample)

			with open(out[1], 'a') as f:
				f.write(estimated_yield)

		else:
			sys.exit(1)
			
	return sample
			

if __name__ == '__main__':
	SampleSheet_maker(sys.argv[1], sys.argv[2])


