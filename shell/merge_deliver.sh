#!bin/bash
tardir=$1
receiver=$2
#link=$3
tm=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
cd $tardir
rm -f $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt
pid=$(pwd | awk -F "/" '{print $NF}')
ossutil cp -ru ./ oss://sz-hapdeliver/Kefu_Data_hapdeliver/${tm}/${pid}/
for fq in `ls *.gz`;
do 
ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/Kefu_Data_hapdeliver/${tm}/${pid}/${fq}  --timeout 604800 > ${fq}_link.txt
sed G ${fq}_link.txt > ${fq}_emp_link.txt
cat ${fq}_emp_link.txt |head -n 1 >> $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt
done
ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/Kefu_Data_hapdeliver/${tm}/${pid}/md5 --timeout 604800 > md5_link.txt
sed G md5_link.txt  > md5_emp_link.txt
cat md5_emp_link.txt |head -n 1 >> $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt
rm *link.txt
if [ -f /data/users/wuliuyu/wuliuyu/python/sendemail.py ]; then
python /data/users/wuliuyu/wuliuyu/python/sendemail.py -p ${pid} -f $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt -r $receiver
fi
if [ -f /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail.py ]; then
python /thinker/nfs5/public/wuliuyu/wuliuyu/python/sendemail.py -p ${pid} -f $(echo ${tardir} |awk -F "/" '{print $NF}')_link_merge.txt -r $receiver
fi