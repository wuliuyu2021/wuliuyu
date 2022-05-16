#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
import argparse
import json


def getCommands():
	parser = argparse.ArgumentParser(
				description='A script to get stats json info.')
	parser.add_argument('-i','--indir',dest='indir', required=True, help='The input directory contains input files')
	#parser.add_argument('-i','--outdir',dest='outdir',required=True, help='The input directory contains all  files')
	
	parser.add_argument('-o','--outdir',dest='outdir',required=True, help='The output directory contains result files')
	
	args = parser.parse_args()
	
	return args

def get_jsons(indir):
	pattern = re.compile(r"(^Stats)(.+)json$")
	sjs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	return sjs

def info_write(indir, outdir):
	dn={}
	sjs=get_jsons(indir)
	outcsv=os.path.join(outdir, "sample_stats.xls")
	outcsv_open=open(outcsv,"w")
	head="RunId\tLaneNumber\tOrd_ID\tIndex\tSample_or_Lib\tRaw_Yield(G)\tRaw_Reads_Num(M)\tRaw_Q30(%)\tData_path\n"
	outcsv_open.write(head)
	for sj in sjs:
		f=open(indir+"/"+sj)
		data=json.load(f)
		LaneNumber=data["ReadInfosForLanes"][0]["LaneNumber"]
		RunId=data["RunId"]
		Sampleinfo=data["ConversionResults"][0]["DemuxResults"]
		#for sample in data["ConversionResults"]["DemuxResults"]["SampleName"]:
		print(LaneNumber)
		print(RunId)
		for sampleinfo in Sampleinfo:
			samplename=sampleinfo["SampleName"]
			YieldR1=sampleinfo["ReadMetrics"][0]["Yield"]
			YieldR2=sampleinfo["ReadMetrics"][-1]["Yield"]
			YieldQ30R1=sampleinfo["ReadMetrics"][0]["YieldQ30"]
			YieldQ30R2=sampleinfo["ReadMetrics"][-1]["YieldQ30"]
			Yield=float(YieldR1+YieldR2) 
			#YieldQ30=float(YieldQ30R1+YieldQ30R2) /float(YieldR1+YieldR2)
			NumberReads=float(sampleinfo["NumberReads"]) 
			index=sampleinfo["IndexMetrics"][0]["IndexSequence"]
			if Yield != 0 and samplename.split("_")[2] != "":
				outcsv_open.write("%s\t%s\t%s\t%s\t%s\t%.4f\t%.4f\t%.2f\toss://sz-hapseq/rawfq/20%s%s%s%s/%s/%s\n" % (RunId,
					LaneNumber,
					samplename.split("_")[0],
					index,
					samplename.split("_")[2],
					float(Yield)/1000**3,
					float(NumberReads)/1000**2,
					(float(YieldQ30R1+YieldQ30R2) /float(YieldR1+YieldR2)),
					RunId[0],
					RunId[1],
					RunId[2],
					RunId[3],
					RunId,
					samplename))
			if Yield == 0 and samplename.split("_")[2] != "":
				outcsv_open.write("%s\t%s\t%s\t%s\t%s\t%.4f\t%.4f\t0\toss://sz-hapseq/rawfq/20%s%s%s%s/%s/%s\n" % (RunId,
					LaneNumber,
					samplename.split("_")[0],
					index,
					samplename.split("_")[2],
					float(Yield)/1000**3,
					float(NumberReads)/1000**2,
					RunId[0],
					RunId[1],
					RunId[2],
					RunId[3],
					RunId,
					samplename))
			if Yield != 0 and samplename.split("_")[2] == "":
				outcsv_open.write("%s\t%s\t%s\t%s\t%s\t%.4f\t%.4f\t%.2f\toss://sz-hapseq/rawfq/20%s%s%s%s/%s/%s\n" % (RunId,
					LaneNumber,
					samplename,
					index,
					samplename,
					float(Yield)/1000**3,
					float(NumberReads)/1000**2,
					(float(YieldQ30R1+YieldQ30R2) /float(YieldR1+YieldR2)),
					RunId[0],
					RunId[1],
					RunId[2],
					RunId[3],
					RunId,
					samplename))
			if Yield == 0 and samplename.split("_")[2] != "":
				outcsv_open.write("%s\t%s\t%s\t%s\t%s\t%.4f\t%.4f\t0\toss://sz-hapseq/rawfq/20%s%s%s%s/%s/%s\n" % (RunId,
					LaneNumber,
					samplename,
					index,
					samplename,
					float(Yield)/1000**3,
					float(NumberReads)/1000**2,
					RunId[0],
					RunId[1],
					RunId[2],
					RunId[3],
					RunId,
					samplename))
	outcsv_open.close()




def main():
	args = getCommands()
	indir, outdir=args.indir, args.outdir

	info_write(indir, outdir)
	

if __name__ == "__main__":
	main()
