#!/bin/bash

infile=$1
outdir=$2
rm -f $outdir/*tmp
infilename=$(ls $infile |awk -F "/" '{print $NF}')
tmp=$outdir/${infilename}_tmp

for info in `cat $infile`

do
fq=$(echo $info |awk -F "," '{print $2}')
sample=$(echo $info |awk -F "," '{print $1}')
ossdir=$(ossutil ls  $fq |tail -n 4 |head -n 1 |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
echo "${sample},${ossdir}" >> $tmp
done
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -o $outdir