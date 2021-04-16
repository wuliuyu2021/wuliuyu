#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Fastp(object):

	def __init__(self, json_f):
		data = json.load(json_f)
		self.raw_reads_num = data["summary"]["before_filtering"]["total_reads"]
		self.raw_bases_num = data["summary"]["before_filtering"]["total_bases"]
		self.raw_q20_rate = data["summary"]["before_filtering"]["q20_rate"]
		self.raw_q30_rate = data["summary"]["before_filtering"]["q30_rate"]
		self.raw_gc_content = data["summary"]["before_filtering"]["gc_content"]
		self.clean_reads_num = data["summary"]["after_filtering"]["total_reads"]
		self.clean_bases_num = data["summary"]["after_filtering"]["total_bases"]
		self.clean_q20_rate = data["summary"]["after_filtering"]["q20_rate"]
		self.clean_q30_rate = data["summary"]["after_filtering"]["q30_rate"]
		self.clean_gc_content = data["summary"]["after_filtering"]["gc_content"]
		self.command = data["command"]
		try:
			self.dup_rate = data["duplication"]["rate"]
		except:
			self.dup_rate = data["summary"]["duplication"]["rate"]

		self.r1_before_quality = data["read1_before_filtering"]["quality_curves"]
		self.r1_before_mean_quality = data["read1_before_filtering"]["quality_curves"]["mean"]
		self.r1_after_quality = data["read1_after_filtering"]["quality_curves"]
		self.r1_after_mean_quality = data["read1_after_filtering"]["quality_curves"]["mean"]
		self.r2_before_quality = data["read2_before_filtering"]["quality_curves"]
		self.r2_before_mean_quality = data["read2_before_filtering"]["quality_curves"]["mean"]
		self.r2_after_quality = data["read2_after_filtering"]["quality_curves"]
		self.r2_after_mean_quality = data["read2_after_filtering"]["quality_curves"]["mean"]

		self.r1_before_content = data["read1_before_filtering"]["content_curves"]
		self.r1_before_gc_content = data["read1_before_filtering"]["content_curves"]["GC"]
		self.r1_after_content = data["read1_after_filtering"]["content_curves"]
		self.r1_after_gc_content = data["read1_after_filtering"]["content_curves"]["GC"]
		self.r2_before_content = data["read2_before_filtering"]["content_curves"]
		self.r2_before_gc_content = data["read2_before_filtering"]["content_curves"]["GC"]
		self.r2_after_content = data["read2_after_filtering"]["content_curves"]
		self.r2_after_gc_content = data["read2_after_filtering"]["content_curves"]["GC"]

	def percent(self, num):
		return float(num) * 100

	def filter_rate(self, raw, clean):
		return (float(clean) / float(raw)) * 100


if __name__ == "__main__":
	jsonf = sys.argv[1]
	f = open(jsonf, "r")
	fastp = Fastp(f)