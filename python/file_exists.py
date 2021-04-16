#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import time

def file_exists(file, sh):
	while True:
		if os.path.exists(file):
			print('Program Starts at: %s' % time.ctime())
			os.system('sh %s' % sh)
		else:
			time.sleep(300)
			continue
		return False

def main():
	file=sys.argv[1]
	sh=sys.argv[2]
	file_exists(file,sh)

if __name__ == '__main__':
	main()