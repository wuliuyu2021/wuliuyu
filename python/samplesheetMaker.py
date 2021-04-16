#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import re


HEADER = (
	"[Header],,,,,,,,\n"
	"IEMFileVersion,4,,,,,,,\n"
	"Investigator Name,,,,,,,,\n"
	"Experiment Name,,,,,,,,\n"
	"Date,,,,,,,,\n"
	"Workflow,GenerateFASTQ,,,,,,,\n"
	"Application,HiSeq FASTQ Only,,,,,,,\n"
	"Assay,TruSeq HT,,,,,,,\n"
	"Description,,,,,,,,\n"
	"Chemistry,Amplicon,,,,,,,\n"
	",,,,,,,,\n"
	"[Reads],,,,,,,,\n"
	"151,,,,,,,,\n"
	"151,,,,,,,,\n"
	",,,,,,,,\n"
	"[Settings],,,,,,,,\n"
	"ReverseComplement,0,,,,,,,\n"
	"Adapter,,,,,,,,\n"
	"AdapterRead2,,,,,,,,\n"
	",,,,,,,,\n"
	"[Data],,,,,,,,\n"
	"Lane,Sample_ID,Sample_Name,Sample_Plate,Sample_Well,I7_Index_ID,index,Sample_Project,Description\n")


def index_dict_maker():
	Indexs_csv = "/thinker/nfs5/public/wuliuyu/wuliuyu/csv_file/all_Indexs.csv"
	with open(Indexs_csv, "r") as f:
		indexs = [line.strip().split(",") for line in f]#按照行列出元素并且以逗号分隔开
		ks, vs = [], []
		for index in indexs:
			ks.append(index[0])
			vs.append(index[1])
		d = dict(zip(ks, vs))
		return d


def check_str(string):
	if not re.match("^[a-zA-Z0-9][a-zA-Z0-9-]+$", string):#^为：找到字符串开头的位置，字母范围在a-z之间，外加0-9的数字
		print ("Warning: %s!!! check it!!!\n" % string) * 3
		# sys.exit(1)


def table_split(dirname):
	infos = []
	table = os.path.join(dirname, "sequence_%s.csv" % os.path.basename(dirname))
	for line in open(table):
		libID = line.strip().split(",")[1]
		check_str(libID)
		sampleID = line.strip().split(",")[3]
		check_str(sampleID)
		pID = line.strip().split(",")[7]
		check_str(pID)
		numID = line.strip().split(",")[0]
		samsheetID = "_".join([ordID, pID, libID])
		indexID = line.strip().split(",")[12]
		index_seq = line.strip().split(",")[13]
		#estimated_yield = line.strip().split(",")[13]
		lane = int(line.strip().split(",")[11])
		infos.append((numID, indexID, index_seq, lane, pID))
	return infos


def outwriter(path):
	SampleSheet = os.path.join(path, "SampleSheet.csv")
	for f in [SampleSheet, fqsamplesheet, estimated_yield]:
		if os.path.exists(f):
			os.remove(f)
	with open(SampleSheet, "w") as f:
		f.write(HEADER)
	return SampleSheet, fqsamplesheet, estimated_yield


def check_index_len_and_duplication(**lanes_indexs):
	d = lanes_indexs
	for lane in d.keys():
		indexs = d[lane]
		flag = len(set(map(len, indexs)))
		if flag != 1:
			print "ERROR: all indexs must have same size! Please check Lane%s!\n" % (ord(lane) - 65)
			sys.exit(1)
		if len(indexs) != len(set(indexs)):
			print "ERROR: duplicated index! Please check Lane%s!\n" % (ord(lane) - 65)
			sys.exit(1)


def samplesheet_maker(outpath, double_index="F"):
	d = index_dict_maker()
	infos = table_split(outpath)
	out = outwriter(outpath)
	lane_s_e = []
	lanes_indexs = {}
	for info in infos:
		# skip 2 lines
		(sampleID, indexID, index_seq, data, lane) = (info[0], info[1], info[2], info[3], info[4])
		try:
			if indexID in d.keys():
				index = d[indexID]
			else:
				index = index_seq  # make a false index in order to prevent interrupt from no index!
				sys.exit(1)
		except:
			print "Warning: Cannot match the index sequence, please check the index ID (%s)!!!\n" % indexID

		if lane != 0:
			lane_id = lane
		else:
			lane_id = ""
		sample = "%s,%s,%s,,,%s,%s,,\n" % (lane_id, sampleID, sampleID, indexID, index)
		lane_s_e.append(lane_id)

		lane_chr = chr(int(lane) + 65)
		if lane_chr not in lanes_indexs.keys():
			lanes_indexs[lane_chr] = [index]
		else:
			if index in lanes_indexs[lane_chr]:
				print "ERROR: duplicated index! Please check Lane%s:%s!\n" % (lane, index)
				sys.exit(1)
			lanes_indexs[lane_chr].append(index)
		check_index_len_and_duplication(**lanes_indexs)

		if double_index == "F":
			with open(out[0], "a") as f:
				f.write(sample)
		else:
			fastqsplit_Index = sampleID + "," + index + "\n"
			with open(out[1], "a") as f:
				f.write(fastqsplit_Index)
		estimated_yield = sampleID + "," + data + "\n"
		with open(out[2], "a") as f:
			f.write(estimated_yield)
	return min(lane_s_e), max(lane_s_e)


def main():
	outpath = sys.argv[1]
	double_index = sys.argv[2]
	samplesheet_maker(outpath, double_index)


if __name__ == "__main__":
	main()
