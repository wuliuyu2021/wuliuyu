#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DATE: 2020-7-10
# AUTHER: Liuyu Wu

import os,re,sys
import numpy as np
import pandas as pd
import argparse

def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to figure out the common and different genes between samples.')
	parser.add_argument('-i','--input',type=str,dest='inputDir', required=True
				, help='The input directory contains all sample files')
	parser.add_argument('-o','--output',type=str,dest='outputDir',required=True
				, help='The output directory contains all result files')
	#parser.add_argument('-r','--skiprows',type=int,dest='skiprows',required=True
	#			,help = 'type the rows to skip at the head of every file')
	#parser.add_argument('-t','--filetype',type=str,dest='fileType',choices =['anno','vcf'],default = 'anno'
	#			, help='The output directory contains all result files')
	args = parser.parse_args()
	print('>>>Get arguments Done\n')	
	return (args)

def fetchFiles(indir,tag):

	DFs = []
	IDs = []
	Names = []
	Count = 0

	if not os.path.isdir(indir):
		print("The input dir is not a dir path!")
		sys.exit(1)

	for dirpath,dirnames,filenames in os.walk(indir):
		for fh in filenames:
			if fh.endswith(tag):
				prefix=fh[:-4]
				filepath = os.path.join(dirpath,fh)
				print("Reading file: ",filepath)
				df= pd.read_csv(filepath,sep = "\t",skiprows=0,encoding='utf-8')
				Count += 1
				if Count == 1:
					Names.extend(df.columns.values.tolist())
				IDs.append(prefix)
				DFs.append(df)
			else:
				continue
	print("\n>>> files number: %s\n" % Count)
	print('\n>>> Reads files and push to dataframes Done.\n')
	print(df)
	return (IDs,DFs,Names)

def Comm_Diff(dfs):
	Merge_cols = ["GeneName","Location"]
	df_count = 0
	for df in dfs:
		df_count += 1
		if df_count == 1:
			comm_df = df
			diff_df = df
		else:
			print("COM",comm_df.iloc[:3,:2])
			print("df",df.iloc[:3,:2])
			comm_df = pd.merge(comm_df,df,how='inner',on=Merge_cols)
			diff_df = diff_df.append(df,sort=False)
		print(">>>DF Count: ",df_count)
	diff_df = diff_df.drop_duplicates(subset=Merge_cols,keep=False)#.reset_index(drop = True)
	comm_df = comm_df.drop_duplicates(subset=Merge_cols,keep='first')
	print('>>>Find out Commnon and Different sites Done.\n' )
	return (comm_df,diff_df)

def Div(diff_df,dfs):
	diffs = []
	Merge_cols = ["GeneName","Location"]
	for index, df in enumerate(dfs):
		dif = pd.merge(df,diff_df,how = 'inner',on = Merge_cols)
		drop_y(dif)
		diffs.append(dif)
	print('>>>Separete different DataFrame depend on every sample Done.\n')
	return(diffs)

def drop_y(df):
	to_drop = [x for x in df if '_y' in x]
	df.drop(to_drop, axis=1, inplace=True)
	to_drop = [x for x in df if '_x_x' in x]
	df.drop(to_drop, axis=1, inplace=True)
	to_drop = [x for x in df if '1_x' in x]
	df.drop(to_drop, axis=1, inplace=True)
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

def WriteDF(dirpath,filename,df):
	Merge_cols = ["GeneName","Location"]
	print(">>>Write to file:",dirpath+"/"+filename)
	if 'Chr' in df.head():
		df = df.sort_values(Merge_cols)	
	# write dataframe to out dir
	df.to_csv(dirpath+'/'+filename
				,index=None
				,sep = '\t'
				,encoding='utf-8')
	return

def main():
	alltag = "alldiff.xls"
	sigtag = "Significantdiff.xls"
	Merge_cols = ["GeneName","Location"]
	args = getCommands()
	inDir = args.inputDir
	outDir = args.outputDir
	#if  os.path.exists(outDir):
	#	os.remove(outDir)
	if not os.path.exists(outDir):
		os.makedirs(outDir)
	Tags = [alltag, sigtag]
	all_tag_name = "All_common_all.xls"
	sig_tag_name = "All_common_sig.xls"
	sample_col = ['common']
	all_col = []
	sig_col = []
	for idx,tag in enumerate(Tags):
		samples,DFs,File_cols = fetchFiles(inDir, tag)
		if len(samples) == 0:
			continue
		Merge_cols = File_cols[:2]
		com_df,dif_df = Comm_Diff(DFs)
		drop_y(com_df)
		drop_y(dif_df)
		WriteDF(outDir,'All_diff_'+tag,dif_df)
		dif_dfs = Div(dif_df,DFs)
		if idx == 0:
			for s in samples:
				s = s.split("_")[0]+"_"+s.split("_")[1]
				sample_col.append(s)
			WriteDF(outDir,all_tag_name,com_df)
			dif_files = [s+".diff.xls" for s in samples]
			all_col.append(com_df.shape[0])
		if idx == 1:
			WriteDF(outDir,sig_tag_name,com_df)
			dif_files = [s+".diff.xls" for s in samples]
			sig_col.append(com_df.shape[0])

		for i , d in enumerate(dif_dfs):
			WriteDF(outDir,dif_files[i],d)
			if idx == 0:
				all_col.append(d.shape[0])
			else:
				sig_col.append(d.shape[0])
		print("############## ",tag," ALL Done ~\n")
	print(sample_col,all_col,sig_col)
	#sum_df = pd.DataFrame({"Sample":sample_col,"Snp":snp_col})
	sum_df = pd.DataFrame({"Sample":sample_col,"all":all_col,"sig":sig_col})
	#sum_df = sum_df[['Sample','Snp']]
	sum_df = sum_df[['Sample','all','sig']]
	WriteDF(outDir,"Common_Different_summary.xls",sum_df)

	


if __name__ == '__main__':
	main()