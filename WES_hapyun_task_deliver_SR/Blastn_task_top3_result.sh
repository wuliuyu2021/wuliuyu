#!/bin/bash
csv=$1 #1.csv文件
yinshe=$2 #字典对应表
outdir=$3 #data.csv生成路径
contact=$4 #项目编号
Hapyun_account=$5 #Hapyun账号选择

time=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
hms=$(date "+%Y%m%d_%H%M%S" | awk -F "" '{print $3$4$5$6$7$8$9$10$11$12$13$14$15}')

sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/data_csv_maker.sh $csv $yinshe $outdir no

if [ -e $outdir/data.csv ];then
instance=$(cat $outdir/data.csv |wc -l) #Hapyun执行工具或流的并发数
echo -e "\033[45;1mHayun并发数:\033[0m $instance"
echo -e "\033[45;1m项目编号:\033[0m $contact"
else
echo -e "\033[41;1mNo csv file:\033[0m $outdir/data.csv, please check!!!" && exit 0
fi

#Hapyun csv make
instance=$(cat $outdir/data.csv |wc -l)
conID=$contact
sample=${contact}_${hms}
ossutil cp -f $outdir/data.csv oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv
echo -e "\033[43;1moss表:\033[0m oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv"

if [ "$Hapyun_account" == "ll" ];then
zhanghao="/thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpy_login_ll.sh"
csvfile=$(echo "oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv")
fi
if [ "$Hapyun_account" == "gcw" ];then
zhanghao="/thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpy_login_gcw.sh"
csvfile=$(echo "oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv")
fi
if [ "$Hapyun_account" == "qyk" ];then
zhanghao="/thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpy_login_qyk.sh"
csvfile=$(echo "oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv")
fi
echo "csv,instance_count,sample" > $outdir/${contact}_${time}.csv
echo "$csvfile,$instance,$sample" >> $outdir/${contact}_${time}.csv
expect $zhanghao
echo "python2 /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py batch -t /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/Top3_result_blastn_tpl.json -c $outdir/${contact}_${time}.csv"
python2 /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py batch -t /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/Top3_result_blastn_tpl.json -c $outdir/${contact}_${time}.csv
echo -e "\033[42;1mDone!\033[0m"

