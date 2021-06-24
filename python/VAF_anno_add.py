#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import time


def table_info(indir):
	pattern=re.compile(r"(.+)(anno)(.+)(multianno.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	print(tabs)

	return tabs


def read_table(indir,outdir):
	tabs=table_info(indir)
	#lts=["ABL1","ASXL1","ATRX","BCOR","BCORL1","BRAF","CALR","CBL","CBLB","CBLC","CDKN2A","CEBPA","CSF3R","CUX1","DNMT3A","JAK3","ETV6/TEL","KDM6A","EZH2","KIT","FBXW7","KRAS","FLT3","MLL","GATA1","MPL","GATA2","MYD88","GNAS","NOTCH1","GNB1","NPM1","HRAS","NRAS","IDH1","PDGFRA","IDH2","PHF6","IKZF1","PPM1D","JAK2","PTEN","PTPN11","RAD21","RUNX1","SETBP1","SF3B1","SMC1A","SMC3","SRSF2","STAG2","TET2","TP53","U2AF1","WT1","ZRSR2"]
	'''csv_header=('Chr\tStart\tEnd\tRef\tAlt\tFunc.refGene\tGene.refGene\tGeneDetail.refGene\t'
		'ExonicFunc.refGene\tAAChange.refGene\tcytoBand\tgenomicSuperDups\tgff3\tesp6500siv2_all\t'
		'1000g2015aug_all\t1000g2015aug_afr\t1000g2015aug_eas\t1000g2015aug_eur\tavsnp150\tSIFT_score\t'
		'SIFT_pred\tPolyphen2_HDIV_score\tPolyphen2_HDIV_pred\tPolyphen2_HVAR_score\tPolyphen2_HVAR_pred\t'
		'LRT_score\tLRT_pred\tMutationTaster_score\tMutationTaster_pred\tMutationAssessor_score\tMutationAssessor_pred\t'
		'FATHMM_score\tFATHMM_pred\tRadialSVM_score\tRadialSVM_pred\tLR_score\tLR_pred\tVEST3_score\tCADD_raw\tCADD_phred\t'
		'GERP++_RS\tphyloP46way_placental\tphyloP100way_vertebrate\tSiPhy_29way_logOdds\tcosmic91\tCLNALLELEID\tCLNDN\t'
		'CLNDISDB\tCLNREVSTAT\tCLNSIG\tgerp++gt2\tExAC_ALL\tExAC_AFR\tExAC_AMR\tExAC_EAS\tExAC_FIN\tExAC_NFE\tExAC_OTH\t'
		'ExAC_SAS\tgwasCatalog\tdbscSNV_ADA_SCORE\tdbscSNV_RF_SCORE\tOMIM\tREACTOME_PATHWAY\tGO_BP\tGO_CC\tGO_MF\tKEGG_PATHWAY\t'
		'PID_PATHWAY\tBIOCARTA_PATHWAY\tOtherinfo\tVAF')'''
	for tab in tabs:
		csv1=os.path.join(outdir, "%s_vaf.xls" % (os.path.basename(tab).split('.xls')[0]))
		if os.path.exists(csv1):
			os.remove(csv1)
		csv1_open=open(csv1, "w")
		csv_header=open(indir+"/"+tab, "r").readlines()[0]
		csv1_open.write("\t".join(csv_header.strip().split("\t")[:])+"\t"+"VAF"+"\n")
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			for line in lines:
				lst = line.strip().split("\t")
				AD=lst[-1].split(" ")[-1].split(':')[1].split(",")[-1]
				DP=lst[-1].split(" ")[-1].split(':')[2]
				if  int(AD) !=0 and int(DP) != 0 :
					VAF=float("%.4f" % (float(AD)/float(DP)))
					csv1_open.write("%s\t%.4f\n" % ("\t".join(lst[:]), VAF))
				if   int(AD) ==0 or  int(DP) == 0 :
					csv1_open.write("%s\t0\n" % ("\t".join(lst[:])))
					
			
		csv1_open.close()

def main():
	indir=sys.argv[1]
	outdir=sys.argv[2]
	read_table(indir,outdir)

if __name__ == '__main__':
	main()