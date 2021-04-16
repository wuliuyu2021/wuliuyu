#!/bin/bash
dir=$1
fastq=$2
test=$(echo $fastq|awk '{split($0,c,".");print c[1]}')
echo;date;echo "fq to fa"
cd $dir
awk '{if(NR%4 == 1){print ">" substr($0, 2)}}{if(NR%4 == 2){print}}' ./${test}.fastq >  ./${test}.fa
echo;date;echo "blastn map"
/thinker/nfs3/public/yelei/software/ncbi-blast-2.7.1+/bin/blastn -outfmt 6 -evalue 1e-5 -max_target_seqs 10 -num_threads 8 -db /thinker/nfs3/public/zhangjing/Database/NT/blast_index/nt -out ${test}.fa.m8 -query ./${test}.fa
echo;date;echo "filter best blast result"
perl -ne 'BEGIN{%hash}@l=split/\t/;if(!$hash{$l[0]}){print;$hash{$l[0]}=1;}' ${test}.fa.m8 >${test}.best.m8
echo;date;echo "get all species blast info"
ls ./${test}.best.m8 >${test}.m8.list
perl /thinker/nfs3/public/yelei/Project/20180613F4A2-5_contaminated_20180814/get_tax.pl ${test}.m8.list
#ls ${test}.tax.xls > tax.list
#perl stat.pl tax.list
#echo;date
#perl get_untax_reads.pl ${test}.tax.xls ${test}.fa ${test}.tax_reads.fa ${test}.untax_reads.fa
echo;date;echo "stat all species mapped reads number"
perl -e 'while(<>){@aa=split/\t/;@bb=split/;/,$aa[1];print "$bb[7]\n";}' ${test}.tax.xls|awk '{print $0}' -|sort|uniq -c |sort -nr >${test}_reads_stat.xls
echo;date
