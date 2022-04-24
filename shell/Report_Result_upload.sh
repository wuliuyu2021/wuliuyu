#!/bin/bash

indir=$1
ossdir=$(echo $indir |awk -F "/" '{print $NF}')

report=$(ls HGC*_report.tar.gz)
result=Result.tar.gz

cd $indir

ossutil cp -ru $report oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/
ossutil cp -ru $result oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/
#echo "Report URL"
echo "Hi all, "
reportsign=$(ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$report  --timeout 1296000 |head -n1)
#flag="oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/"
report_m=$(ossutil ls oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$report | grep "report" |awk -F " " '{print $5}')
lv1=`echo "scale=0; ${report_m}/1024/1024" |bc`
#echo "${lv1}M"
echo " "
echo "该项目的分析结题报告已上传至阿里云，请注意查收~"
echo " "
echo "下载链接: "
#echo "Result URL"
#ossutil ls oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$result 
resulttsign=$(ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$result  --timeout 1296000 |head -n1)
result_m=$(ossutil ls oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$result  | grep "Result" |awk -F " " '{print $5}')
#echo "$result_m"
lv2=`echo "scale=0; ${result_m}/1024/1024" |bc`
#echo "${lv2}M"
echo "$reportsign"
echo " "
echo "Result.tar.gz: "
echo "$resulttsign"
echo " "
echo "文件大小: ${lv1} M & ${lv2} M"
echo "下载期限: 15d"
echo " "
echo "祝好!"
