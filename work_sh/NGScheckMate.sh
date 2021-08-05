#!/bin/bash
indir=$1
outdir=$2
type=$3 #vcf,fastq
Chr_bed=$4
#/thinker/nfs5/public/laigr/bin/NGSCheckMate/SNP/SNP.pt
#/thinker/nfs5/public/laigr/bin/NGSCheckMate/SNP/SNP_GRCh38_hg38_wChr.bed
if [ $type == "vcf" ];then
ls $indir/*/*snp.vcf > $outdir/list
/usr/bin/python /thinker/nfs5/public/laigr/bin/NGSCheckMate/ncm.py -V -f  -l $outdir/list -N NAG -bed $Chr_bed -O $outdir/NGSCheckMate
fi

if [ $type == "fastq" ];then
for fq in `ls *_R1_001.fastq.gz`;
do
sam_name=$(echo $fq |awk -F "/" '{print $NF}' |awk -F "_R1_001.fastq.gz" '{print $1}')
R2=$(echo $fq |awk -F "_R1_001.fastq.gz" '{print $1}')_R2_001.fastq.gz
echo "$fq	$R2	$sam_name" >> $outdir/list
/usr/bin/python /thinker/nfs5/public/laigr/bin/NGSCheckMate/ncm_fastq.py -l $outdir/list -O $outdir/NGSCheckMate -pt $Chr_bed -p 4 -N NGS
done
fi
