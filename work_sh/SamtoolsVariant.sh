#!/bin/bash
#indir=$1
outdir=$1
gtf=$2

#human hg38 /thinker/nfs5/public/laigr/data/hg38/GRCh38_Ensembl91/ChromFa/Homo_sapiens.GRCh38.91.dna.primary_assembly.fa
#mouse mm10 /thinker/nfs5/public/laigr/data/mm10/10090/GRCm38_93/ChromFa/chrAll.fa
#rat rat6.0 /thinker/nfs5/public/laigr/data/ensemble_rnor6.0/ChromFa/new.Rattus_norvegicus.Rnor_6.0.dna.toplevel.fa
#cp -f $indir/*sorted.rmdup.bam $outdir
find $outdir -type f -name "*bam" | awk -F'/' '{match($NF,/(.*).sorted.rmdup.bam/,a)
print "mkdir "a[1]"  && /thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools mpileup -d 10000 -q 5 -Q 13 -C 50 -m 2 -F 0.002 -f '$gtf' -a \"DP,AD,ADF,ADR,SP,AD,ADF,ADR\"  "$0" | /thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools call -O v -v -c -o "a[1]"/"a[1]".vcf &&    /thinker/nfs4/public/liyq/soft/bcftools/bin/bcftools filter -O v -s FLTER -i '\''%QUAL > 20 && INFO/DP > 4 && MQ > 30'\'' "a[1]"/"a[1]".vcf > "a[1]"/"a[1]".tmp.vcf && perl /thinker/nfs4/public/liyq/temp/wuliuyu/SamtoolsVariant/PASS_snp_indel.pl "a[1]"/"a[1]".tmp.vcf "a[1]"/"a[1]".filit.vcf "a[1]"/"a[1]"_snp.vcf "a[1]"/"a[1]"_indel.vcf &"
}'
