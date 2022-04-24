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
echo "Result URL"
ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/生信科研部_all_data/科服项目数据释放/$ossdir/$result  --timeout 1296000
