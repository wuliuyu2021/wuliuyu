#!/bin/bash
indir=$1
outdir=$2
num=$3
blast_num=$4

sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/2W_reads_split.sh $indir $outdir $num
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/blast_muti.py $outdir $blast_num
sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/top3_blast_result.sh $outdir
