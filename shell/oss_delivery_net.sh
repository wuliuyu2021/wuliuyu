#!/bin/bash

infile=$1
outdir=$2
receiver=$3

time=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')

sed -i "s/\t/,/g" $infile

sed -i "s/LIEbing/novelbio/g" $infile
sed -i "s/SHANGhaiouyi/oebiotech/g" $infile
sed -i "s/FUjun/fulgent/g" $infile

infilename=$(ls $infile |awk -F "/" '{print $NF}')
rm -f $outdir/${infilename}_tmp
tmp=$outdir/${infilename}_tmp

for info in `cat $infile `

do
contact=$(echo $info |awk -F "," '{print $1}')
flag=$(echo $info |awk -F "," '{print $2}')
ossdir=$(ossutil ls  $info |tail -n 4 |head -n 1 |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
echo "${contact},${flag},${ossdir}_R1_001.fastq.gz" >> $tmp
echo "${contact},${flag},${ossdir}_R2_001.fastq.gz" >> $tmp
done

for info2 in `cat $tmp`
do
fq=$(echo $info2 |awk -F "," '{print $3}')
contact2=$(echo $info2 |awk -F "," '{print 3}')
flag2=$(echo $info2 |awk -F "," '{print 2}')
ossutil cp -ru $fq oss://sz-hapdeliver/${flag2}/$time/${contact2}/
echo $fq uploaded to oss://sz-hapdeliver/${flag2}/$time/${contact2}/
done

un=$(cat $tmp |awk -F"," '{print $2","$1}' |sort |uniq)
for info3 in `cat $un`
do
flag3=$(echo $info3 |awk -F "," '{print $1}')
contact3=$(echo $info3 |awk -F "," '{print $2}')
python /data/users/wuliuyu/wuliuyu/python/dingtalkChatbot.py oss://sz-hapdeliver/$flag3/$time/$contact3 $receiver
