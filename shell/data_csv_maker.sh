#!/bin/bash
ehco "使用事项：本脚本使用oss数据以/分割的样本名为目录的单层或底层目录"
ehco "不适用于以相同样本名为目录的多层目录，且每层目录都有相同样本数据"

infile=$1
dictcsv=$2
outdir=$3
need_adpater=$4

sed -i "s/\t/,/g" $infile
infilename=$(ls $infile |awk -F "/" '{print $NF}')
rm -f $outdir/${infilename}_tmp
tmp=$outdir/${infilename}_tmp

for info in `cat $infile`;

do
fq=$(echo $info |awk -F "," '{print $2}')
sample=$(echo $info |awk -F "," '{print $1}')
ossinfo=$(echo $info |awk -F "," '{print $2}')
prefix=$(echo $info |awk -F "/" '{print $NF}')
flag=$(ossutil ls $ossinfo  |grep "${prefix}" |grep "_R1_001.fastq.gz" |awk -F " " '{print $NF}')
flagR2=$(ossutil ls $ossinfo  |grep "${prefix}" |grep "_R2_001.fastq.gz" |awk -F " " '{print $NF}')
for file in ${flag[@]};
do
last16=$(echo $file |awk 'BEGIN{FS="'$prefix'"}{print $NF}'|awk -F "" '{print $(NF-15)$(NF-14)$(NF-13)$(NF-12)$(NF-11)$(NF-10)$(NF-9)$(NF-8)$(NF-7)$(NF-6)$(NF-5)$(NF-4)$(NF-3)$(NF-2)$(NF-1)$NF}')
length16=$(echo $file |awk 'BEGIN{FS="'$prefix'"}{print $NF}'|awk -F "" '{print length($0)}')
#echo "$last16"
#echo "$length16"
if [ $length16 == 16 ] && [ $last16 == "_R1_001.fastq.gz" ]; then
if [ -n "$flag" ] && [ -n "$flagR2" ];then
ossdir=$(echo $file |awk -F "_R1_001.fastq.gz" '{print $1}')
echo "${sample},${ossdir}" >> $tmp
else
echo "$flag or $flagR2 is not exsits!!!" 
fi
fi
done
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
