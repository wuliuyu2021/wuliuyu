#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re
import sys


def usbdir2_find(usbdir2):
	lst1=[]
	for root,ds,fs in os.walk('%s/Rawdata' % usbdir2):
		ds.sort()
		for d in ds:
			lst1.append(d)
	return lst1

def usbdir1_find_move_to_usbdir2(usbdir1, usbdir2):
	lst=usbdir2_find(usbdir2)
	for root,ds,fs in os.walk('%s/Rawdata' % usbdir1):
		ds.sort()
		for d in ds:
			if d in lst:
				os.system('mv %s/Rawdata/%s/*.gz %s/Rawdata/%s' % (usbdir1, d, usbdir2, d))
				print('%s/Rawdata/%s/*.gz moved to %s/Rawdata/%s' % (usbdir1, d, usbdir2, d))
				os.system('rm -rf %s/Rawdata/%s' % (usbdir1, d))
				print("rm %s/Rawdata/%s" % (usbdir1, d))
			elif d not in lst:
				os.system('mv %s/Rawdata/%s %s/Rawdata' % (usbdir1, d, usbdir2))
				print('%s/Rawdata/%s moved to %s/Rawdata' % (usbdir1, d, usbdir2))
				

	os.system('cat %s/md5 >> %s/md5_new' % (usbdir1, usbdir2))
	os.system('cat %s/md5.check >> %s/md5_new.check' % (usbdir1, usbdir2))

def main():
	usbdir1=sys.argv[1]
	usbdir2=sys.argv[2]
	usbdir1_find_move_to_usbdir2(usbdir1, usbdir2)

if __name__ == '__main__':
	main()