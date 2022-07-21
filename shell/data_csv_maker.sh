#!/bin/bash
echo "使用事项：本脚本使用oss数据以/分割的样本名为目录的单层或底层目录"
echo "不适用于以相同样本名为目录的多层目录，且每层目录都有相同样本数据"

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
#length16=$(echo $file |awk 'BEGIN{FS="'$prefix'"}{print $NF}'|awk -F "" '{print length($0)}')
#echo "$last16"
#echo "$length16"
if [ $last16 == "_R1_001.fastq.gz" ]; then
flam=$(ossutil ls $file  |grep "${prefix}" |grep "_R1_001.fastq.gz" |awk -F " " '{print $NF}')
if [ -n "$flag" ] && [ -n "$flagR2" ];then
ossdir=$(echo $flam |awk -F "_R1_001.fastq.gz" '{print $1}')
echo "${sample},${ossdir}" >> $tmp
else
echo "$flag or $flagR2 is not exsits!!!" 
fi
else
echo "$sample,$flam is not in data.csv, please check!!!"
fi
done
done
#验证rawcsv和tmpcsv行数是否一致;
rawwc=$(less $infile |wc -l )
tmpwc=$(less $tmp |wc -l )
if [ "$rawwc" == "$tmpwc" ]; then
echo "${infile} 行数：$rawwc 等于 ${tmp} 行数：$tmpwc !"
else 
echo -e "\e[41m ${infile} 行数：$rawwc 不等于 ${tmp} 行数：$tmpwc, 请检查oss路径下是否存在多个前缀开始的数据 \e[0m" && exit 0
fi

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
echo -e "\e[41m Sorry, your parameter is wrong!!! \e[0m" \
&& exit 0
fi
