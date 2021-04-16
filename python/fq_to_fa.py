#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import time
start = time.time()
import gzip
for root,ds,fs in os.walk(sys.argv[1]):
	fs.sort()
	for f in fs:
		if f.endswith('fastq.gz') or f.endswith('fq.gz'):
			with gzip.open('%s/%s' % (sys.argv[1], f),'rt') as fp:
				output_fasta = open("%s/%s.fa"%(sys.argv[2], f.split('.')[0]),'w') 
				i = 0 
				for line in fp:
					i += 1
					if i % 4 == 1: 
						line_new = line[1:]
						output_fasta.write('>'+line_new) 
					elif i % 4 == 2: 
						output_fasta.write(line)
				output_fasta.close()
		if f.endswith('fastq') or f.endswith('fq'):
			with open('%s/%s' % (sys.argv[1], f),'rt') as fp:
				output_fasta = open("%s/%s.fa"%(sys.argv[2], f.split('.')[0]),'w') 
				i = 0 
				for line in fp:
					i += 1
					if i % 4 == 1: 
						line_new = line[1:]
						output_fasta.write('>'+line_new) 
					elif i % 4 == 2: 
						output_fasta.write(line)
				output_fasta.close()
end = time.time()
print("used %s s" % str(end - start))