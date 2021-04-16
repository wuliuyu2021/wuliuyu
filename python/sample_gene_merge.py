#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
import pandas as pd
import numpy as np


def sample_info(indir):
	snp_g=[]
	indel_g=[]
	si1,si2={},{}
	pattern1 = re.compile(r"(.+)(snp.anno.vcf)(.+)(multianno.xls)$")
	pattern2 = re.compile(r"(.+)(indel.anno.vcf)(.+)(multianno.xls)$")
	srs1 = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(indir)))
	srs2 = sorted(filter(lambda x: re.match(pattern2, x), os.listdir(indir)))
	for s1 in srs1:
		with open("%s/%s" % (indir, s1), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				info="%s_%s_%s_%s_%s" % (lst[0],lst[1],lst[2],lst[3],lst[4])
				snp_g.append(info)
				si1[info]=lst[6]
	for s2 in srs2:
		with open("%s/%s" % (indir, s2), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				info="%s_%s_%s_%s_%s" % (lst[0],lst[1],lst[2],lst[3],lst[4])
				indel_g.append(info)
				si2[info]=lst[6]
	#print(si1)
	#print(sorted(set(indel_g)))

	return sorted(set(snp_g)),sorted(set(indel_g)),si1,si2

def mer_csv_snp(indir):
	ls1,ls2,ls3,ls4=[],[],[],[]
	snp=sample_info(indir)[0]
	
	pattern1 = re.compile(r"(.+)(snp.anno.vcf)(.+)(multianno.xls)$")
	
	srs1 = sorted(filter(lambda x: re.match(pattern1, x), os.listdir(indir)))
	

	with open("%s/%s" % (indir, srs1[0]), "r") as f:
		
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls1.append(info)
	with open("%s/%s" % (indir, srs1[1]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls2.append(info)
	with open("%s/%s" % (indir, srs1[2]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls3.append(info)
	with open("%s/%s" % (indir, srs1[3]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls4.append(info)
	
	header1="info"+"\t"+os.path.basename(srs1[0]).split('.anno.vcf')[0]
	header2="info"+"\t"+os.path.basename(srs1[1]).split('.anno.vcf')[0]
	header3="info"+"\t"+os.path.basename(srs1[2]).split('.anno.vcf')[0]
	header4="info"+"\t"+os.path.basename(srs1[3]).split('.anno.vcf')[0]
	csv1=os.path.join(indir, "%s.snp_tmp.xls" % (os.path.basename(srs1[0]).split('.anno.vcf')[0]))
	csv2=os.path.join(indir, "%s.snp_tmp.xls" % (os.path.basename(srs1[1]).split('.anno.vcf')[0]))
	csv3=os.path.join(indir, "%s.snp_tmp.xls" % (os.path.basename(srs1[2]).split('.anno.vcf')[0]))
	csv4=os.path.join(indir, "%s.snp_tmp.xls" % (os.path.basename(srs1[3]).split('.anno.vcf')[0]))
	so1=open(csv1, "w")
	so1.write(header1+"\n")
	so2=open(csv2, "w")
	so2.write(header2+"\n")
	so3=open(csv3, "w")
	so3.write(header3+"\n")
	so4=open(csv4, "w")
	so4.write(header4+"\n")

	for info in snp:
		if info in sorted(set(ls1)):
			so1.write(info+"\t"+"snp"+"\n")
		else:
			so1.write(info+"\t"+"."+"\n")
	so1.close()
	for info in snp:
		if info in sorted(set(ls2)):
			so2.write(info+"\t"+"snp"+"\n")
		else:
			so2.write(info+"\t"+"."+"\n")
	so2.close()
	for info in snp:
		if info in sorted(set(ls3)):
			so3.write(info+"\t"+"snp"+"\n")
		else:
			so3.write(info+"\t"+"."+"\n")
	so3.close()
	for info in snp:
		if info in sorted(set(ls4)):
			so4.write(info+"\t"+"snp"+"\n")
		else:
			so4.write(info+"\t"+"."+"\n")
	so4.close()

def mer_csv_indel(indir):
	ls1,ls2,ls3,ls4=[],[],[],[]
	indel=sample_info(indir)[1]
	pattern2 = re.compile(r"(.+)(indel.anno.vcf)(.+)(multianno.xls)$")
	srs2 = sorted(filter(lambda x: re.match(pattern2, x), os.listdir(indir)))
	with open("%s/%s" % (indir, srs2[0]), "r") as f:
		
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls1.append(info)
	with open("%s/%s" % (indir, srs2[1]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls2.append(info)
	with open("%s/%s" % (indir, srs2[2]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls3.append(info)
	with open("%s/%s" % (indir, srs2[3]), "r") as f:
		lines = f.readlines()[1:]
		for line in lines:
			lst = line.strip().split("\t")
			info=lst[0]+"_"+lst[1]+"_"+lst[2]+"_"+lst[3]+"_"+lst[4]
			ls4.append(info)
	
	
	header1="info"+"\t"+os.path.basename(srs2[0]).split('.anno.vcf')[0]
	header2="info"+"\t"+os.path.basename(srs2[1]).split('.anno.vcf')[0]
	header3="info"+"\t"+os.path.basename(srs2[2]).split('.anno.vcf')[0]
	header4="info"+"\t"+os.path.basename(srs2[3]).split('.anno.vcf')[0]
	csv1=os.path.join(indir, "%s.indel_tmp.xls" % (os.path.basename(srs2[0]).split('.anno.vcf')[0]))
	csv2=os.path.join(indir, "%s.indel_tmp.xls" % (os.path.basename(srs2[1]).split('.anno.vcf')[0]))
	csv3=os.path.join(indir, "%s.indel_tmp.xls" % (os.path.basename(srs2[2]).split('.anno.vcf')[0]))
	csv4=os.path.join(indir, "%s.indel_tmp.xls" % (os.path.basename(srs2[3]).split('.anno.vcf')[0]))
	so1=open(csv1, "w")
	so1.write(header1+"\n")
	so2=open(csv2, "w")
	so2.write(header2+"\n")
	so3=open(csv3, "w")
	so3.write(header3+"\n")
	so4=open(csv4, "w")
	so4.write(header4+"\n")

	for info in indel:
		if info in sorted(set(ls1)):
			so1.write(info+"\t"+"indel"+"\n")
		else:
			so1.write(info+"\t"+"."+"\n")
	so1.close()
	for info in indel:
		if info in sorted(set(ls2)):
			so2.write(info+"\t"+"indel"+"\n")
		else:
			so2.write(info+"\t"+"."+"\n")
	so2.close()
	for info in indel:
		if info in sorted(set(ls3)):
			so3.write(info+"\t"+"indel"+"\n")
		else:
			so3.write(info+"\t"+"."+"\n")
	so3.close()
	for info in indel:
		if info in sorted(set(ls4)):
			so4.write(info+"\t"+"indel"+"\n")
		else:
			so4.write(info+"\t"+"."+"\n")
	so4.close()
	
def merge_snp_maker(indir,outdir):
	s1=sample_info(indir)[2]
	head1=""
	dfs = []
	df_count = 0
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	genetable=os.path.join(outdir,'merge_snp.xls')
	#if os.path.exists(genetable):
	#	os.remove(genetable)
	pattern=re.compile(r"(.+)(snp_tmp.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	for tab in tabs:
		df= pd.read_csv(indir+"/"+tab, sep = "\t",encoding='utf-8')
		dfs.append(df)
	#genetable_open=open(genetable, "w")
	for dfg in dfs:
		df_count += 1
		if df_count == 1:
			df = dfg
		else:
			df = pd.merge(df,dfg,how='inner',on="info")
	#genetable_open.write(merge_df)
	#genetable_open.close()
		to_drop = [x for x in df if '_y' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '_x_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '1_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		#to_drop = [x for x in df if '2' in x]
		#df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '2_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '3_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '4_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '5_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '6_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		df.to_csv(genetable,index=None,sep = '\t',encoding='utf-8')
	with open("%s/merge_snp.xls" % outdir, "r") as f:
		head1=f.readlines()[0]
	with open("%s/merge_snp.xls" % outdir, "r") as f:	
		lines = f.readlines()[1:]
		csv1=os.path.join(outdir, "merge.snp.xls")
		csv1open=open(csv1, "w")
		csv1open.write(head1.strip().split("\t")[0]+"\t"+head1.strip().split("\t")[1]+"\t"+head1.strip().split("\t")[2]+"\t"
			+head1.strip().split("\t")[3]+"\t"+head1.strip().split("\t")[4]+"\t"+"ref_gene"+"\n")

		for line in lines:
			lst = line.strip().split("\t")
			
			if lst[0] in s1.keys():
				#print(lst[0],lst[1],lst[2],lst[3],lst[4])
				csv1open.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (lst[0],lst[1],lst[2],lst[3],lst[4],s1[lst[0]]))
				#csv1open.write("%s\t%s\n" % (lst[0],s1[lst[0]]))
		csv1open.close()

def merge_indel_maker(indir,outdir):
	s1=sample_info(indir)[3]
	head1=""
	dfs = []
	df_count = 0
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	genetable=os.path.join(outdir,'merge_indel.xls')
	#if os.path.exists(genetable):
	#	os.remove(genetable)
	pattern=re.compile(r"(.+)(indel_tmp.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	for tab in tabs:
		df= pd.read_csv(indir+"/"+tab, sep = "\t",encoding='utf-8')
		dfs.append(df)
	#genetable_open=open(genetable, "w")
	for dfg in dfs:
		df_count += 1
		if df_count == 1:
			df = dfg
		else:
			df = pd.merge(df,dfg,how='inner',on="info")
	#genetable_open.write(merge_df)
	#genetable_open.close()
		to_drop = [x for x in df if '_y' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '_x_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '1_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		#to_drop = [x for x in df if '2' in x]
		#df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '2_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '3_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '4_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '5_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		to_drop = [x for x in df if '6_x' in x]
		df.drop(to_drop, axis=1, inplace=True)
		df.to_csv(genetable,index=None,sep = '\t',encoding='utf-8')
	with open("%s/merge_indel.xls" % outdir, "r") as f:
		head1=f.readlines()[0]
	with open("%s/merge_indel.xls" % outdir, "r") as f:	
		lines = f.readlines()[1:]
		csv1=os.path.join(outdir, "merge.indel.xls")
		csv1open=open(csv1, "w")
		csv1open.write(head1.strip().split("\t")[0]+"\t"+head1.strip().split("\t")[1]+"\t"+head1.strip().split("\t")[2]+"\t"
			+head1.strip().split("\t")[3]+"\t"+head1.strip().split("\t")[4]+"\t"+"ref_gene"+"\n")

		for line in lines:
			lst = line.strip().split("\t")
			
			if lst[0] in s1.keys():
				#print(lst[0],lst[1],lst[2],lst[3],lst[4])
				csv1open.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (lst[0],lst[1],lst[2],lst[3],lst[4],s1[lst[0]]))
				#csv1open.write("%s\t%s\n" % (lst[0],s1[lst[0]]))
		csv1open.close()

def main():
	
	indir=sys.argv[1]
	outdir=sys.argv[2]
	sample_info(indir)
	mer_csv_snp(indir)
	mer_csv_indel(indir)
	merge_snp_maker(indir,outdir)
	merge_indel_maker(indir,outdir)
	

if __name__ == '__main__':
	main()