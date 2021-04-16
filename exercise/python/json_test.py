#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import sys

class Json:
	def __init__(self, json_f):
		data=json.load(json_f)
		self.raw_reads_num = data["summary"]["before_filtering"]["total_reads"]
		self.raw_bases_num = data["summary"]["before_filtering"]["total_bases"]
		self.raw_q20_rate = data["summary"]["before_filtering"]["q20_rate"]
		self.raw_q30_rate = data["summary"]["before_filtering"]["q30_rate"]
		self.raw_gc_content = data["summary"]["before_filtering"]["gc_content"]

	

if __name__ == '__main__':
	
	file="/thinker/nfs2/longrw/runPipelineInfo/201806/180629_E00603_0135_AHLK53CCXY/fastp_qcout/Undetermined_S0_L008_R1_001.json"
	data_json=open(file, "r")
	fastp = Json(data_json)
	print("raw_num: %s\n" % fastp.raw_bases_num)
	
