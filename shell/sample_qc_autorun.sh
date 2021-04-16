#!/bin/bash
seqdir=$1
indir=$2
outdir=$3
flag=$4
sample_num=$5
[[ $# -lt 5 ]] && echo "The number of parameter is less than 5 Please check!" \
&& exit 0

sr_dir="/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
mon_sr_shell="$sr_dir/${seqdir}_monitor.sh"
qc_sr_shell="$sr_dir/${seqdir}_sample_qc.sh"

bj_dir="/thinker/storage/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
mon_bj_shell="$bj_dir/${seqdir}_monitor.sh"
qc_bj_shell="$bj_dir/${seqdir}_sample_qc.sh"

if [[ -d $sr_dir ]] ;then
if [[ ! -e "$sr_dir/01_samplesheet/hapyuncsv_${seqdir}.csv" ]] ;then
echo "NO hapyuncsv_${seqdir}.csv, please check!!!"
exit 0
fi
pids=(`cut -d , -f 8 $sr_dir/01_samplesheet/hapyuncsv_${seqdir}.csv | sort | uniq`)
echo "#!/bin/bash" > $mon_sr_shell
echo "######monitor" >> $mon_sr_shell
echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/project/qc_autorun.py $seqdir $indir $sample_num" >> $mon_sr_shell
echo "#!/bin/bash" > $qc_sr_shell
echo "######qc" >> $qc_sr_shell
	for pid in ${pids[@]}
		do 
		if [ $pid == "bgi-A" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_bgi-A.py $indir $sr_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_sr_shell
		fi
		if [ $pid == "bgi-B" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_bgi-B.py $indir $sr_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_sr_shell
		fi
		if [ $pid != "bgi-A" ] && [ $pid != "bgi-B" ] &&[ $flag == "clean" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_hgc-B.py $indir $sr_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_sr_shell
		fi
		if [ $pid != "bgi-A" ] && [ $pid != "bgi-B" ] &&[ $flag != "clean" ];then
			echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_hgc-A.py $indir $sr_dir/04_fastp_qcout_download/ $pid" >> $qc_sr_shell
		fi
		done
fi
if [[ -d $bj_dir ]] ;then
if [[ ! -e "$bj_dir/01_samplesheet/hapyuncsv_${seqdir}.csv" ]] ;then
echo "NO hapyuncsv_${seqdir}.csv, please check!!!"
exit 0
fi
pids=(`cut -d , -f 8 $bj_dir/01_samplesheet/hapyuncsv_${seqdir}.csv | sort | uniq`)
echo "#!/bin/bash" > $mon_bj_shell
echo "######monitor" >> $mon_bj_shell
echo "python /thinker/storage/users/wuliuyu/mygit/wuliuyu/project/qc_autorun.py $seqdir $indir $sample_num" >> $mon_bj_shell
echo "#!/bin/bash" > $qc_bj_shell
echo "######qc" >> $qc_bj_shell
	for pid in ${pids[@]}
		do 
		if [ $pid == "bgi-A" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/storage/users/wuliuyu/mygit/wuliuyu/python/fastp_run_bgi-A.py $indir $bj_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_bj_shell
		fi
		if [ $pid == "bgi-B" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/storage/users/wuliuyu/mygit/wuliuyu/python/fastp_run_bgi-B.py $indir $bj_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_bj_shell
		fi
		if [ $pid != "bgi-A" ] && [ $pid != "bgi-B" ] &&[ $flag == "clean" ];then
			if [[ ! -e $outdir ]] ;then
				mkdir -p $outdir
			fi
			echo "python /thinker/storage/users/wuliuyu/mygit/wuliuyu/python/fastp_run_hgc-B.py $indir $bj_dir/04_fastp_qcout_download/ $pid $outdir" >> $qc_bj_shell
		fi
		if  [ $pid != "bgi-A" ] && [ $pid != "bgi-B" ] &&[ $flag != "clean" ];then
			echo "python /thinker/storage/users/wuliuyu/mygit/wuliuyu/python/fastp_run_hgc-A.py $indir $bj_dir/04_fastp_qcout_download/ $pid" >> $qc_bj_shell
		fi
		done
fi
