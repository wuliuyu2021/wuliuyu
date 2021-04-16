#!/bin/bash
seqdir=$1
pID=$2
timedir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0

qcreporter="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/qcreport_${pID}.sh"


echo "#!/bin/bash" > $qcreporter
echo " " >> $qcreporter
echo "#####ngs_reporter" >> $qcreporter
cmd="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/ngsqcreporter/ngsqcreporter.py \\
-s /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/sequence_${seqdir}.csv \\
-j /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout \\
-p $pID \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/${seqdir}_${pID}_report \\
--send"
echo "$cmd" >> $qcreporter




