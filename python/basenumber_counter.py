#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from os.path import getsize

seqid=sys.argv[1]

BASE_DIR = "/thinker/dstore/rawfq"

csv=open('size.csv', 'a')

rawfqdir=os.path.join(BASE_DIR, seqid)
pattern = re.compile(r"(^S\d+)(.+)(_R1_001.fastq|_R1_001.fastq.gz)")
#undetermined = filter(lambda x: re.match(r'Undetermined(.+)R1(.+)', x), os.listdir(rawfqdir))
srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(rawfqdir)))
#print '%s' % os.path.abspath(srs)
#for root, dirs, files in os.walk(rawfqdir):
for sr1 in srs:
	print sr1
	sr2 = sr1.replace('_R1_001','_R2_001')
	size1 = os.path.getsize(os.path.join(os.path.basename(rawfqdir), sr1))

	size2 = os.path.getsize(os.path.join(os.path.basename(rawfqdir), sr2))
	
	csv.write('%s,%.3f\n' % ('_'.join(sr1.split('_')[0:5]), ((size1+size2)/1024/1024)))
csv.close()