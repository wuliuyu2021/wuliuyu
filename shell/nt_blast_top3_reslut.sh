#!/bin/bash

indir=$1
fqdir=$2
sp_flag=$3

cd $indir

sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/2W_reads_split.sh $fqdir $indir  $sp_flag

python /thinker/nfs5/public/wuliuyu/wuliuyu/python/blast_muti.py $indir 4

sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/top3_blast_result.sh $indir