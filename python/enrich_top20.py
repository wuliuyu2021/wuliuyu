#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re, json, csv
import time
import argparse

def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to figure out the top20 in Enrich results.')
	parser.add_argument('-i','--input',type=str,dest='inputDir', required=True
				, help='The input directory contains all sample files')
	parser.add_argument('-o','--output',type=str,dest='outputDir',required=True
				, help='The output directory contains all result files')
	parser.add_argument('-p','--pflag',type=str,dest='pflag',required=True
				, help='Input pvalue or p.adjust')
	args = parser.parse_args()
	return args

def infile(indir):
	pattern=re.compile(r"(.+)(Reactome_Enrich.xls|KEGG_Enrich.xls)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(indir)))
	return tabs

def p_value_adj(indir, outdir, pflag):
	header="ID\tDescription\tGeneRatio\tBgRatio\tpvalue\tp.adjust\tqvalue\tgeneID\tCount\n"
	tabs=infile(indir)
	for tab in tabs:
		with open("%s/%s" %(indir, tab), "r") as f:
			lines = f.readlines()[1:]
			if lines == "":
				continue
			else:
				new_xls=os.path.join(outdir,"%s_tmp" % os.path.basename(tab))
				new_xls_open=open(new_xls, "w")
				new_xls_open.write(header)
				for line in lines:
					lst = line.strip().split("\t")
					if pflag == "p.adjust":
						if float(lst[5]) < 0.05:
							new_xls_open.write(lst[0]+"\t"+lst[1]+"\t"+lst[2]+"\t"+lst[3]+"\t"+lst[4]+"\t"+lst[5]+"\t"+lst[6]+"\t"+lst[7]+"\t"+lst[8]+"\n")
					if pflag == "pvalue":
						if float(lst[4]) < 0.05:
							new_xls_open.write(lst[0]+"\t"+lst[1]+"\t"+lst[2]+"\t"+lst[3]+"\t"+lst[4]+"\t"+lst[5]+"\t"+lst[6]+"\t"+lst[7]+"\t"+lst[8]+"\n")
				new_xls_open.close()

def main():
	args = getCommands()
	indir = args.inputDir
	outdir = args.outputDir
	pflag = args.pflag
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	p_value_adj(indir, outdir, pflag)
	os.chdir(outdir)
	if os.path.exists("%s/work.sh" % outdir):
		os.remove("%s/work.sh" % outdir)
	pattern=re.compile(r"(.+)(Enrich.xls_tmp)$")
	tabs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(outdir)))
	for tab in tabs:
		os.system("less %s |head -n 21 > %s" % (tab,os.path.basename(tab).split("_tmp")[0]))
		if os.path.basename(tab).split("_Enrich")[0].split(".")[1] == "KEGG":
			sample=os.path.basename(tab).split("_tmp")[0]
			group=os.path.basename(tab).split(".KEGG_Enrich.xls_tmp")[0]
			os.system("echo \"Rscript pathway_Bubble_plot_2.R -i %s -n %s -t KEGG \"  >> work.sh" % (sample,group))
		if os.path.basename(tab).split("_Enrich")[0].split(".")[1] == "Reactome":
			sample=os.path.basename(tab).split("_tmp")[0]
			group=os.path.basename(tab).split(".Reactome_Enrich.xls_tmp")[0]
			os.system("echo \"Rscript pathway_Bubble_plot_2.R -i %s -n %s -t Reactome\" >> work.sh"% (sample,group))
	os.system("rm -f *xls_tmp")


if __name__ == '__main__':
	main()