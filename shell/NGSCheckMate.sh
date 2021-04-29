#!/bin/bash
echo;date
vcfdir=$1
outdir=$2
rm -f $outdir/list
if [ ! -d $outdir/ngscheckmate ];then
mkdir -p $outdir/ngscheckmate
fi
for vcfd in `ls -d $vcfdir/*`

do
sample = $(echo $vcfd |awk -F"/" '{print $NF}')
sample_vcf=${vcfd}/${sample}.vcf
echo $sample_vcf >> $outdir/list
done
/usr/bin/python /thinker/nfs5/public/laigr/bin/NGSCheckMate/ncm.py -V -f  -l $outdir/list -N NAG -bed /thinker/nfs5/public/laigr/bin/NGSCheckMate/SNP/SNP_GRCh37_hg19_woChr.bed -O $outdir/ngscheckmate
echo;date