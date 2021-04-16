#!/bin/bash
seqdir=$1
type=$2
cleandir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0
timedir=20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)
pids=(`cut -d , -f 8 /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/01_samplesheet/hapyuncsv_${seqdir}.csv | sort | uniq`)
fastp="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/${seqdir}_fastp_${type}.sh"
echo "#!/bin/bash" > $fastp
echo " " >> $fastp
for pid in ${pids[@]}
do
if [[ $type = 'bgi-A' ]];then
echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_bgi-A.py \
/thinker/dstore/rawfq/$seqdir \
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/04_fastp_qcout_download \
$pid \
$cleandir" >> $fastp
elif [[ $type == 'hgc-A' ]];then
echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_hgc-A.py \
/thinker/dstore/rawfq/$seqdir \
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/04_fastp_qcout_download \
$pid" >> $fastp
elif [[ $type == 'hgc-B' ]];then
echo "python /thinker/nfs5/public/wuliuyu/wuliuyu/python/fastp_run_hgc-B.py \
/thinker/dstore/rawfq/$seqdir \
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/04_fastp_qcout_download \
$pid \
$cleandir" >> $fastp
fi 
done
