#!/bin/bash
gtf_file=$1
network_dir=$2
outdir=$3 

awk -F "\t"  '$3~/transcript/' $gtf_file |awk -F "\t" '{print $NF}' |awk -F "; " '{print $2"\t"$3}' > $outdir/transcript_gene.xls
sed -i "s/transcript_id //g" $outdir/transcript_gene.xls

sed -i "s/gene_name //g" $outdir/transcript_gene.xls

sed -i "s/\"//g" $outdir/transcript_gene.xls

sed -i "/MSTRG./d" $outdir/transcript_gene.xls

python3 /thinker/nfs5/public/wuliuyu/wuliuyu/python/network_trans_to_gene.py $outdir/transcript_gene.xls $network_dir $outdir
echo "Done"
