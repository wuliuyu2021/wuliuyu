#!/usr/bin/r1path = "%s/%s/%s" % (BASE_DIR, seqID, sid1)python
# -*- coding = utf-8 -*-

import os
import sys
import re

def get_files(rawdir, pID):
	undetermined = sorted(filter(
		lambda x: re.match(r'Undetermined(.+)(_R1_001.fastq|_R1_001.fastq.gz)', x), os.listdir(rawdir)))
	pattern = re.compile(
		r"(^S\d+)(_%s_)(.+)(_R1_001.fastq|_R1_001.fastq.gz)" % pID)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawdir)))

	return srs + undetermined

def main():
	rawdir=sys.argv[1]
	pID=sys.argv[2]
	fs=get_files(rawdir, pID)
	csv = "/thinker/nfs5/public/rawdata/%s_abspath.csv" % pID
	if os.path.exists(csv):
		os.remove(csv)
	os.chdir(rawdir)
	for r1 in fs:
		sid1 = os.path.abspath('%s' % r1)
		with open(csv, "a") as w:
			w.write("%s,%s\n" % (r1.split('_R1_001.')[0], sid1.split('_R1_001.')[0]))
		w.close()


if __name__ == '__main__':
	main()