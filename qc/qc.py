#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re
from optparse import OptionParser
import time
from csv_info import Seqcsv
from fastp_info import Fastp
reload(sys)
sys.setdefaultencoding('utf-8')

def parse_cmd():
	usage = (
        "Quality Control for Illumina raw fastq reads data\n"
        "CMD: python %prog <-i rawfqdir> <-j jsondir> <-o outdir> <-p pid> <-y seqinfo>\n")
	version = "%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option(
        "-i", "--rawfqdir", dest="rawfqdir",
        help="the raw fastq files directory")
	parser.add_option(
        "-j", "--jsondir", dest="jsondir",
        help="the json files directory")
	parser.add_option(
        "-o", "--outdir", dest="outdir", default=None,
        help="the output directory")
	parser.add_option(
        "-s", "--seqinfo", dest="seqinfo",
        help="the seqinfo csv")
	parser.add_option(
        "-p", "--pid", dest="projectid", default=None,
        help="specify the project id, default is None")
	
	return parser.parse_args()

def get_rawdir_files(options):
	if os.path.exists(options.projectid):
		pattern=re.compile(r"(S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz|_001.fq.gz|_001.fastq)$" % options.projectid)
	else:
		pattern=re.compile(r"(S\d+)(.+)(_R1)(_001.fastq.gz|_001.fq.gz|_001.fastq)$")
	undetermineds=filter(lambda x: re.match(r'Undetermined(.+)R1(.+)', x), os.listdir(options.rawfqdir))
	srs=sorted(filter(lambda x:re.match(pattern, x), os.listdir(options.rawfqdir)))

	return srs + undetermineds

def get_fastp_json_files(options):
	if os.path.exists(options.projectid):
		pattern = re.compile(r"(^S\d+)(_%s_)(.+).json$" % options.projectid)
	else:
		pattern = re.compile(r"(.+).json$")
	jfs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(options.jsondir)))

	return jfs

def qc_csv(seqinfo, rawfqfs, fastpjsonfs, rawfqjsonfs, sampleout, laneout):
	sample_out_head = (
        "Seq_ID,Lane_Number,Ord_ID,Index,Lib_ID,Lib_Type,Sample_ID,"
        "Contract_ID,Client_ID,Read_Type,Estimated_Yield(G),Raw_Data_Path,"
        "Raw_Yield(G),Raw_Reads_Num(M),Raw_Q30(%),Raw_Q20(%),Raw_GC(%),"
        "Clean_Yield(G),Clean_Reads_Num(M),Clean_Q30(%),Clean_Q20(%),"
        "Clean_GC(%),Effective(%),Duplication_Rate(%),Filter_Cmd")
	'''Lane_out_head = (
        "Seq_ID,Lane_Number,Pool_ID,Sample_Num,Indexs,Lib_Types,"
        "Client_IDs,Read_Type,Estimated_Yield(G),Raw_Yield(G),"
        "Raw_Q30(%),Raw_GC(%),Undetermined_Raw_Yield(G),"
        "Undetermined_Raw_Q30(%),Undetermined_Raw_GC(%),"
        "Total_Raw_Yield(G),Undetermined_Raw_Rate(%),Clean_Yield(G),"
        "Clean_Q30(%),Clean_GC(%),Effective(%),Duplication_Rate(%),"
        "TotalClustersRaw,TotalClusterPF,%PF,Undetermined_Top20_Indexs")'''
	sample_out.write(sample_out_head)
	seq_id = os.path.basename(os.path.dirname(seqinfo))
	flowcell_id = seq_id.split("_")[-1]
	rawdata_path = ""
	poolid = ""
	readtype = ""
	undetermined_raw_yield = 0.00
	Undetermined_Raw_Q30 = 0.00
	Undetermined_Raw_GC = 0.00
	TotalClustersRaw = 1
	TotalClusterPF = 0
	Undetermined_Top20_Indexs = ""
	lane_number = -1
	sample_num = 1
	indexs = []
	lib_types = []
	client_ids = []
	esti_yield = 0.00
	raw_yield = 0.00
	raw_q30 = 0.00
	raw_gc = 0.00
	und_raw_yield = 0.00
	und_raw_q30 = 0.00
	und_raw_gc = 0.00
	clean_yield = 0.00
	clean_q30 = 0.00
	clean_gc = 0.00
	duplication_rate = 0.00
	sample = Seqcsv(sampleinfo.split(","))
	flag = "_".join([sample.ordID, sample.projectID, sample.clientID, flowcell_id])
	for jsonf in fastpjsonfs:
		if flag in jsonf:
                # print jsonf
			f = open(jsonf, "r")
			fastp = Fastp(f)
                # write sample information
			index = sample.indexSeq if sample.indexSeq != "" else sample.indexID
                # print rawfqfiles
			rawdata_path = os.path.join("path", flag)
			for rawfqfile in rawfqfs:
				if flag in os.path.basename(rawfqfile):
					rawdata_path = os.path.join(os.path.dirname(rawfqfile), flag)
                # print index
					sample_out_line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%.4f,%s,%.4f,%.2f,%.2f,%.2f,%.2f,%.4f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%s" % (
					seq_id, sample.laneID, sample.ordID, index, sample.libID,
					sample.libtype, sample.clientID, sample.contractID,
					sample.whereFromID, sample.readType,
					float(sample.estimateProduct), rawdata_path,
					float(fastp.raw_bases_num) / 1000**3,
					float(fastp.raw_reads_num) / 1000**2,
					float(fastp.raw_q30_rate) * 100,
					float(fastp.raw_q20_rate) * 100,
					float(fastp.raw_gc_content) * 100,
					float(fastp.clean_bases_num) / 1000**3,
					float(fastp.clean_reads_num) / 1000**2,
					float(fastp.clean_q30_rate) * 100,
					float(fastp.clean_q20_rate) * 100,
					float(fastp.clean_gc_content) * 100,
					(float(fastp.clean_bases_num) / float(fastp.raw_bases_num)) * 100,
					float(fastp.dup_rate) * 100,
					fastp.command.encode('utf-8'))
				sample_out.write("%s\n" % sample_out_line)
	sample_out.close()

def main():
	time1=time.time()
	(options, args)=parse_cmd()
	seqID = os.path.basename(os.path.dirname(options.seqinfo))
	if not os.path.exists(options.outdir):
		os.makedirs(options.outdir)

	rawfqfiles=get_rawdir_files(options.rawfqdir)
	rawfqfs = [os.path.join(options.rawfqdir, rawfqfile) for rawfqfile in rawfqfiles]

	fastpjfs = get_fastp_json_files(options)
	fastpjsonfs = [os.path.join(options.jsondir, jf) for jf in fastpjfs]

	sample_out = os.path.join(options.outdir, "%s_sample.csv" % seqID)
	#lane_out = os.path.join(options.outdir, "%s_lane.csv" % seqID)
	
	if os.path.exists(options.projectid):
		sample_out = os.path.join(options.outdir, "%s_%s_sample.csv" % (seqID, options.projectid))
		#lane_out = os.path.join(options.outdir, "%s_%s_lane.csv" % (seqID, options.projectid))
	qc_csv(options.seqinfo, rawfqfs, fastpjsonfs, rawfqjsonfs, sample_out, lane_out)

	time2 = time.time()
	print("Time used: %s" % str(time2 - time1))


if __name__ == '__main__':
	main()