#!/bin/bash
outdir=$1
name=$2

echo;date;echo "fq to fa"
awk '{if(NR%4 == 1){print ">" substr($0, 2)}}{if(NR%4 == 2){print}}' $outdir/${name}.fastq >  $outdir/${name}.fa
echo;date;echo "blastn map"
/data/users/hapseq/tools/ncbi-blast-2.13.0+/bin/blastn -outfmt 6 -evalue 1e-5 -max_target_seqs 10 -num_threads 8 -db /data/users/hapseq/tools/NT/blast_index/nt -out $outdir/${name}.fa.m8 -query  $outdir/${name}.fa
echo;date;echo "filter best blast result"
perl -ne 'BEGIN{%hash}@l=split/\t/;if(!$hash{$l[0]}){print;$hash{$l[0]}=1;}' $outdir/${name}.fa.m8 >  $outdir/${name}.best.m8
echo;date;echo "get all species blast info"
ls $outdir/${name}.best.m8 > $outdir/${name}.m8.list
perl /data/users/hapseq/tools/NT/get_tax.pl $outdir/${name}.m8.list
#ls $outdir/${name}.tax.xls > tax.list
#perl stat.pl tax.list
#echo;date
#perl get_untax_reads.pl $outdir/${name}.tax.xls $outdir/${name}.fa $outdir/${name}.tax_reads.fa $outdir/${name}.untax_reads.fa
echo;date;echo "stat all species mapped reads number"
perl -e 'while(<>){@aa=split/\t/;@bb=split/;/,$aa[1];print "$bb[7]\n";}' $outdir/${name}.tax.xls|awk '{print $0}' -|sort|uniq -c |sort -nr > $outdir/${name}_reads_stat.xls
echo;date
