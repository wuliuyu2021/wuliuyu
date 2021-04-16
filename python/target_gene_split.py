#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import time
#from collections import Counter
#import pandas as pd
#import numpy as np

def table_info(indir):
	pattern=re.compile(r"(.+)(anno)(.+)(multianno.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	print(tabs)

	return tabs

def read_table(indir):
	tabs=table_info(indir)
	lts=["ABL1","ASXL1","ATRX","BCOR","BCORL1","BRAF","CALR","CBL","CBLB","CBLC","CDKN2A","CEBPA","CSF3R","CUX1","DNMT3A","JAK3","ETV6/TEL","KDM6A","EZH2","KIT","FBXW7","KRAS","FLT3","MLL","GATA1","MPL","GATA2","MYD88","GNAS","NOTCH1","GNB1","NPM1","HRAS","NRAS","IDH1","PDGFRA","IDH2","PHF6","IKZF1","PPM1D","JAK2","PTEN","PTPN11","RAD21","RUNX1","SETBP1","SF3B1","SMC1A","SMC3","SRSF2","STAG2","TET2","TP53","U2AF1","WT1","ZRSR2"]
	csv_header=(
		'Chr\tStart\tEnd\tRef\tAlt\tFunc.refGene\tGene.refGene\tGeneDetail.refGene\t'
		'ExonicFunc.refGene\tAAChange.refGene\tcytoBand\tgenomicSuperDups\tgff3\tesp6500siv2_all\t'
		'1000g2014oct_all\t1000g2014oct_afr\t1000g2014oct_eas\t1000g2014oct_eur\tavsnp150\tSIFT_score\t'
		'SIFT_pred\tPolyphen2_HDIV_score\tPolyphen2_HDIV_pred\tPolyphen2_HVAR_score\tPolyphen2_HVAR_pred\t'
		'LRT_score\tLRT_pred\tMutationTaster_score\tMutationTaster_pred\tMutationAssessor_score\t'
		'MutationAssessor_pred\tFATHMM_score\tFATHMM_pred\tRadialSVM_score\tRadialSVM_pred\tLR_score\t'
		'LR_pred\tVEST3_score\tCADD_raw\tCADD_phred\tGERP++_RS\tphyloP46way_placental\tphyloP100way_vertebrate\t'
		'SiPhy_29way_logOdds\tcosmic86\tclinvar_20190305\tgerp++gt2\tExAC_ALL\tExAC_AFR\tExAC_AMR\tExAC_EAS\t'
		'ExAC_FIN\tExAC_NFE\tExAC_OTH\tExAC_SAS\tgwasCatalog\tdbscSNV_ADA_SCORE\tdbscSNV_RF_SCORE\tOMIM\t'
		'REACTOME_PATHWAY\tGO_BP\tGO_CC\tGO_MF\tKEGG_PATHWAY\tPID_PATHWAY\tBIOCARTA_PATHWAY\tOtherinfo\tVAF')
	for tab in tabs:
		csv1=os.path.join(indir, "%s_target_gene.xls" % (os.path.basename(tab).split('.xls')[0]))
		#csv2=os.path.join(indir, "%s_005.xls" % (os.path.basename(tab).split('.xls')[0]))
		if os.path.exists(csv1):
			os.remove(csv1)
		#if os.path.exists(csv2):
		#	os.remove(csv2)
		csv1_open=open(csv1, "w")
		#csv2_open=open(csv2, "w")
		
		csv1_open.write(csv_header+"\n")
		#csv2_open.write(csv_header+"\n")
		#row_csv_open.write(csv_header)
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				AD=lst[66].split(" ")[-1].split(':')[1].split(",")[-1]
				DP=lst[66].split(" ")[-1].split(':')[2]
				
				#if lst[6] in lts and AD!=0 and DP != 0:
				if  int(AD) !=0 and int(DP) != 0:
					VAF=float("%.4f" % (float(AD)/float(DP)))
					#print("%s/%s"% (AD,DP))
					#print(VAF)
					csv1_open.write(
						lst[0]+"\t"+lst[1]+"\t"+lst[2]+"\t"+lst[3]+"\t"+lst[4]+"\t"+lst[5]+"\t"+lst[6]+"\t"+lst[7]+"\t"+lst[8]+"\t"+
						lst[9]+"\t"+lst[10]+"\t"+lst[11]+"\t"+lst[12]+"\t"+lst[13]+"\t"+lst[14]+"\t"+lst[15]+"\t"+lst[16]+"\t"+lst[17]
						+"\t"+lst[18]+"\t"+lst[19]+"\t"+lst[20]+"\t"+lst[21]+"\t"+lst[22]+"\t"+lst[23]+"\t"+lst[24]+"\t"+lst[25]+"\t"+
						lst[26]+"\t"+lst[27]+"\t"+lst[28]+"\t"+lst[29]+"\t"+lst[30]+"\t"+lst[31]+"\t"+lst[32]+"\t"+lst[33]+"\t"+lst[34]
						+"\t"+lst[35]+"\t"+lst[36]+"\t"+lst[37]+"\t"+lst[38]+"\t"+lst[39]+"\t"+lst[40]+"\t"+lst[41]+"\t"+lst[42]+"\t"+
						lst[43]+"\t"+lst[44]+"\t"+lst[45]+"\t"+lst[46]+"\t"+lst[47]+"\t"+lst[48]+"\t"+lst[49]+"\t"+lst[50]+"\t"+lst[51]
						+"\t"+lst[52]+"\t"+lst[53]+"\t"+lst[54]+"\t"+lst[55]+"\t"+lst[56]+"\t"+lst[57]+"\t"+lst[58]+"\t"+lst[59]+"\t"+
						lst[60]+"\t"+lst[61]+"\t"+lst[62]+"\t"+lst[63]+"\t"+lst[64]+"\t"+lst[65]+"\t"+lst[66]+"\t"+str(VAF)+"\n")
				if   int(AD) ==0 or  int(DP) == 0:
					#print("%s--%s"% (AD, DP))
					'''AD=lst[66].split(" ")[-1].split(':')[1].split(",")[-1]
					DP=lst[66].split(" ")[-1].split(':')[2]
					VAF=float("%.4f" % (float(AD)/float(DP)))'''
					#print("%s/%s"% (AD,DP))
					#print(VAF)
					csv1_open.write(
						lst[0]+"\t"+lst[1]+"\t"+lst[2]+"\t"+lst[3]+"\t"+lst[4]+"\t"+lst[5]+"\t"+lst[6]+"\t"+lst[7]+"\t"+lst[8]+"\t"+
						lst[9]+"\t"+lst[10]+"\t"+lst[11]+"\t"+lst[12]+"\t"+lst[13]+"\t"+lst[14]+"\t"+lst[15]+"\t"+lst[16]+"\t"+lst[17]
						+"\t"+lst[18]+"\t"+lst[19]+"\t"+lst[20]+"\t"+lst[21]+"\t"+lst[22]+"\t"+lst[23]+"\t"+lst[24]+"\t"+lst[25]+"\t"+
						lst[26]+"\t"+lst[27]+"\t"+lst[28]+"\t"+lst[29]+"\t"+lst[30]+"\t"+lst[31]+"\t"+lst[32]+"\t"+lst[33]+"\t"+lst[34]
						+"\t"+lst[35]+"\t"+lst[36]+"\t"+lst[37]+"\t"+lst[38]+"\t"+lst[39]+"\t"+lst[40]+"\t"+lst[41]+"\t"+lst[42]+"\t"+
						lst[43]+"\t"+lst[44]+"\t"+lst[45]+"\t"+lst[46]+"\t"+lst[47]+"\t"+lst[48]+"\t"+lst[49]+"\t"+lst[50]+"\t"+lst[51]
						+"\t"+lst[52]+"\t"+lst[53]+"\t"+lst[54]+"\t"+lst[55]+"\t"+lst[56]+"\t"+lst[57]+"\t"+lst[58]+"\t"+lst[59]+"\t"+
						lst[60]+"\t"+lst[61]+"\t"+lst[62]+"\t"+lst[63]+"\t"+lst[64]+"\t"+lst[65]+"\t"+lst[66]+"\t"+"0"+"\n")
			
		csv1_open.close()
		#csv2_open.close()



def main():
	indir=sys.argv[1]
	#table=sys.argv[2]
	time1=time.time()
	read_table(indir)
	#csv_trans(indir)
	time2=time.time()
	print("Time used: %s" %(str(time2-time1)))


if __name__ == '__main__':
	main()