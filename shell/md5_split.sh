#!/bin/bash

md5old=$1
out=$2
st=$3

md5name=$(ls $md5old |awk -F"/" '{print $NF}')
rm -f $out/${md5name}_new
if [ ! -d $out ];then
mkdir -p $out
fi

#fq5=$(cat $md5old |awk -F "  " '{print $2}' |awk -F "_" '{print $5}')
for fqcode in `cat $md5old`;
do
code=$(echo $fqcode |awk -F"  " '{print $1}')
fqR1=$(echo $fqcode |awk -F"  " '{print $2}' |grep "_R1")
fqR2=$(echo $fqcode |awk -F"  " '{print $2}' |grep "_R2")
fqR3=$(echo $fqcode |awk -F"  " '{print $2}' |grep "_R3")
if [[ "$fqR1" != "" ]] && [[ "$fqR2" == "" ]] && [[ "$fqR3" == "" ]] ;then
fq=$(echo $fqcode |awk -F"  " '{print $2}' |awk -F"_" '{print $('$st')"_R1_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
elif [[ $fqR1 == "" ]] && [[ $fqR2 != "" ]] && [[ "$fqR3" == "" ]] ;then
fq=$(echo $fqcode |awk -F"  " '{print $2}' |awk -F"_" '{print $('$st')"_R2_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
elif [[ "$fqR1" == "" ]] && [[ "$fqR2" == "" ]] && [[ "$fqR3" != "" ]] ;then
fq=$(echo $fqcode |awk -F"  " '{print $2}' |awk -F"_" '{print $('$st')"_R3_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
fi

done
