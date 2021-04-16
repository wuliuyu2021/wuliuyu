#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import gzip

index_list=['GCAA']
gz1=gzip.open(sys.argv[1],'rb')
gz2=gzip.open(sys.argv[2],'rb')
out1=gzip.open(sys.argv[3],'wb', compresslevel=4)
out2=gzip.open(sys.argv[4],'wb', compresslevel=4)
for line in gz1:
	if line.startswith('@E00') and line.split(':')[-1][0:4] in index_list:
		out1.write('%s:%s\n' % (":".join(line.strip().split(':')[0:9]), line.strip().split(':')[-1]))
	if not line.startswith('@E00'):
		out1.write(line)
for line in gz2:
	if line.startswith('@E00') and line.split(':')[-1][0:4] in index_list:
		out2.write('%s:%s\n' % (":".join(line.strip().split(':')[0:9]), line.strip().split(':')[-1]))
	if not line.startswith('@E00'):
		out2.write(line)