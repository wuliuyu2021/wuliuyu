#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

def get_files(indir, outdir):

	pattern = re.compile(r"(.+)(_R1_001.fastq|_R1_001.fastq.gz|_R1.fq.gz)")

	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))

	return srs


def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]

	fs = get_files(indir, outdir)
	print fs
	head="实验名称\t数据类型\t实验描述\t样本名称\t分组\t描述\t文件名\tmd5\t保存路径\nRNA\tRNA-Seq\t\t\t\t\t\t\t\n"
	csv = os.path.join(outdir, "%s_rna_abspath.xls" % os.path.basename(indir))
	abs_csv = os.path.join(outdir, "data.xls")
	abs_csv_r1 = os.path.join(outdir, "data_r1.xls")
	abs_csv_open =open(abs_csv, "w")
	abs_csv_r1_open=open(abs_csv_r1, "w")
	abs_csv_open.write(head)
	abs_csv_r1_open.write(head)
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	if os.path.exists(csv):
		os.remove(csv)
	if os.path.exists(abs_csv):
		os.remove(abs_csv)
	if os.path.exists(abs_csv_r1):
		os.remove(abs_csv_r1)

	for r1 in fs:
		r2 = r1.replace("_R1", "_R2")
		sid = r1.split("_R1.")[0]
		r1path = "%s/%s" % (indir, sid)

		with open(csv, "a") as w:
			w.write("%s\n" % r1path)
		w.close()
		abs_csv_open.write("\t\t\t%s\t\t%s/%s\n\t\t\t%s\t\t%s/%s\n" % (r1, indir, r1, r2, indir, r2))
		abs_csv_r1_open.write("\t\t\t%s\t\t%s/%s\n" % (r1, indir, r1))
	abs_csv_open.close()
	abs_csv_r1_open.close()

if __name__ == "__main__":
	main()
