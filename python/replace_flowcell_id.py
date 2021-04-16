#!/usr/bin/python
# -*- coding = utf-8 -*-
#replace_flowcell_id.py

import os
import sys
import gzip

def replace_rawfqinfo(gzfile,output_path,Machine_ID,Run_ID,Flowcell_ID,Lane_ID):
	if not os.path.exists('%s/Replace_dir' % output_path):
		os.mkdir('%s/Replace_dir' % output_path)
	out_gzfile = os.path.join('%s/Replace_dir' % output_path,'%s' % gzfile.split('/')[-1])
	fqoutput=gzip.open(out_gzfile,'wb', compresslevel=4)
	with gzip.open(gzfile, "rb") as fqfile:
		for line in fqfile:
			if line.startswith('@E00'):
				fqoutput.write('%s:%s:%s:%s:%s\n' % (Machine_ID,Run_ID,Flowcell_ID,Lane_ID,':'.join(line.strip().split(':')[4:])))	
			else:
				fqoutput.write(line)

def main():
	gzfile = sys.argv[1]          #/thinker/nfs5/hanjie/test_R1_001.good.fastq.gz
	output_path = sys.argv[2]     #./
	Machine_ID = sys.argv[3]      #@E00602
	Run_ID = sys.argv[4]          #602
	Flowcell_ID = sys.argv[5]     #AB3CDEFXY
	Lane_ID = sys.argv[6]         #1
	replace_rawfqinfo(gzfile,output_path,Machine_ID,Run_ID,Flowcell_ID,Lane_ID)

if __name__ == "__main__":
	main()