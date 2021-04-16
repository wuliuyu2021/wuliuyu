#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re



i=0
	
for line in open(sys.argv[1], "r"):
	lst=line.strip().split("\t")
	ky=int(lst[2])-int(lst[1])
	i=i+int(ky)
print(i)