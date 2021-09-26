#!/bin/bash

md5=$1
outdir=$2

md5dir=$outdir/MD5

mkdir -p $md5dir

sed "s/ /==/g" $md5 > $outdir/md5_new

for info in `cat $outdir/md5_new`;
do
code=$(echo $info |awk -F "====" '{print $1}')
sample=$(echo $info |awk -F "====" '{print $2}')
echo "$code  $sample" > $md5dir/${sample}.md5
done
rm -f $outdir/md5_new
rm -f $md5
