#!/bin/bash
indir=$1

cd $indir
header="样本	比对物种Top1	read数	占比(%s)	比对物种Top2	read数	占比(%s)	比对物种Top3	read数	占比(%s)"
echo "$header" > top3_spe.csv
for spe in `ls *_reads_stat.xls`;
do
specie1=$(cat $spe |head -n 2 |tail -n 1 |awk -F " s__" '{print $2}')
nums1=$(cat $spe |head -n 2 |tail -n 1 |awk -F " s__" '{print $1}')
lv1=`echo "scale=4; ${nums1}*100/$(cat $spe |head -n 1)" |bc`

specie2=$(cat $spe |head -n 3 |tail -n 1 |awk -F " s__" '{print $2}')
nums2=$(cat $spe |head -n 3 |tail -n 1 |awk -F " s__" '{print $1}')
lv2=`echo "scale=4; ${nums2}*100/$(cat $spe |head -n 1)" |bc`

specie3=$(cat $spe |head -n 4 |tail -n 1 |awk -F " s__" '{print $2}')
nums3=$(cat $spe |head -n 4 |tail -n 1 |awk -F " s__" '{print $1}')
lv3=`echo "scale=4; ${nums3}*100/$(cat $spe |head -n 1)" |bc`

prefix=$(echo $spe |awk -F "_reads_stat.xls" '{print $1}')
echo "$prefix	$specie1	$nums1	$lv1	$specie2	$nums2	$lv2	$specie3	$nums3	$lv3"	>> top3_spe.csv
done