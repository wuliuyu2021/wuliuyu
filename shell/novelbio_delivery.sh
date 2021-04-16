#!/bin/bash

indir=$1
needmd5=$2

tm=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
piddir=$(echo $indir | awk -F "/" '{print $NF}')
cd $indir
if [ $needmd5 == "y" ];then
for fq in `ls *gz`;
do 
md5sum $fq > ${fq}.md5
done
fi
if [ $needmd5 == "n" ];then
echo "md5files exists!!!"
fi
cd ..
ossutil cp -ru ${piddir}/ oss://sz-hapdeliver/novelbio/${tm}/${piddir}/

echo "${indir} uploaded to oss://sz-hapdeliver/novelbio/${tm}/${piddir}/ done"
