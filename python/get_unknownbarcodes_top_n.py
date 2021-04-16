#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json


def get_dict(json_f):
	with open(json_f, "r") as f:
		data = json.load(f)
		info = []
		for lane in data["UnknownBarcodes"]:
			lane_id = lane["Lane"]
			indexs = lane["Barcodes"]
			info.append((lane_id, indexs))

	return info


def sort_d_value(out, d, lane_id, untop_num):
	num = 1
	vs = []
	for v in d.values():
		vs.append(int(v))
	for v in reversed(sorted(set(vs))):
		if num <= int(untop_num):  # stat top 20 Barcodes
			for k in d.keys():
				if d[k] == v:
					count = v
					index = k
					outcsv(out, lane_id, count, index)
					num += 1


def outcsv(out, lane_id, count, index):
	with open(out, "a") as f:
		f.write("%s,%s,%s\n" % (lane_id, count, index))


def outcsv_head(out):
	with open(out, "a") as f:
		f.write("Lane,Count,Index\n")


def stat_unknownbarcodes(json_f, out, untop_num):
	index_ds = get_dict(json_f)
	if os.path.exists(out):
		os.remove(out)
	outcsv_head(out)
	for d in index_ds:
		lane_id = d[0]
		sort_d_value(out, d[1], lane_id, untop_num)


def main():
	json_f = sys.argv[1]
	outdir = sys.argv[2]
	untop_num = sys.argv[3]
	out = os.path.join(outdir,"%s_%s_untop%s.csv" % (os.path.basename(outdir),os.path.basename(json_f).split(".json")[0].split("Stats_")[-1],untop_num))
	stat_unknownbarcodes(json_f, out, untop_num)


if __name__ == "__main__":
	main()
