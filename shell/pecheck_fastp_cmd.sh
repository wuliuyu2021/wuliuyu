#!/bin/bash
seqdir=$1
nbdir=$2
pedir=$3
pID=$4
timedir=$5
[[ $# -lt 5 ]] && echo "The number of parameter is less than 5 Please check!" \
&& exit 0
fastp_h_j="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_${pID}.sh"
echo "#!/bin/bash" > $fastp_h_j
echo "mkdir -p /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout" >> $fastp_h_j
echo "mkdir -p /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/N_error" >> $fastp_h_j
echo "mkdir -p /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/pecheck" >> $fastp_h_j
echo "cp /thinker/dstore/$nbdir/QC/*.json /thinker/dstore/$nbdir/QC/*.html /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout" >> $fastp_h_j
echo "cp /thinker/dstore/$pedir/PECHECK/*.json /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/pecheck" >> $fastp_h_j
echo " " >> $fastp_h_j
cmd1="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/qc_batch.py \\
-i /thinker/dstore/rawfq/$seqdir \\
-j /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/qc_${pID} \\
-s /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/sequence_${seqdir}.csv \\
-p $pID"
echo "$cmd1" >> $fastp_h_j
echo " " >> $fastp_h_j
cmd2="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/check_N_tile.py \\
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout \\
0.02 \\
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/N_error"
echo "$cmd2" >> $fastp_h_j
echo "grep -rn 'failed' /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/pecheck/" >> $fastp_h_j