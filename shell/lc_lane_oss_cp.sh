#!/bin/bash
#20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)
seqdir=$1
indir=$2
nfsdir=$3
poolingid=$4
pid=$5
cptype=$6
[[ $# -lt 6 ]] && echo "The number of parameter is less than 6 Please check!" && exit 0
shdir="/thinker/$nfsdir/public/rawdata/cp_cmd"
if [[ ! -e $shdir ]]; then
	mkdir -p $shdir
fi
cp="${shdir}/${seqdir}_${poolingid}_${pid}_cp.sh"

echo "#!/bin/bash" > $cp
echo "######cp" >> $cp
echo " " >> $cp
cmd1="python /thinker/nfs5/public/wuliuyu/wuliuyu/python/lc_xten_lane_copy.py \\
$indir \\
/thinker/$nfsdir/public/rawdata/$poolingid \\
/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/sequence_${seqdir}.csv \\
$poolingid \\
$pid"
cmd2="python /thinker/nfs5/public/wuliuyu/wuliuyu/python/lc_xten_lane_copy.py \\
$indir \\
/data/rawdata/mnt/$poolingid \\
/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/sequence_${seqdir}.csv \\
$poolingid \\
$pid"
if [[ $cptype == 'hd' ]]; then
	echo "$cmd2" >> $cp
elif [[ $cptype == 'oss' ]]; then
	echo "$cmd1" >> $cp
	echo "cd /thinker/$nfsdir/public/rawdata" >> $cp
	echo "/thinker/nfs5/public/tools/ossutil/ossutil cp -u -r ${poolingid}/ oss://sz-hapdeliver/GMPHP18F/Hiseq-Xten/${poolingid}/" >> $cp
fi