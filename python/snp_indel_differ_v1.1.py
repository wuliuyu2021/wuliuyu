#!/usr/bin/env python
# -*- coding: utf-8 -*-


# DATE: 2018-10-30
# AUTHER: WANG WF


import os,re,sys
import numpy as np
import pandas as pd
import argparse


def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to figure out the common and different snvs and indels between samples.')
	parser.add_argument('-i','--input',type=str,dest='inputDir', required=True
				, help='The input directory contains all sample files')
	parser.add_argument('-o','--output',type=str,dest='outputDir',required=True
				, help='The output directory contains all result files')
	parser.add_argument('-r','--skiprows',type=int,dest='skiprows',required=True
				,help = 'type the rows to skip at the head of every file')
	parser.add_argument('-t','--filetype',type=str,dest='fileType',choices =['anno','vcf'],default = 'anno'
				, help='The output directory contains all result files')
	args = parser.parse_args()
	print('>>>Get arguments Done\n')	
	return (args)


def fetchFiles(indir,tag,skiprow):
	# walk the input dir
	# read  all the proper files to DataFrames
	# >push all DataFrames into a list
	# >push all sampleIDs into a list
	# >output sampleIDs list and DataFrames list
	
	# initialize the list
	DFs = []
	IDs = []
	Names = []
	Count = 0
	#if input not dir exit 
	if not os.path.isdir(indir):
		print("The input dir is not a dir path!")
		sys.exit(1)
	
	# walk the input dir
	for dirpath,dirnames,filenames in os.walk(indir):
		for fh in filenames:
			if fh.endswith(tag):
				prefix = fh[:-4]
				filepath = os.path.join(dirpath,fh)
				print("Reading file: ",filepath)
				df= pd.read_csv(filepath,sep = "\t",skiprows=skiprow,encoding='utf-8')
				Count += 1
				if Count == 1:
					Names.extend(df.columns.values.tolist())
				IDs.append(prefix)
				DFs.append(df)
			else:
				continue
	print("\n>>> files number: ",Count)
	print('\n>>> Reads files and push to dataframes Done.\n')
	print(Names)
	return (IDs,DFs,Names)

def Comm_Diff(dfs):
	
	# pull out all the common sites and special sites
	# return a common DataFrame AND a different DataFrame
 
	df_count = 0
	#comm_df = pd.DataFrame(np.zeros([0,Cols_num]),columns=File_cols)
	#diff_df = pd.DataFrame(np.zeros([0,Cols_num]),columns=File_cols)
	for df in dfs:
		df_count += 1
		if df_count == 1:
			comm_df = df
			diff_df = df
		else:
			print("COM",comm_df.iloc[:3,:5])
			print("df",df.iloc[:3,:5])
			comm_df = pd.merge(comm_df,df,how='inner',on=Merge_cols)#,sort=False)
			diff_df = diff_df.append(df,sort=False)
		print(">>>DF Count: ",df_count)
	diff_df = diff_df.drop_duplicates(subset=Merge_cols,keep=False)#.reset_index(drop = True)
	comm_df = comm_df.drop_duplicates(subset=Merge_cols,keep='first')
	print('>>>Find out Commnon and Different sites Done.\n' )
	return (comm_df,diff_df) 


def Div(diff_df,dfs):
	
	# input the DataFrame contains all splical sites 
	# >and the list contains all sample DataFrame
	# 
	# find out every sample special snvs and indels 
	# >push every special DataFrame to a new list
	# >return the list
	
	diffs = []
	for index, df in enumerate(dfs):
		#print(df.shape,diff_df.shape)
		#dif = df.isin(diff_df)
		#dif = df[(df['Chr'] == diff_df['Chr'])&(df['Start'] == diff_df['Start'])&(df['End'] == diff_df['End'])&(df['Ref'] == diff_df['Ref'])&(df['Alt'] == diff_df['Alt'])]
		#dif['Start'],dif['End'] =  dif['Start'].astype('int'),dif['End'].astype('int')
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
	print(">>>Write to file:",dirpath+"/"+filename)
	if 'Chr' in df.head():
		df = df.sort_values(Merge_cols)	
	# write dataframe to out dir
	df.to_csv(dirpath+'/'+filename
				,index=None
				,sep = '\t'
				,encoding='utf-8')
	return

if __name__ == "__main__":
	SnpTag = 'snp.anno.vcf.mm10_multianno.xls'
	IndelTag = 'indel.anno.vcf.mm10_multianno.xls'
	vcf_snpTag = 'snp.vcf'
	vcf_indelTag = 'indel.vcf'
	#File_cols = ['Chr','Start','End','Ref', 'Alt','Func.refGene','Gene.refGene','GeneDetail.refGene','ExonicFunc.refGene','AAChange.refGene','cytoBand','genomicSuperDups','gff3','esp6500siv2_all','1000g2014oct_all','1000g2014oct_afr','1000g2014oct_eas','1000g2014oct_eur','avsnp150','SIFT_score','SIFT_pred','Polyphen2_HDIV_score','Polyphen2_HDIV_pred','Polyphen2_HVAR_score','Polyphen2_HVAR_pred','LRT_score','LRT_pred','MutationTaster_score','MutationTaster_pred','MutationAssessor_score','MutationAssessor_pred','FATHMM_score','FATHMM_pred','RadialSVM_score','RadialSVM_pred','LR_score','LR_pred','VEST3_score','CADD_raw','CADD_phred','GERP++_RS','phyloP46way_placental','phyloP100way_vertebrate','SiPhy_29way_logOdds','cosmic86','clinvar_20180603','gerp++gt2','ExAC_ALL','ExAC_AFR','ExAC_AMR','ExAC_EAS','ExAC_FIN','ExAC_NFE','ExAC_OTH','ExAC_SAS','OMIM','REACTOME_PATHWAY','GO_BP','GO_CC','GO_MF','KEGG_PATHWAY','PID_PATHWAY','Otherinfo']
	Merge_cols = ['Chr','Start','End','Ref', 'Alt']
	#Cols_num = len(File_cols)
	#snp_common_filename = 'All_common_snp.anno.vcf.mm10_multianno.xls'
	#indel_common_filename = 'All_common_indel.anno.vcf.mm10_multianno.xls'
	#common_filenames = [snp_common_filename,indel_common_filename]
	# get the arguments
	args = getCommands()
	inDir,outDir,ftype,skiprow  = args.inputDir,args.outputDir,args.fileType,args.skiprows
	if ftype == 'anno':
		snp_common_filename = 'All_common_snp.anno.vcf.mm10_multianno.xls'
		indel_common_filename = 'All_common_indel.anno.vcf.mm10_multianno.xls'
		Tags = [SnpTag,IndelTag]
		#Tags = [SnpTag]
		skiprow = skiprow
	if ftype == 'vcf':
		snp_common_filename = 'All_common_snp.vcf.xls'
		indel_common_filename = 'All_common_indel.vcf.xls'
		Tags = [vcf_snpTag,vcf_indelTag]
		#Tags = [vcf_snpTag]
	# make dir if input dir is not exist
	if not os.path.exists(outDir):
		os.system('mkdir '+outDir) 
	# initialize the dataframe list and filename list
	sample_col = ['common']
	snp_col = []
	indel_col = []
	for idx,tag in enumerate(Tags):
		samples,DFs,File_cols = fetchFiles(inDir,tag,skiprow)
		if len(samples) == 0:
			continue

		# decide merge on which cols
		# first five cols if input file is anno file
		# 1,2,4,5 cols if input ifle is vcf file
		
		if ftype == 'anno':
			Merge_cols = File_cols[:5]
		if ftype == 'vcf':
			Merge_cols = File_cols[:2]
			Merge_cols.extend(File_cols[3:5])
		com_df,dif_df = Comm_Diff(DFs)
		#dif_df
		drop_y(com_df)
		drop_y(dif_df)
		WriteDF(outDir,'All_diff_'+tag,dif_df)
		dif_dfs = Div(dif_df,DFs)
		if idx == 0:
			for s in samples:
				#slicPos = [i.start() for i in re.finditer("_" , s)]  
				#if "somatic" in s:
				#	s = s[:slicPos[1]]
				#else:
				#	s = s[:slicPos[0]]
				s = s.split("_")[0]+"_"+s.split("_")[1]
				sample_col.append(s)
			
			WriteDF(outDir,snp_common_filename,com_df)
			dif_files = [s+".diff.xls" for s in samples]
			snp_col.append(com_df.shape[0])
		if idx == 1:
			WriteDF(outDir,indel_common_filename,com_df)
			dif_files = [s+".diff.xls" for s in samples]
			indel_col.append(com_df.shape[0])
		for i , d in enumerate(dif_dfs):
			WriteDF(outDir,dif_files[i],d)
			if idx == 0:
				snp_col.append(d.shape[0])
			else:
				indel_col.append(d.shape[0])
		print("############## ",tag," ALL Done ~\n")
	print(sample_col,snp_col,indel_col)
	#sum_df = pd.DataFrame({"Sample":sample_col,"Snp":snp_col})
	sum_df = pd.DataFrame({"Sample":sample_col,"Snp":snp_col,"Indel":indel_col})
	#sum_df = sum_df[['Sample','Snp']]
	sum_df = sum_df[['Sample','Snp','Indel']]
	WriteDF(outDir,"Common_Different_summary.xls",sum_df)
