#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re

def get_files(indir, outdir):

	undetermined = sorted(filter(
		lambda x: re.match(r'Undetermined(.+)(_R1_001.fastq|_R1_001.fastq.gz)', x), os.listdir(indir)))

	pattern = re.compile(r"(.+)(_R1_001.fastq|_R1_001.fastq.gz)")

	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))

	return undetermined + srs


def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]

	fs = get_files(indir, outdir)
	print fs

	csv = os.path.join(outdir, "%s_abspath.csv" % os.path.basename(indir))
	if os.path.exists(csv):
		os.remove(csv)

	for r1 in fs:
		sid = r1.split("_R1_001.")[0]
		r1path = "%s/%s" % (indir, r1)
		r2 = r1.replace("_R1_001.", "_R2_001.")
		r2path = "%s/%s" % (indir, r2)

		with open(csv, "a") as w:
			w.write("%s,%s,,%s,,%s\n%s,%s,,%s,,%s\n" % (sid, sid, r1, r1path, sid, sid, r2, r2path))


if __name__ == "__main__":
	main()
