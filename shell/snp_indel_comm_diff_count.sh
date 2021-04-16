#!/bin/bash

indir=$1
gv=$2

cd $indir

for dir in `ls -d *-*`;
do 
comm_diff="$dir/Common_Different_summary_multianno.xls" 
nrows_snp=$(less $dir/All_common_snp.anno.vcf.${gv}_multianno.xls | grep "chr" |wc -l)
nrows_indel=$(less $dir/All_common_indel.anno.vcf.${gv}_multianno.xls | grep "chr" |wc -l)
echo "common	$nrows_snp	$nrows_indel"
echo "Sample	Snp	Indel" > $comm_diff
echo "common	$nrows_snp	$nrows_indel" >> $comm_diff
	for sdif in `ls $dir/*snp.anno.vcf.${gv}_multianno.diff.xls`;
	do
	path=$(ls $sdif |awk -F "/" '{print $1}')
	prefix=$(ls $sdif |awk -F "/" '{print $2}' |awk -F "_snp.anno.vcf.${gv}_multianno.diff.xls" '{print $1}')
 	sdif_snp=$(less $sdif | grep "chr" |wc -l)
	sdif_indel=$(less $path/${prefix}_indel.anno.vcf.${gv}_multianno.diff.xls | grep "chr" |wc -l)
	echo "$prefix	$sdif_snp	$sdif_indel" >> $comm_diff
	done
done