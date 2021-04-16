#!bin/bash
ossdir=$1
outdir=$2
receiver=$3
dfdir="/oss/sz-hapseq/$(echo $ossdir |awk -F "sz-hapseq/" '{print $2}')"

if [ ! -d $outdir ];then
mkdir -p $outdir
fi
if [ ! -f  $outdir/$(echo $outdir |awk -F "/" '{print $NF}')_link_merge.txt ];then
rm -f $outdir/$(echo $outdir |awk -F "/" '{print $NF}')_link_merge.txt
fi
cd $dfdir
for fq in `ls *.gz`;
do 
ossutil -e oss-cn-shenzhen.aliyuncs.com sign ${ossdir}${fq}  --timeout 604800 > $outdir/${fq}_link.txt
sed G $outdir/${fq}_link.txt > $outdir/${fq}_emp_link.txt
cat $outdir/${fq}_emp_link.txt |head -n 1 >> $outdir/$(echo $outdir |awk -F "/" '{print $NF}')_link_merge.txt
done
cd $outdir
ossutil cp -ru ${ossdir}MD5/ .
cat $(echo $ossdir |awk -F "sz-hapseq/" '{print $2}')MD5/*.md5 > md5
ossutil cp -ru md5 ${ossdir}
ossutil -e oss-cn-shenzhen.aliyuncs.com sign ${ossdir}md5 --timeout 604800 > md5_link.txt
sed G md5_link.txt  > md5_emp_link.txt
cat md5_emp_link.txt |head -n 1 >> $(echo $outdir |awk -F "/" '{print $NF}')_link_merge.txt
rm -rf goodfq *link.txt
#if [ -f /data/users/wuliuyu/wuliuyu/python/sendemail.py ]; then
#python /data/users/wuliuyu/wuliuyu/python/sendemail.py -p ${pid} -f $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt -r $receiver
#fi
#if [ -f /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail.py ]; then
#python /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail.py -p ${pid} -f $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt -r $receiver
#fi
python /data/users/hapseq/tmp/single_link_shell/sendemail.py -p $(echo $outdir |awk -F "/" '{print $NF}') -f  $outdir/$(echo $outdir |awk -F "/" '{print $NF}')_link_merge.txt -r $recei    ver
