#!/bin/bash

infile=$1
dictcsv=$2
outdir=$3
need_adpater=$4

sed -i "s/\t/,/g" $infile
infilename=$(ls $infile |awk -F "/" '{print $NF}')
rm -f $outdir/${infilename}_tmp
tmp=$outdir/${infilename}_tmp

for info in `cat $infile`

do
fq=$(echo $info |awk -F "," '{print $2}')
sample=$(echo $info |awk -F "," '{print $1}')
prefix=$(echo $info |awk -F "/" '{print $NF}')
ifno=$(ossutil ls  $fq |grep "${prefix}_R1_001.fastq.gz" )

if [ "$ifno" == "" ];then
ossdir=$(ossutil ls  $fq |tail -n 4 |head -n 1 |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
echo "${sample},${ossdir}" >> $tmp
else
ossdir=$(ossutil ls  $fq |grep "${prefix}_R1_001.fastq.gz" |awk -F "_R1_001.fastq.gz" '{print $1}' |awk -F "oss" '{print "oss"$2}' )
echo "${sample},${ossdir}" >> $tmp
fi
done
if [ $need_adpater == "no" ];then
if [ -f "/data/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /data/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir
fi
if [ -f "/thinker/nfs5/public/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir
fi
if [ -f "/haplox/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /haplox/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir
fi
elif [ $need_adpater == "IDT" ] || [ $need_adpater == "UPM" ] ||[ $need_adpater == "MGI" ];then
if [ -f "/data/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /data/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir -a $need_adpater
fi
if [ -f "/thinker/nfs5/public/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir -a $need_adpater
fi
if [ -f "/haplox/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py" ];then
python /haplox/users/wuliuyu/wuliuyu/python/kefu_fastp_merge_csv_info_v2.py -i $tmp -t $dictcsv -o $outdir -a $need_adpater
fi
else
echo "Sorry, your parameter is wrong!!!" \
&& exit 0
fi
