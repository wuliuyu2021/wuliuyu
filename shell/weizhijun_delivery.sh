#!/bin/bash

indir=$1

tm=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
piddir=$(echo $indir | awk -F "/" '{print $NF}')
cd $indir
for fqR1 in `ls *_R1_*`
do
prefix=$(echo $fqR1 |awk -F "_R1_" '{print $1}')
mkdir -p $prefix
mv ${prefix}_* $prefix
done
rename _R1_001 _1 */*gz
rename _R2_001 _2 */*gz
