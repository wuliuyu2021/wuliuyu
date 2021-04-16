#!/usr/bin/python
# -*- coding = utf-8 -*-


import os, sys, re

dn={"A":"T", "T":"A", "C":"G", "G":"C"}

outdir=sys.argv[1]
csv=sys.argv[2]


new_csv=os.path.join(outdir, 'new_%s' % os.path.basename(csv))

f=open(new_csv, 'w')
for line in open(csv):
	lst=line.strip().split(',')[0]
	for x in lst:
		if x not in dn.keys():
			print('Warning!!! No appropriate bases: %s in index: %s, Please check!!!\n' % (x, lst))
			sys.exit(-1)
	lrt=lst[::-1]
	if len(lrt) == int(10):
		l10='%s,%s%s%s%s%s%s%s%s%s%s' % (lst, dn[lrt[0]], dn[lrt[1]], dn[lrt[2]],dn[lrt[3]],dn[lrt[4]],dn[lrt[5]],dn[lrt[6]],dn[lrt[7]],dn[lrt[8]],dn[lrt[9]])
		f.write(l10+'\n')
	elif len(lrt) == int(8):
		l8='%s,%s%s%s%s%s%s%s%s' % (lst, dn[lrt[0]], dn[lrt[1]], dn[lrt[2]],dn[lrt[3]],dn[lrt[4]],dn[lrt[5]],dn[lrt[6]],dn[lrt[7]])
		f.write(l8+'\n')
	elif len(lrt) == int(6):
		l6='%s,%s%s%s%s%s%s' % (lst, dn[lrt[0]], dn[lrt[1]], dn[lrt[2]],dn[lrt[3]],dn[lrt[4]],dn[lrt[5]])
		f.write(l6+'\n')
	elif lst == "":
		f.write(""+"\n")
	else:
		print('Warning!!! No appropriate index types: %s[%d]\n' %(lst, len(lst)))
		sys.exit(-1)
f.close()