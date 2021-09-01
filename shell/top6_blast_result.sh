#!/bin/bash
indir=$1

cd $indir
header="样本	比对物种Top1	read数	占比(%s)	比对物种Top2	read数	占比(%s)	比对物种top3	read数	占比(%s)	比对物种top4	read数	占比(%s)	比对物种top5	read数	占比(%s)	比对物种top6	read数	占比(%s)"
echo "$header" > top6_spe.xls
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

specie4=$(cat $spe |head -n 5 |tail -n 1 |awk -F " s__" '{print $2}')
nums4=$(cat $spe |head -n 5 |tail -n 1 |awk -F " s__" '{print $1}')
lv4=`echo "scale=4; ${nums4}*100/$(cat $spe |head -n 1)" |bc`

specie5=$(cat $spe |head -n 6 |tail -n 1 |awk -F " s__" '{print $2}')
nums5=$(cat $spe |head -n 6 |tail -n 1 |awk -F " s__" '{print $1}')
lv5=`echo "scale=4; ${nums5}*100/$(cat $spe |head -n 1)" |bc`

specie6=$(cat $spe |head -n 7 |tail -n 1 |awk -F " s__" '{print $2}')
nums6=$(cat $spe |head -n 7 |tail -n 1 |awk -F " s__" '{print $1}')
lv6=`echo "scale=4; ${nums6}*100/$(cat $spe |head -n 1)" |bc`

prefix=$(echo $spe |awk -F "_reads_stat.xls" '{print $1}')
echo "$prefix	$specie1	$nums1	$lv1	$specie2	$nums2	$lv2	$specie3	$nums3	$lv3	$specie4	$nums4	$lv4	$specie5	$nums5	$lv5	$specie6	$nums6	$lv6"	>> top6_spe.xls
done
