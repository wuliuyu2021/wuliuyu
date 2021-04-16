#!/bin/bash

md5old=$1
out=$2
st=$3

if [ ! -d $out ];then
mkdir -p $out
fi

#fq5=$(cat $md5old |awk -F "  " '{print $2}' |awk -F "_" '{print $5}')
if [ $st == "1" ]; then
awk -F"_" '{print $1"_"$NF}' $md5old > $out/md5_new
fi
if [ $st == "2" ]; then
awk -F"_" '{print $1"  "$2"_"$NF}' $md5old |awk -F "  " '{print $1"  "$3}' > $out/md5_new
fi
if [ $st == "3" ]; then
awk -F"_" '{print $1"  "$3"_"$(NF-1)"_001.fastq.gz"}' $md5old |awk -F "  " '{print $1"  "$3}' > $out/md5_new
fi
cd $out
sed -i "s/.fastq.gz/_001.fastq.gz/g" md5_new
