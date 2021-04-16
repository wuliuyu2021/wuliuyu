#!/bin/bash

infile=$1
outdir=$2
ossdir2=$3
receiver=$4
#sed -i "s/\t/,/g" $infile
rm -f $outdir/*tmp
infilename=$(ls $infile |awk -F "/" '{print $NF}')
tmp=$outdir/${infilename}_tmp

for info in `cat $infile`

do
#fq=$(echo $info |awk -F "," '{print $2}')
#sample=$(echo $info |awk -F "," '{print $1}')
ossdir=$(ossutil ls  $info |tail -n 4 |head -n 1 |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
echo "${ossdir}_R1_001.fastq.gz" >> $tmp
echo "${ossdir}_R2_001.fastq.gz" >> $tmp
done

for fq in `cat $tmp`
do
ossutil cp -ru $fq $ossdir2$(echo $fq |awk -F "/" '{print $NF}')
echo $fq upload to $ossdir2$(echo $fq |awk -F "/" '{print $NF}')
done
python /data/users/wuliuyu/wuliuyu/python/dingtalkChatbot.py $ossdir2 $receiver
