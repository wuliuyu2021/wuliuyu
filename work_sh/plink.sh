#!bin/bash
echo ;date

snp_dir=$1
outdir=$2

sd=$outdir/plink/snp
sr=$outdir/plink/result

mkdir -p $sd
mkdir -p $sr

for snp in `ls $snp_dir/*/*/*_snp.vcf`;
do
sample=$(echo $snp |awk -F "/" '{print $NF}')
bgzip -c $snp > $sd/${sample}.gz
/thinker/nfs5/public/wuliuyu/Hapcolud_docker/bcftoolsVariant/bcftools-1.12/bcftools index $sd/${sample}.gz
done

ls $sd/*_snp.vcf.gz | tr "\n" " " > $sr/info.csv
#info_maf = $(echo $info)
/thinker/nfs5/public/wuliuyu/Hapcolud_docker/bcftoolsVariant/bcftools-1.12/bcftools merge -o $sr/all.vcf.gz $(cat $sr/info.csv)

less $sr/all.vcf.gz |sed 's/\s\.\/\.:\.:\./\t0\/0:\.:\./g' | awk '{if($1~/^#CHROM/){for(m=10;m<=NF;m++){if($m~/\//){match($m,/.*\/(.*.bam)/,a)}else{a[1]=$m}; b=b"\t"a[1]};print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7"\t"$8"\t"$9b}else{if($1!~/ID=KI|ID=GL|^KI|^GL/)print $0}}' > $sr/all.vcf

cd $sr
/thinker/nfs5/public/tools/plink_soft/plink --const-fid --vcf $sr/all.vcf --make-bed -out ./plink
/thinker/nfs5/public/tools/plink_soft/plink --bfile ./plink --genome
