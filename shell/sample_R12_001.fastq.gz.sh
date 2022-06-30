#!/bin/bash

dir=$1
st=$2

cd $dir

for fq in `ls *R1_001.fastq.gz` `ls *R1.fastq.gz` `ls *1.fq.gz`;
do
frn=$(ls $fq | awk -F "_" '{print $('$st')}')
mv $fq ${frn}_R1_001.fastq.gz
echo "$fq moves to ${frn}_R1_001.fastq.gz"
done 

for fq in `ls *R2_001.fastq.gz` `ls *R2.fastq.gz` `ls *2.fq.gz`;
do
frn=$(ls $fq | awk -F "_" '{print $('$st')}')
mv $fq ${frn}_R2_001.fastq.gz
echo "$fq moves to ${frn}_R2_001.fastq.gz"
done

for fq in `ls *R3_001.fastq.gz` `ls *R3.fastq.gz` `ls *3.fq.gz`;
do
frn=$(ls $fq | awk -F "_" '{print $('$st')}')
mv $fq ${frn}_R3_001.fastq.gz
echo "$fq moves to ${frn}_R3_001.fastq.gz"
done
