#!/bin/bash

runid=$1

basedir="/data/users/wuliuyu/runPipelineInfo"
month=${runid:0:4}
seqinfo="$basedir/20$month/$runid/sequence_${runid}.csv"
shcmd="$basedir/20$month/$runid/${runid}_autorun_bcl2fastq_fastp.sh"

echo "#!/bin/bash" > $shcmd
echo "#######--01 autorun_csv_maker######" >> $shcmd
echo "python /data/users/wuliuyu/wuliuyu/project/autorun_csv_maker.py \
$seqinfo \
$basedir/20$month/$runid \
1 \
sz" >> $shcmd

echo "#######--02 bcl2fastq######" >> $shcmd
echo "python /data/users/longrw/tools/hpycli/hpycli.py \
batch \
-c $basedir/20$month/$runid/nova_bcl2fastq_by_lane.csv \
-t $basedir/nova_bcl2fastq_by_lane_ondisk_tpl.json" >> $shcmd

echo "#######--03 fastp######" >> $shcmd
echo "python /data/users/longrw/tools/hpycli/hpycli.py \
batch \
-c $basedir/20$month/$runid/qc_md5_batch_v1_0_1.csv\
-t $basedir/qc_md5_batch_v1_0_1_tpl.json" >> $shcmd