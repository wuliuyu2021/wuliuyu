#!/bin/bash
# zhoujia@haplox.com
# tongqn@haplox.com
# fanxh@haplox.com
# xiayb@haplox.com
# linlong@haplox.com
# zhouqian@haplox.com
# oss://delivery-data/s345/
piddir=$1
receiver=$2
#`date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}'`
tm=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
cd $piddir
pid=$(pwd | awk -F "/" '{print $NF}')
#echo $tm
tar -cf ${pid}.tar *
coscli cp ${pid}.tar cos://sz-hapdeliver/Kefu_Data_hapdeliver/${tm}/${pid}.tar && coscli signurl cos://sz-hapdeliver/Kefu_Data_hapdeliver/${tm}/${pid}.tar  --time 604800 |grep 'https' |awk -F 'https' '{print "https"$NF}' > ${pid}_link.txt
if [ -f /data/users/wuliuyu/wuliuyu/python/sendemail_single_file.py ]; then
python /data/users/wuliuyu/wuliuyu/python/sendemail_single_file.py -p ${pid} -f ${pid}_link.txt -r $receiver
fi
if [ -f /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail_single_file.py ]; then
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail_single_file.py -p ${pid} -f ${pid}_link.txt -r $receiver
fi
