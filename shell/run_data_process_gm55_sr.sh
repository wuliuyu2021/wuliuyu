#!/bin/bash

runid=$1
#seqinfo=$2
#servicetype=$3

basedir="/thinker/nfs2/longrw/runPipelineInfo"
month=${runid:0:4}
servicetype="tech"
seqinfo="$basedir/20$month/$runid/sequence_${runid}.csv"
shdir="$basedir/20$month/$runid/00_cmd"

if [[ ! -e $seqinfo ]];then
    echo -e "\e[41;37;5m ERROR:\e[0m Please upload sequence_${runid}.csv!"
    exit -1
fi
########## 01 ##########

echo "#!/bin/bash" > ${shdir}/01_samplesheet_maker_${runid}.sh

outdir="$basedir/20$month/$runid/01_samplesheet"
for indextype in "I6-0" "I8-0" "S0-0"
do
    echo "python /thinker/nfs2/longrw/mygit/tumor_ctDNA/samplesheetMaker.py \
--runid=$runid --seqinfo=$seqinfo \
--flag=single --type=tech --indextype=$indextype \
--outdir=$outdir" >> ${shdir}/01_samplesheet_maker_${runid}.sh
done

for indextype in "I8-8" "I6-6" "I6-8" "D0-0"
do
    echo "python /thinker/nfs2/longrw/mygit/tumor_ctDNA/samplesheetMaker.py --runid=$runid \
--seqinfo=$seqinfo --flag=double --type=tech --indextype=$indextype \
--outdir=$outdir" >> ${shdir}/01_samplesheet_maker_${runid}.sh
done

sh ${shdir}/01_samplesheet_maker_${runid}.sh
########## 02 ##########

echo "#!/bin/bash" > ${shdir}/02_hapyun_qc_csv_make_upload.sh

pids=(`cut -d , -f 8 $basedir/20$month/$runid/01_samplesheet/hapyuncsv_${runid}.csv | sort | uniq`)
#pids=(${pids[*]} "Undetermined")

for pid in ${pids[@]}
do
    echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/upload_data_to_hapcloud.py --seqID=$runid \
--pid=$pid --outdir=$basedir/20$month/$runid/02_hapyun_csv_upload" >> ${shdir}/02_hapyun_qc_csv_make_upload.sh
    echo "##########" >> ${shdir}/02_hapyun_qc_csv_make_upload.sh
done
########## 03 ##########

echo "#!/bin/bash" > ${shdir}/03_check_N_error.sh
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/check_N_tile.py \
$basedir/20$month/$runid/04_fastp_qcout_download \
0.02 \
$basedir/20$month/$runid/03_check_download" >> ${shdir}/03_check_N_error.sh

########## 04 ##########


########## 05 ##########

echo "#!/bin/bash" > ${shdir}/05_stats_download.sh
outdir="$basedir/20$month/$runid/05_stats_download"
laneindextypes=()

for indextype in "I6-0" "I8-0" "I6-6" "I8-8" "I6-8"
do
    laneindextypes=(${laneindextypes[*]} "Lane1"$indextype)
    laneindextypes=(${laneindextypes[*]} "Lane2"$indextype)
    laneindextypes=(${laneindextypes[*]} "Lane3"$indextype)
    laneindextypes=(${laneindextypes[*]} "Lane4"$indextype)
done

for lane in ${laneindextypes[@]}
do
    if [[ -e /thinker/dstore/rawfq/$runid/${lane} ]];then
        echo "ds cp /thinker/dstore/rawfq/$runid/${lane}/Stats.json $outdir/Stats_${lane}.json" >> ${shdir}/05_stats_download.sh
        echo "##########" >> ${shdir}/05_stats_download.sh
    else
        echo "ds cp /thinker/dstore/rawfq/$runid/Stats/Stats.json $outdir/Stats.json" >> ${shdir}/05_stats_download.sh
        break
    fi
done
########## 06 ##########

echo "#!/bin/bash" > ${shdir}/06_interop.sh
echo "if [[ -e $basedir/20$month/$runid/06_interop/${runid}_InterOp.csv ]];then
    echo '${runid}_InterOp.csv exists!'
    exit -1
fi
if [[ ! -e /thinker/nfs1/longrw/sav/20$month/$runid/InterOp ]];then
    echo 'Please copy $runid SAV!'
    exit -1
fi" >> ${shdir}/06_interop.sh
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/interop_parser.py \
-r /thinker/nfs1/longrw/sav/20$month/$runid/InterOp \
-n 1317888 \
-o $basedir/20$month/$runid/06_interop/${runid}_InterOp.csv" >> ${shdir}/06_interop.sh
########## 07 ##########

echo "#!/bin/bash" > ${shdir}/07_qc_o.sh
echo "#!/bin/bash" > ${shdir}/07_qc_o_fast.sh
pids=(`cut -d , -f 8 $basedir/20$month/$runid/01_samplesheet/hapyuncsv_${runid}.csv | sort | uniq`)

for pid in ${pids[@]}
do
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/qc_batch.py \
-i /thinker/dstore/rawfq/$runid \
-j $basedir/20$month/$runid/04_fastp_qcout_download \
-o $basedir/20$month/$runid/07_qc_o \
-s $seqinfo \
-b $basedir/20$month/$runid/05_stats_download \
-n $basedir/20$month/$runid/06_interop \
-r $runid \
-p $pid" >> ${shdir}/07_qc_o.sh
echo "##########" >> ${shdir}/07_qc_o.sh
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/qc_batch.py \
-i /thinker/dstore/rawfq/$runid \
-j $basedir/20$month/$runid/04_fastp_qcout_download \
-o $basedir/20$month/$runid/07_qc_o \
-s $seqinfo \
-b $basedir/20$month/$runid/05_stats_download \
-n $basedir/20$month/$runid/06_interop \
-r $runid \
-p $pid \
--fast" >> ${shdir}/07_qc_o_fast.sh
echo "##########" >> ${shdir}/07_qc_o_fast.sh
done

##qc_all
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/qc_batch.py \
-i /thinker/dstore/rawfq/$runid \
-j $basedir/20$month/$runid/04_fastp_qcout_download \
-o $basedir/20$month/$runid/07_qc_o \
-s $seqinfo \
-b $basedir/20$month/$runid/05_stats_download \
-n $basedir/20$month/$runid/06_interop \
-r $runid" >> ${shdir}/07_qc_o.sh
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/qc_batch.py \
-i /thinker/dstore/rawfq/$runid \
-j $basedir/20$month/$runid/04_fastp_qcout_download \
-o $basedir/20$month/$runid/07_qc_o \
-s $seqinfo \
-b $basedir/20$month/$runid/05_stats_download \
-n $basedir/20$month/$runid/06_interop \
-r $runid \
--fast" >> ${shdir}/07_qc_o_fast.sh
########## 08 ##########

echo "#!/bin/bash" > ${shdir}/08_qc_reports.sh
pids=(`cut -d , -f 8 $basedir/20$month/$runid/01_samplesheet/hapyuncsv_${runid}.csv | sort | uniq`)

for pid in ${pids[@]}
do
echo "python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/ngsqcreporter/ngsqcreporter.py \
-s $seqinfo \
-j $basedir/20$month/$runid/04_fastp_qcout_download \
-p $pid \
-o $basedir/20$month/$runid/08_qc_reports/${runid}_${pid}_report --send" >> ${shdir}/08_qc_reports.sh
echo "##########" >> ${shdir}/08_qc_reports.sh
done
########## 09 ##########

whos=(`cut -d , -f 2 $basedir/20$month/$runid/01_samplesheet/hapyuncsv_${runid}.csv | sort | uniq`)

for who in ${whos[@]}
do
    mkdir -p $basedir/20$month/$runid/09_send_data_tmp/$who
done
########################################################
##########                  run               ##########
########################################################


if [[ -e /data/sav/20$month/$runid/InterOp ]] && [[ ! -e $basedir/20$month/$runid/06_interop/${runid}_InterOp.csv ]];then
    nohup sh ${shdir}/06_interop.sh &
else
    echo -e "\e[43;37;5m Please \e[0m copy $runid SAV! or ${runid}_InterOp.csv exists!"
fi
