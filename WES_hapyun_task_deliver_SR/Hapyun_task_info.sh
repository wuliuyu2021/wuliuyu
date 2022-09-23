#!/bin/bash
csv=$1 #1.csv文件
yinshe=$2 #字典对应表
outdir=$3 #data.csv生成路径
bed=$4 #安捷伦V6: /hapbin/databases/KF_Database/genome/BedFile/Exon_V6_r2_Regions_XY.bed,IDT: /hapbin/databases/KF_Database/genome/BedFile/IDT/xgen-exome-research-panel-target_XY.bed
contact=$5 #项目编号
Hapyun_account=$6 #Hapyun账号选择

time=$(date "+%Y%m%d" | awk -F "" '{print $3$4$5$6$7$8}')
hms=$(date "+%Y%m%d_%H%M%S" | awk -F "" '{print $3$4$5$6$7$8$9$10$11$12$13$14$15}')

sh /data/users/wuliuyu/wuliuyu/shell/data_csv_maker.sh $csv $yinshe $outdir no

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
if [ "$Hapyun_account" == "ll" ];then
zhanghao="/thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpy_login_ll.sh"
ossutil cp -u $outdir/data.csv oss://sz-hapbin/users/liangshu/wes/Depth_Cover/${contact}_${hms}.csv
echo -e "\033[43;1moss表:\033[0m oss://sz-hapbin/users/liangshu/wes/Depth_Cover/${contact}_${hms}.csv"
csvfile=$(echo "oss://sz-hapbin/users/liangshu/wes/Depth_Cover/${contact}_${hms}.csv")
fi
if [ "$Hapyun_account" == "gcw" ];then
zhanghao="/thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpy_login_gcw.sh"
ossutil cp -u $outdir/data.csv oss://sz-hapbin/users/ganchuanwei/wes/Depth_Cover/${contact}_${hms}.csv
echo -e "\033[43;1moss表:\033[0m oss://sz-hapbin/users/ganchuanwei/wes/Depth_Cover/${contact}_${hms}.csv"
csvfile=$(echo "oss://sz-hapbin/users/ganchuanwei/wes/Depth_Cover/${contact}_${hms}.csv")
fi

echo -e "\033[40;1m需要切分,注意工作流选择\033[0m"
ossutil cp -f $outdir/data.csv oss://sz-hapdeliver/Data_from_SR/Hapyun_task_csv/$time/${contact}_${hms}.csv
echo "data,instance_count,bed,sample" > $outdir/${contact}_${time}.csv
echo "$csvfile,$instance,$bed,$sample" >> $outdir/${contact}_${time}.csv
expect $zhanghao
echo "python2 /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py batch -t /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/wes_depth_tpl.json -c $outdir/${contact}_${time}.csv"
python2 /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py batch -t /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/wes_depth_tpl.json -c $outdir/${contact}_${time}.csv
echo -e "\033[42;1mDone!\033[0m"

