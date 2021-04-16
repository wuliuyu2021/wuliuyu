#!/bin/bash

dir=$1

cd $dir

for xl in `ls *anno*xls`;
do
prefix=$(ls $xl | awk -F ".anno." '{print $1}')
less $xl | awk -F "\t" '{print $7}' > ${prefix}.anno.txt
echo "$dir/${prefix}.anno.txt"
done 
