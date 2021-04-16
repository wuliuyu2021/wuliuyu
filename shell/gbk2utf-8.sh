#!/bin/bash

runid=$1
seqcity=$2
[[ $# -lt 2 ]] && echo "The number of parameter is less than 2 Please check!" && exit 0

if [ $seqcity == 'sr' ];then
basedir="/thinker/nfs2/longrw/runPipelineInfo"
month=${runid:0:4}
seqinfo="$basedir/20$month/$runid/sequence_${runid}.csv"

if [[ -e $seqinfo ]];then
	cat /thinker/nfs5/public/wuliuyu/wuliuyu/csv_file/seqcsv_header.csv $seqinfo > $basedir/20$month/$runid/new_sequence_${runid}.csv
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/new_sequence_${runid}.csv -o $basedir/20$month/$runid/sequence_${runid}_utf-8.csv
	rm -f $basedir/20$month/$runid/new_sequence_${runid}.csv
else
	echo \"NO $seqinfo, please check!!!\"
	exit -1
fi


if [[ -e $basedir/20$month/$runid/07_qc_o/${runid}_sample_qc.csv ]];then
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/07_qc_o/${runid}_sample_qc.csv -o $basedir/20$month/$runid/${runid}_sample_qc_utf-8.csv
else
	echo \"NO $basedir/20$month/$runid/07_qc_o/${runid}_sample_qc.csv, please check!!!\"
	exit -1
fi


if [[ -e $basedir/20$month/$runid/07_qc_o/${runid}_all_lane_qc.csv ]];then
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/07_qc_o/${runid}_all_lane_qc.csv -o $basedir/20$month/$runid/${runid}_all_lane_qc_utf-8.csv
else
	echo \"NO $basedir/20$month/$runid/07_qc_o/${runid}_all_lane_qc.csv, please check!!!\"
	exit -1
fi
fi
if [ $seqcity == 'sz' ];then
basedir="/data/users/hapseq/runPipelineInfo"
month=${runid:0:4}
seqinfo="$basedir/20$month/$runid/sequence_${runid}.csv"

if [[ -e $seqinfo ]];then
	cat /data/users/wuliuyu/wuliuyu/csv_file/seqcsv_header.csv $seqinfo > $basedir/20$month/$runid/new_sequence_${runid}.csv
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/new_sequence_${runid}.csv -o $basedir/20$month/$runid/sequence_${runid}_utf-8.csv
	ossutil cp -u $basedir/20$month/$runid/sequence_${runid}_utf-8.csv oss://sz-hapdeliver/Data_from_SR/$runid/
	rm -f $basedir/20$month/$runid/new_sequence_${runid}.csv
else
	echo \"NO $seqinfo, please check!!!\"
	exit -1
fi


if [[ -e $basedir/20$month/$runid/07_qctab/${runid}_sample_qc.csv ]];then
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/07_qctab/${runid}_sample_qc.csv -o $basedir/20$month/$runid/${runid}_sample_qc_utf-8.csv
	ossutil cp -u $basedir/20$month/$runid/${runid}_sample_qc_utf-8.csv oss://sz-hapdeliver/Data_from_SR/$runid/
else
	echo \"NO $basedir/20$month/$runid/07_qctab/${runid}_sample_qc.csv, please check!!!\"
	exit -1
fi


if [[ -e $basedir/20$month/$runid/07_qctab/${runid}_lane_qc.csv ]];then
	iconv -f gbk -t utf-8 $basedir/20$month/$runid/07_qctab/${runid}_lane_qc.csv -o $basedir/20$month/$runid/${runid}_lane_qc_utf-8.csv
	ossutil cp -u $basedir/20$month/$runid/${runid}_lane_qc_utf-8.csv oss://sz-hapdeliver/Data_from_SR/$runid/
else
	echo \"NO $basedir/20$month/$runid/07_qctab/${runid}_lane_qc.csv, please check!!!\"
	exit -1
fi
fi
