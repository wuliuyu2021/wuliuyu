#!bin/bash
echo ;date

snp_dir=$1
outdir=$2

sd=$outdir/plink/snp
sr=$outdir/plink/result

mkdir -p $sd
mkdir -p $sr
cp $snp_dir/*/*/*_snp.vcf $sd/
rename _snp .snp $sd/*vcf
cd $sd
for snp in `ls *vcf`;
do
prefix1=$(echo $snp |awk -F ".snp.vcf" '{print $1}')
num=$(echo $snp |awk -F"_" '{print NF}')
if [ $num == 1 ];then
s1=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $1}')
s2=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $2}')
prefix2=$(echo $s1"."$s2)
fi
if [ $num == 2 ];then
s1=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $1}')
s2=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $2}')
s3=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $3}')
prefix2=$(echo $s1"."$s2"."$s3)
fi
if [ $num == 3 ];then
s1=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $1}')
s2=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $2}')
s3=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $3}')
s4=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $4}')
prefix2=$(echo $s1"."$s2"."$s3"."$s4)
fi
if [ $num == 4 ];then
s1=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $1}')
s2=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $2}')
s3=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $3}')
s4=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $4}')
s5=$(echo $snp |awk -F".snp.vcf" '{print $1}' |awk -F "_" '{print $5}')
prefix2=$(echo $s1"."$s2"."$s3"."$s4"."$s5)
fi
sed -i "s/${prefix1}/${prefix2}/g" $snp
bgzip $snp
/thinker/nfs5/public/wuliuyu/Hapcolud_docker/bcftoolsVariant/bcftools-1.12/bcftools index ${prefix1}.snp.vcf.gz
done

ls $sd/*snp.vcf.gz | tr "\n" " " > $sr/info.csv
#info_maf = $(echo $info)
/thinker/nfs5/public/wuliuyu/Hapcolud_docker/bcftoolsVariant/bcftools-1.12/bcftools merge -o $sr/all.vcf.gz $(cat $sr/info.csv)

less $sr/all.vcf.gz |sed 's/\s\.\/\.:\.:\./\t0\/0:\.:\./g' | awk '{if($1~/^#CHROM/){for(m=10;m<=NF;m++){if($m~/\//){match($m,/.*\/(.*.bam)/,a)}else{a[1]=$m}; b=b"\t"a[1]};print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7"\t"$8"\t"$9b}else{print $0}}' > $sr/all.vcf
cd $sr
/thinker/nfs5/public/tools/plink_soft/plink --const-fid --vcf $sr/all.vcf --make-bed -out ./plink 
/thinker/nfs5/public/tools/plink_soft/plink --bfile ./plink --genome 

perl /thinker/nfs5/public/wuliuyu/wuliuyu/plink/plink_heatmap.pl ./plink.genome ./
