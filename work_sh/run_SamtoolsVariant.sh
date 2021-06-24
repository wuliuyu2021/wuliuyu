#!/bin/bash
indir=$1
outdir=$1
gtf=$3

#human hg38 /thinker/nfs5/public/laigr/data/hg38/GRCh38_Ensembl91/ChromFa/Homo_sapiens.GRCh38.91.dna.primary_assembly.fa
#mouse mm10 /thinker/nfs5/public/laigr/data/mm10/10090/GRCm38_93/ChromFa/chrAll.fa
#rat rat6.0 /thinker/nfs5/public/laigr/data/ensemble_rnor6.0/ChromFa/new.Rattus_norvegicus.Rnor_6.0.dna.toplevel.fa
echo "cp *sorted.rmdup.bam to $indir: start"
cp -f $indir/*sorted.rmdup.bam $outdir
echo "cp *sorted.rmdup.bam to $indir: done"
sh /thinker/nfs5/public/wuliuyu/wuliuyu/work_sh/SamtoolsVariant.sh $outdir $gtf > $outdir/run_bcftools.sh