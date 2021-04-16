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

	csv = os.path.join(outdir, "%s_rna_abspath.csv" % os.path.basename(indir))
	abs_csv = os.path.join(outdir, "data.csv")
	abs_csv_r1 = os.path.join(outdir, "data_r1.csv")
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
		with open(abs_csv, "a") as f:
			f.write(",,,%s,,%s/%s\n,,,%s,,%s/%s\n" % (r1, indir, r1, r2, indir, r2))
		f.close()
		with open(abs_csv_r1, "a") as r:
			r.write(",,,%s,,%s/%s\n" % (r1, indir, r1))
		r.close()

if __name__ == "__main__":
	main()
