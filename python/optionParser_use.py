#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from optparse import OptionParser


def parse_cmd():
	usage="xx xx xx"
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-a","--aaa",dest="aaa",default=None,help="input aaa")
	parser.add_option("-b","--bbb",dest="bbb",default=None,help="input bbb")
	parser.add_option("-c","--ccc",dest="ccc",default=None,help="input ccc")
	parser.add_option("-d","--ddd",dest="ddd",default=None,help="input ddd")
	
	return parser.parse_args()

def get_files(options):
	if options.aaa:
		print(options.aaa+'\n')
	if options.bbb:
		print(options.bbb+'\n')
	if options.ccc:
		print(options.ccc+'\n')
	if options.ddd:
		print(options.ddd+'\n')



def main():
	(options, args) = parse_cmd()
	get_files(options)
	

if __name__ == "__main__":
	main()
