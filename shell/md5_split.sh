#!/bin/bash

md5old=$1
out=$2
st=$3

md5name=$(ls $md5old |awk -F"/" '{print $NF}')
rm -f $out/${md5name}_new
if [ ! -d $out ];then
mkdir -p $out
fi
tmp=$out/${md5name}_new
sed 's/  /CD==FQ/g' $md5old > $tmp
for fqcode in `cat $tmp`;
do
code=$(echo $fqcode |awk -F"CD==FQ" '{print $1}')
fqR1=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |grep "_R1")
fqR2=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |grep "_R2")
fqR3=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |grep "_R3")
if [[ -n "$fqR1" ]] && [[ -z "$fqR2" ]] && [[ -z "$fqR3" ]];then
fq=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |awk -F"_" '{print $('$st')"_R1_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
elif [[ -z "$fqR1" ]] && [[ -n "$fqR2" ]] && [[ -z "$fqR3" ]];then
fq=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |awk -F"_" '{print $('$st')"_R2_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
elif [[ -z "$fqR1" ]] && [[ -z "$fqR2" ]] && [[ -n "$fqR3" ]] ;then
fq=$(echo $fqcode |awk -F"CD==FQ" '{print $2}' |awk -F"_" '{print $('$st')"_R3_001.fastq.gz"}')
echo "$code  $fq" >> $out/${md5name}_new
echo "$code  $fq"
fi
rm -f $tmp
done
