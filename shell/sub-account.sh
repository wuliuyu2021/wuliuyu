#!/bin/bash

indir=$1
client=$2
project_man=$3


tm=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
piddir=$(echo $indir | awk -F "/" '{print $NF}')

cd $indir

ossutil cp -ru ${indir}/ oss://sz-hapdeliver/${client}/${tm}/${piddir}/

python /data/users/wuliuyu/wuliuyu/python/dingtalkChatbot.py ${client}:\ oss://sz-hapdeliver/${client}/${tm}/${piddir}/ $project_man