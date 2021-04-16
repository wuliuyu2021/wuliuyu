#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import os
import re
import heapq
from sr_seqcsv import Seqcsv
reload(sys)
sys.setdefaultencoding('utf-8')


def open_stats(json_f):
	num=1
	d_sample_info={}
	d_lane_info={}
	d_untop_info={}
	samples=[]
	lanes=[]
	lanes_indexs_num=[]
	f = open(json_f, 'r')
	data = json.load(f)
	Runid = data["RunId"]
	for UnknownBarcode in data["UnknownBarcodes"]:
		lane=str(UnknownBarcode["Lane"])
		Barcode=UnknownBarcode["Barcodes"]
		d_untop_info[lane]={
		"UnknownBarcodes":Barcode,
		}
	for ConversionResult in data["ConversionResults"]:
		LaneNumber=str(ConversionResult["LaneNumber"])
		lanes.append(LaneNumber)
		TotalClustersRaw=ConversionResult["TotalClustersRaw"]
		TotalClustersPF=ConversionResult["TotalClustersPF"]
		lane_Yield=float(ConversionResult["Yield"]) / 1000**3
		Undetermined_yield=float(ConversionResult["Undetermined"]["Yield"]) / 1000**3
		Undetermined_Raw_Rate=Undetermined_yield * 100 / lane_Yield
		Undetermined_Q30 = (float(ConversionResult["Undetermined"]["ReadMetrics"][0]["YieldQ30"]) + 
			float(ConversionResult["Undetermined"]["ReadMetrics"][-1]["YieldQ30"])) * 100 /1000**3 / Undetermined_yield
		PF=float(TotalClustersPF) * 100/float(TotalClustersRaw)
		d_lane_info[LaneNumber]={
		"Seq_ID":Runid,
		"Lane_Number":LaneNumber,
		"Pool_ID":[],
		"Sample_Num":0,
		"Indexs":[],
		"Lib_Types":[],
		"Client_IDs":[],
		"Read_Type":[],
		"Estimated_Yield":0.00,
		"Raw_Yield":0.00,
		"Raw_Q30":0.00,
		"Undetermined_Raw_Yield":Undetermined_yield,
		"Total_Raw_Yield":lane_Yield,
		"Undetermined_Raw_Rate":Undetermined_Raw_Rate,
		"TotalClustersRaw":TotalClustersRaw,
		"TotalClustersPF":TotalClustersPF,
		"PF":PF,
		"Occupied_Read":"",
		"Undetermined_Top20_Indexs":[]
		}
		for DemuxResult in ConversionResult["DemuxResults"]:
			SampleId=DemuxResult["SampleId"].encode('utf-8')
			samples.append(SampleId)
			NumberRead = float(DemuxResult["NumberReads"]) * 2 / 1000 ** 2
			indexseq=DemuxResult["IndexMetrics"][-1]["IndexSequence"]
			Yield = float(DemuxResult["Yield"]) / 1000 ** 3
			YieldQ30_R1 = float(DemuxResult["ReadMetrics"][0]["YieldQ30"])
			YieldQ30_R2 = float(DemuxResult["ReadMetrics"][-1]["YieldQ30"])
			YQ30=float(YieldQ30_R1 + YieldQ30_R2) * 100 / float(DemuxResult["Yield"])
			rawdata_path=os.path.join("path", SampleId)
			d_sample_info[SampleId]={
			"Seq_ID":Runid,
			"Lane_Number":LaneNumber,
			"Ord_ID":"",
			"Index":indexseq,
			"Lib_ID":"",
			"Lib_Type":"",
			"Sample_ID":"",
			"Contract_ID":"",
			"Client_ID":"",
			"Read_Type":"",
			"Estimated_Yield":0.00,
			"Raw_Data_Path":rawdata_path,
			"Raw_Yield":Yield,
			"Raw_Reads_Num":NumberRead,
			"Raw_Q30":YQ30
			}
	for lane in lanes:
		for sample in samples:
			if d_sample_info[sample]["Lane_Number"] == lane:
				d_lane_info[lane]["Sample_Num"] += 1
				d_lane_info[lane]["Raw_Yield"] += d_sample_info[sample]["Raw_Yield"]
				d_lane_info[lane]["Raw_Q30"] += d_sample_info[sample]["Raw_Q30"]
				#d_lane_info[lane]["Undetermined_Top20_Indexs"].append('/'.join(d_untop_info[lane][0:20]))
		value_20s=heapq.nlargest(20, set(d_untop_info[lane]["UnknownBarcodes"].values()))
		for (key,value) in d_untop_info[lane]["UnknownBarcodes"].items():
			for value_20 in sorted(value_20s):
				if value_20 == value:
					d_lane_info[lane]["Undetermined_Top20_Indexs"].append("%s:%s" %(key,value))
		#print(d_lane_info[lane]["Undetermined_Top20_Indexs"])
	return d_sample_info, d_lane_info	

def result_write(json_f, seqcsv, outdir):
	d_sample_info=open_stats(json_f)[0]
	d_lane_info=open_stats(json_f)[1]
	lanes=[]
	sample_out_head = (
		"Seq_ID,Lane_Number,Ord_ID,Index,Lib_ID,Lib_Type,Sample_ID,"
		"Contract_ID,Client_ID,Read_Type,Estimated_Yield(G),Raw_Data_Path,"
		"Raw_Yield(G),Raw_Reads_Num(M),Raw_Q30(%),Raw_Q20(%),Raw_GC(%),"
		"Clean_Yield(G),Clean_Reads_Num(M),Clean_Q30(%),Clean_Q20(%),"
		"Clean_GC(%),Effective(%),Duplication_Rate(%),Filter_Cmd")
	lane_out_head = (
		"Seq_ID,Lane_Number,Pool_ID,Sample_Num,Indexs,Lib_Types,"
		"Client_IDs,Read_Type,Estimated_Yield(G),Raw_Yield(G),"
		"Raw_Q30(%),Raw_GC(%),Undetermined_Raw_Yield(G),"
		"Undetermined_Raw_Q30(%),Undetermined_Raw_GC(%),"
		"Total_Raw_Yield(G),Undetermined_Raw_Rate(%),Clean_Yield(G),"
		"Clean_Q30(%),Clean_GC(%),Effective(%),Duplication_Rate(%),"
		"TotalClustersRaw,TotalClustersPF,%PF,%PF_Read1,%PF_Read2,"
		"%Occupied_Read1,%Occupied_Read2,Undetermined_Top20_Indexs")
	csv1=os.path.join(outdir,'%s_bcl2fastq_sample_qc.csv' % '_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]))
	csv2=os.path.join(outdir,'%s_bcl2fastq_lane_qc.csv' % '_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]))
	f1=open(csv1, 'w')
	f1.write(sample_out_head+'\n')
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		lanes.append(lst.laneID)
		flag = "%s_%s_%s_%s" % (lst.ordID, lst.projectID, lst.libID, os.path.basename(seqcsv).split('.csv')[0].split('_')[-1])
		if flag in sorted(d_sample_info.keys()):
			sample_out="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%.4f,%s,%.4f,%.2f,%.2f,,,,,,,,,," % (
				d_sample_info[flag]["Seq_ID"],
				d_sample_info[flag]["Lane_Number"],
				lst.ordID,
				d_sample_info[flag]["Index"],
				lst.libID,
				lst.libtype,
				lst.clientID,
				lst.contractID,
				lst.whereFromID,
				lst.readType,
				float(lst.estimateProduct),
				d_sample_info[flag]["Raw_Data_Path"],
				d_sample_info[flag]["Raw_Yield"],
				d_sample_info[flag]["Raw_Reads_Num"],
				d_sample_info[flag]["Raw_Q30"])
			f1.write(sample_out+'\n')
			if lst.laneID in d_lane_info.keys():
				d_lane_info['%s' % lst.laneID]["Estimated_Yield"] += float(lst.estimateProduct)
				d_lane_info['%s' % lst.laneID]["Pool_ID"].append(lst.poolID)
				d_lane_info['%s' % lst.laneID]["Indexs"].append(d_sample_info[flag]["Index"])
				d_lane_info['%s' % lst.laneID]["Lib_Types"].append(lst.libtype)
				d_lane_info['%s' % lst.laneID]["Client_IDs"].append(lst.whereFromID)
				d_lane_info['%s' % lst.laneID]["Read_Type"].append(lst.readType)
	f1.close()
	f2=open(csv2, 'w')
	f2.write(lane_out_head+'\n')
	#print(d_lane_info)
	for lane in sorted(set(lanes)):
		if lane in sorted(d_lane_info.keys()):
			lane_out = "%s,%s,%s,%d,%s,%s,%s,%s,%.4f,%.4f,%.2f,,%.4f,,,%.4f,%.2f,0,,,0,,%s,%s,%.2f,,,,,%s" % (
				d_lane_info[lane]["Seq_ID"],
				d_lane_info[lane]["Lane_Number"],
				'/'.join(set(d_lane_info[lane]["Pool_ID"])),
				d_lane_info[lane]["Sample_Num"],
				'/'.join(d_lane_info[lane]["Indexs"]),
				'/'.join(d_lane_info[lane]["Lib_Types"]),
				'/'.join(set(d_lane_info[lane]["Client_IDs"])),
				'/'.join(set(d_lane_info[lane]["Read_Type"])),
				d_lane_info[lane]["Estimated_Yield"],
				d_lane_info[lane]["Raw_Yield"],
				d_lane_info[lane]["Raw_Q30"] / d_lane_info[lane]["Sample_Num"],
				d_lane_info[lane]["Undetermined_Raw_Yield"],
				d_lane_info[lane]["Total_Raw_Yield"],
				d_lane_info[lane]["Undetermined_Raw_Rate"],
				d_lane_info[lane]["TotalClustersRaw"],
				d_lane_info[lane]["TotalClustersPF"],
				d_lane_info[lane]["PF"],
				'/'.join(d_lane_info[lane]["Undetermined_Top20_Indexs"])
				)
			f2.write(lane_out+'\n')
	f2.close()


def main():
	json_f=sys.argv[1]
	seqcsv=sys.argv[2]
	outdir=sys.argv[3]
	result_write(json_f, seqcsv, outdir)


if __name__ == '__main__':
	main()