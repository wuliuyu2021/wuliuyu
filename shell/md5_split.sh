#!/bin/bash

md5old=$1
out=$2

rm -f $out/md5_new
if [ ! -d $out ];then
mkdir -p $out
fi

#fq5=$(cat $md5old |awk -F "  " '{print $2}' |awk -F "_" '{print $5}')
for fqcode in `cat $md5old`;
do
code=$(awk -F"  " '{print $1}' $fqcode)
fqR1=$(awk -F"  " '{print $2}' $fqcode |grep "_R1")
fqR2=$(awk -F"  " '{print $2}' $fqcode |grep "_R2")
fqR3=$(awk -F"  " '{print $2}' $fqcode |grep "_R3")
if [[ -f $fqR1 ]] && [[ ! -f $fqR2 ]] && [[ ! -f $fqR3 ]] ;then
fq=$(awk -F"  " '{print $2}' $fqcode |awk -F"_" '{print $('$st')"_R1_001.fastq.gz"}')
echo "$code  $fq" >> $out/md5_new
elif [[ ! -f $fqR1 ]] && [[ -f $fqR2 ]] && [[ ! -f $fqR3 ]] ;then
fq=$(awk -F"  " '{print $2}' $fqcode |awk -F"_" '{print $('$st')"_R2_001.fastq.gz"}')
echo "$code  $fq" >> $out/md5_new
elif [[ ! -f $fqR1 ]] && [[ ! -f $fqR2 ]] && [[ -f $fqR3 ]] ;then
fq=$(awk -F"  " '{print $2}' $fqcode |awk -F"_" '{print $('$st')"_R3_001.fastq.gz"}')
echo "$code  $fq" >> $out/md5_new
fi

done
