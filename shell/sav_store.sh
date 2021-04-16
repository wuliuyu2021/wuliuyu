#!/bin/bash
seqdir=$1
seq_type=$2
seq_city=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0
sav_sr_dir="/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
sav_sr_shell="$sav_sr_dir/${seqdir}_sav_${seq_type}.sh"
sav_sr_copy_dir="/thinker/nfs1/longrw/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
sav_bj_dir="/thinker/storage/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
sav_bj_shell="/thinker/storage/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/${seqdir}_sav_${seq_type}.sh"
sav_bj_copy_dir="/thinker/storage/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir"
samba_sr_dir="/thinker/samba/haplox-samba-user/seqdata/rawseq/$seqdir"
if [ $seq_city == "sr" ];then
echo "#!/bin/bash" > $sav_sr_shell
echo "######sav_store" >> $sav_sr_shell
echo "mkdir -p $sav_sr_copy_dir" >> $sav_sr_shell
echo "if [ -d $samba_sr_dir ];then" >> $sav_sr_shell
echo "	echo \"Correct directory and node!!!\" " >> $sav_sr_shell
echo "else" >> $sav_sr_shell
echo "	exit 0" >> $sav_sr_shell
echo "fi" >> $sav_sr_shell
if [ $seq_type == "xten" ];then
	echo "cd /thinker/samba/haplox-samba-user/seqdata/rawseq/$seqdir" >> $sav_sr_shell
	echo "cp -rf InterOp RunInfo.xml runParameters.xml /thinker/nfs1/longrw/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir" >> $sav_sr_shell
	echo "cd /thinker/nfs1/longrw/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir" >> $sav_sr_shell
	echo "mv RunInfo.xml runParameters.xml InterOp" >> $sav_sr_shell
elif [ $seq_type == "nova" ];then
	echo "cd /thinker/samba/haplox-samba-user/seqdata/rawseq/$seqdir" >> $sav_sr_shell
	echo "cp -rf InterOp RunInfo.xml RunParameters.xml /thinker/nfs1/longrw/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir" >> $sav_sr_shell
	echo "cd /thinker/nfs1/longrw/sav/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir" >> $sav_sr_shell
	echo "mv RunInfo.xml RunParameters.xml InterOp" >> $sav_sr_shell
fi
fi
if [ $seq_city == "bj" ];then
echo "#!/bin/bash" > $sav_bj_shell
echo "######sav_store" >> $sav_bj_shell
echo "mkdir -p $sav_bj_copy_dir" >> $sav_bj_shell
if [ -d "/thinker/samba/haplox-samba-user/gm120-1/seqdata/rawseq/$seqdir" ] ;then
	echo "if [ -d "/thinker/samba/haplox-samba-user/gm120-1/seqdata/rawseq/$seqdir" ] ;then" >> $sav_bj_shell
	echo "	echo \"Correct directory and node!!!\" " >> $sav_bj_shell
	echo "else" >> $sav_bj_shell
	echo "	exit 0" >> $sav_bj_shell
	echo "fi" >> $sav_bj_shell
	echo "cd /thinker/samba/haplox-samba-user/gm120-1/seqdata/rawseq/$seqdir" >> $sav_bj_shell
	echo "cp -rf InterOp RunInfo.xml RunParameters.xml $sav_bj_copy_dir" >> $sav_bj_shell
	echo "cd $sav_bj_copy_dir" >> $sav_bj_shell
	echo "mv RunInfo.xml RunParameters.xml InterOp" >> $sav_bj_shell
elif [ -d "/thinker/samba/haplox-samba-user/gm120-2/seqdata/rawseq/$seqdir" ]; then
	echo "if [ -d "/thinker/samba/haplox-samba-user/gm120-2/seqdata/rawseq/$seqdir" ] ;then" >> $sav_bj_shell
	echo "	echo \"Correct directory and node!!!\" " >> $sav_bj_shell
	echo "else" >> $sav_bj_shell
	echo "	exit 0" >> $sav_bj_shell
	echo "fi" >> $sav_bj_shell
	echo "cd /thinker/samba/haplox-samba-user/gm120-2/seqdata/rawseq/$seqdir" >> $sav_bj_shell
	echo "cp -rf InterOp RunInfo.xml RunParameters.xml $sav_bj_copy_dir" >> $sav_bj_shell
	echo "cd $sav_bj_copy_dir" >> $sav_bj_shell
	echo "mv RunInfo.xml RunParameters.xml InterOp" >> $sav_bj_shell
elif [ -d "/thinker/samba/haplox-samba-user/gm120-3/seqdata/rawseq/$seqdir" ];then
	echo "if [ -d "/thinker/samba/haplox-samba-user/gm120-3/seqdata/rawseq/$seqdir" ] ;then" >> $sav_bj_shell
	echo "	echo \"Correct directory and node!!!\" " >> $sav_bj_shell
	echo "else" >> $sav_bj_shell
	echo "	exit 0" >> $sav_bj_shell
	echo "fi" >> $sav_bj_shell
	echo "cd /thinker/samba/haplox-samba-user/gm120-3/seqdata/rawseq/$seqdir" >> $sav_bj_shell
	echo "cp -rf InterOp RunInfo.xml RunParameters.xml $sav_bj_copy_dir" >> $sav_bj_shell
	echo "cd $sav_bj_copy_dir" >> $sav_bj_shell
	echo "mv RunInfo.xml RunParameters.xml InterOp" >> $sav_bj_shell
fi
fi
