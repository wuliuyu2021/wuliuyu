#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

def get_dir(nbdir):
	pattern = re.compile(r"(^S\d+)(.+)(_R1_001)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(nbdir)))
	return srs

def cp_to_publicdir(pudir, nbdir):
	srs = get_dir(nbdir)
	if not os.path.exists(pudir):
		os.makedirs(pudir)
	for sr in srs:
		os.system("mkdir -p %s/%s" % (pudir, sr))
		os.system("cp %s/*.txt %s/*.plot %s/*.png %s/*.bed %s/%s "
			% (sr, sr, sr, sr, pudir, sr))

def main():
	nbdir = sys.argv[1]
	pudir = sys.argv[2]
	cp_to_publicdir(pudir, nbdir)


if __name__ == '__main__':
	main()