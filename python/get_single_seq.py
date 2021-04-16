#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, re 
from Bio import SeqIO

indir = sys.argv[1]

def get_files(indir):
	pattern = re.compile(r"(^S\d+)(.+)(_001.fasta)$")
	fs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	print(os.path.basename(indir))
	return fs

def duplication_counter():
	container = {}
	
	tests = get_files(indir)
	
	for test in tests:

		fp = open(test,"r")
		for record in SeqIO.parse(fp,'fasta'):
			if str(record.seq) not in container:
				record.count = 0
				container[str(record.seq)] = record
    			container[str(record.seq)].count += 1
    		
		fp.close()

		flp = open("duplicated_%s" % test,'w')
		for seq in container.itervalues():
			seq.id = '%s;counter=%s;'%(seq.id,seq.count)
			seq.description = ''
			flp.write(seq.format('fasta'))
		flp.close()

if __name__ == '__main__':
	duplication_counter()
