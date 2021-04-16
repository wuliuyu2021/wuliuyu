#!/usr/bin/python
# -*- coding = utf-8 -*-


import os, sys, re

d1 = {}
d2 = {}
d3 = {}
d4 = {}
d2i = {}
d3i = {}
d4i = {}
lst1=[]
lst2=[]
lst3=[]

csv1='/thinker/nfs5/public/wuliuyu/index/roche.csv'
csv2='/thinker/nfs5/public/wuliuyu/index/vazyme.csv'
csv3='/thinker/nfs5/public/wuliuyu/index/agilent.csv'
csv4='/thinker/nfs5/public/wuliuyu/index/NEB.csv'

if os.path.exists('/thinker/nfs5/public/wuliuyu/index/6r-v-a-N.csv'):
	os.remove('/thinker/nfs5/public/wuliuyu/index/6r-v-a-N.csv')
if os.path.exists('/thinker/nfs5/public/wuliuyu/index/6v-a-N.csv'):
	os.remove('/thinker/nfs5/public/wuliuyu/index/6v-a-N.csv')
if os.path.exists('/thinker/nfs5/public/wuliuyu/index/6a-N.csv'):
	os.remove('/thinker/nfs5/public/wuliuyu/index/6a-N.csv')

csv5=open('/thinker/nfs5/public/wuliuyu/index/6r-v-a-N.csv', 'a')
csv6=open('/thinker/nfs5/public/wuliuyu/index/6v-a-N.csv', 'a')
csv7=open('/thinker/nfs5/public/wuliuyu/index/6a-N.csv', 'a')

 
for line in open(csv1):
	indexID1=line.strip().split(',')[0]
	indexseq1=line.strip().split(',')[1]
	d1[indexID1]=indexseq1
	lst1.append(indexID1)
#print("%s" % d1)

for line in open(csv2):
	indexID2=line.strip().split(',')[0]
	indexseq2=line.strip().split(',')[1][:6]
	d2[indexID2]=indexseq2
	lst2.append(indexID2)
#print("%s" % d2)

for line in open(csv3):
	indexID3=line.strip().split(',')[0]
	indexseq3=line.strip().split(',')[1][:6]
	d3[indexID3]=indexseq3
	lst3.append(indexID3)
#print("%s" % d3)

for line in open(csv4):
	indexID4=line.strip().split(',')[0]
	indexseq4=line.strip().split(',')[1]
	d4[indexID4]=indexseq4
#print("%s" % d4)

for i in range(len(lst1)):
	if d1.values()[i] in d2.values():
		#print("Warning, roche:%s<->%s are in vazyme.csv" % (d1.keys()[i], d1.values()[i]))
		d2i = {v:k for k,v in d2.items()}
		csv5.write("roche,%s,%s,=,vazyme,%s,%s\n" % 
			(d1.keys()[i], d1.values()[i], d2i[d1.values()[i]], d2[d2i[d1.values()[i]]]))
	elif d1.values()[i] in d3.values():
		#print("Warning, roche:%s<->%s are in agilent.csv" % (d1.keys()[i], d1.values()[i])
		d3i = {v:k for k,v in d3.items()}
		csv5.write("roche,%s,%s,=,agilent,%s,%s\n" % 
			(d1.keys()[i], d1.values()[i], d3i[d1.values()[i]], d3[d3i[d1.values()[i]]]))
	elif d1.values()[i] in d3.values():
		#print("Warning, roche:%s<->%s are in NEB.csv" % (d1.keys()[i], d1.values()[i]))
		d4i = {v:k for k,v in d4.items()}
		csv5.write("roche,%s,%s,=,NEB,%s,%s\n" % 
			(d1.keys()[i], d1.values()[i], d4i[d1.values()[i]], d4[d4i[d1.values()[i]]]))
	else:
		print("Good luck, roche indexseqs have no duplicates to vazyme-agilent-NEB!!!")
csv5.close()


for j in range(len(lst2)):
	if d2.values()[j] in d3.values():
		#print("Warning, vazyme:%s<->%s are in agilent.csv" % (d2.keys()[j], d2.values()[j]))
		d3i = {v:k for k,v in d3.items()}
		csv6.write("vazyme,%s,%s,=,agilent,%s,%s\n" % 
			(d2.keys()[j], d2.values()[j], d3i[d2.values()[j]], d3[d3i[d2.values()[j]]]))
	elif d2.values()[j] in d4.values():
		#print("Warning, vazyme:%s<->%s are in NEB.csv" % (d2.keys()[j], d2.values()[j]))
		d4i = {v:k for k,v in d4.items()}
		csv6.write("vazyme,%s,%s,=,NEB,%s,%s\n" % 
			(d2.keys()[j], d2.values()[j], d4i[d2.values()[j]], d4[d4i[d2.values()[j]]]))
	else:
		print("Good luck, vazyme indexseqs have no duplicates to agilent-NEB!!!")
csv6.close()


for k in range(len(lst3)):
	if d3.values()[k] in d4.values():
		#print("Warning, agilent:%s<->%s are in NEB.csv" % (d3.keys()[k], d3.values()[k]))
		d4i = {v:k for k,v in d4.items()}
		csv7.write("agilent,%s,%s,=,NEB,%s,%s\n" % 
			(d3.keys()[k], d3.values()[k], d4i[d3.values()[k]], d4[d4i[d3.values()[k]]]))
	else:
		print("Good luck, agilent indexseqs have no duplicates to NEB!!!")
csv7.close()