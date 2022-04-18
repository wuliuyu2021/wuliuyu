#!/bin/bash

indir=$1
outdir=$2
num=$3

if [ ! -d $outdir ];then
mkdir -p $outdir
fi

cd $indir
for fq in `ls *_R1_001.fastq.gz` `ls *_R1.fastq.gz` `ls *.filtered.1.fq.gz`;
do
flag1=$(echo $fq |awk -F "R1" '{print $NF}')
flag2=$(echo $fq |awk -F ".filtered.1" '{print $NF}')
if [ $flag1 == "_001.fastq.gz" ] || [ $flag1 == ".fastq.gz" ];then
prefix1=$(echo $fq |awk -F "_R1" '{print $1}' |awk -F "_" '{print $1}')
prefix2=$(echo $fq |awk -F "_R1" '{print $1}' |awk -F "_" '{print $2}')
prefix3=$(echo $fq |awk -F "_R1" '{print $1}' |awk -F "_" '{print $3}')
prefix4=$(echo $fq |awk -F "_R1" '{print $1}' |awk -F "_" '{print $4}')
if [ $num == "1" ];then
less $indir/$fq |head -n 80000 > $outdir/${prefix1}.fastq
fi
if [ $num == "2" ];then
less $indir/$fq |head -n 80000 > $outdir/${prefix2}.fastq
fi
if [ $num == "3" ];then
less $indir/$fq |head -n 80000 > $outdir/${prefix3}.fastq
fi
if [ $num == "4" ];then
less $indir/$fq |head -n 80000 > $outdir/${prefix4}.fastq
fi
fi
if [ $flag2 == ".fq.gz" ];then
prefix=$(echo $fq |awk -F ".filtered.1" '{print $1}' )
less $indir/$fq |head -n 80000 > $outdir/${prefix}.fastq
fi
done
