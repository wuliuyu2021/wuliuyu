#!/bin/bash
indir=$1
outdir=$2
gtf=$3
samtoolsVariantdir=$4

echo "#human hg38 /thinker/nfs5/public/laigr/data/hg38/GRCh38_Ensembl91/ChromFa/Homo_sapiens.GRCh38.91.dna.primary_assembly.fa"
echo "#mouse mm10 /thinker/nfs5/public/laigr/data/mm10/10090/GRCm38_93/ChromFa/chrAll.fa"
echo "#rat rat6.0 /thinker/nfs5/public/laigr/data/ensemble_rnor6.0/ChromFa/new.Rattus_norvegicus.Rnor_6.0.dna.toplevel.fa"
cp -f $indir/*sorted.rmdup.bam $outdir
for sorted_rmdup_bam in `ls $outdir/*sorted.rmdup.bam`;
do
sampledir=$(echo $sorted_rmdup_bam |awk -F "/" '{print $NF}' |awk -F ".sorted.rmdup.bam" '{print $1}')
if [ ! -d $sampledir ];then
mkdir -p $outdir/$sampledir
fi
echo "/thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools mpileup -d 10000 -q 5 -Q 13 -C 50 -m 2 -F 0.002 -f $gtf -a \"DP,AD,ADF,ADR,SP,AD,ADF,ADR\" $sorted_rmdup_bam | /thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools call -O v -v -c -o $outdir/$sampledir/${sampledir}.vcf && /thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools filter -O v -s FLTER -i '%QUAL > 20 && DP > 4 && MQ > 30' $outdir/${sampledir}/${sampledir}.vcf > $outdir/${sampledir}/${sampledir}.tmp.vcf && perl /thinker/nfs4/public/liyq/temp/wuliuyu/SamtoolsVariant/PASS_snp_indel.pl $outdir/${sampledir}/${sampledir}.tmp.vcf $outdir/${sampledir}/${sampledir}.filit.vcf $outdir/${sampledir}/${sampledir}_snp.vcf $outdir/${sampledir}/${sampledir}_indel.vcf &" >> $outdir/run_bcftoolsVariant.sh

done
echo "sh $outdir/run_bcftoolsVariant.sh"
echo "wait" >> $outdir/run_bcftoolsVariant.sh
echo "rm -f $outdir/*bam" >> $outdir/run_bcftoolsVariant.sh
echo "expect /thinker/nfs5/public/wuliuyu/wuliuyu/work_sh/expect_bcftools.exp ${outdir}/ $samtoolsVariantdir" >> $outdir/run_bcftoolsVariant.sh
echo "cmd done"
