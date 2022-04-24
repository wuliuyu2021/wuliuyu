#!/bin/bash

indir=$1
ossdir=$(echo $indir |awk -F "/" '{print $NF}')

report=HGC*_report.tar.gz
result=Result.tar.gz

cd $indir

ossutil cp -ru $report oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/
ossutil cp -ru $result oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/

echo "Report URL"
ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$report  --timeout 1296000
report_m=$(ossutil ls oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$report | grep "report" |awk -F " " '{print $5}')
lv1=`echo "scale=4; ${report_m}/1024/1024" |bc`
echo "${lv1}M"
echo " "
echo " "
echo "Result URL"
ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$result  --timeout 1296000
result_m=$(ossutil ls oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$report | grep "Result" |awk -F " " '{print $5}')
lv2=`echo "scale=4; ${result_m}/1024/1024" |bc`
echo "${lv2}M"
