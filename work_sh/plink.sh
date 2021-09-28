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

less $sr/all.vcf.gz |sed 's/\s\.\/\.:\.:\./\t0\/0:\.:\./g' > $sr/all.vcf 

/thinker/nfs5/public/tools/plink_soft/plink --const-fid --vcf $sr/all.vcf --make-bed -out $sr/plink 
/thinker/nfs5/public/tools/plink_soft/plink --bfile $sr/plink --genome
