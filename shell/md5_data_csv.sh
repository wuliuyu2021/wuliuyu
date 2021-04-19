#!/bin/bash

infile=$1
outdir=$2

rm -f $outdir/tmp.txt

do

#fq=$(echo $info |awk -F "," '{print $2}')
#sample=$(echo $info |awk -F "/" '{print $NF}')
ossdir=$(ossutil ls  $info |tail -n 4 |head -n 1 |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
sample=$(echo $ossdir |awk -F "/" '{print $NF}')
echo "${sample},${ossdir}" >> $outdir/tmp.txt
done
python /data/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $outdir/tmp.txt -o $outdir
