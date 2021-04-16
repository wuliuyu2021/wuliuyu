#!/usr/bin python
# -*- coding: utf-8 -*-

import sys
import re

class Seqcsv(object):

	def __init__(self, csv_line):
		self.ordID = csv_line[0]
		self.libID = csv_line[1]
		self.clientID = csv_line[2]
		self.sample_num = csv_line[3]
		self.whereFromID = csv_line[6]
		self.contractID = csv_line[5]
		self.sampleType = csv_line[8]
		self.laneID = csv_line[11]
		self.indexID = csv_line[12]
		self.indexSeq = csv_line[13]
		self.index2ID = csv_line[14]
		self.index2Seq = csv_line[15]
		self.probe = csv_line[18]
		self.estimateProduct = csv_line[22]
		self.readType = csv_line[26]
		self.poolID = csv_line[24]
		self.projectID = csv_line[7]
		self.libtype = csv_line[16]
		self.project_leader = csv_line[30]

if __name__ == '__main__':
	seqcsv = sys.argv[1]