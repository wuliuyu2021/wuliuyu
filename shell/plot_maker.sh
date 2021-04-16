#!/bin/bash
seqdir=$1
pID=$2
timedir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0
plot="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/plot_${pID}.sh"

echo "#!/bin/bash" > $plot
echo "######plot_stat" >> $plot
echo " " >> $plot
cmd="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/plot/quality_content.py \\
-j /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/fastp_qcout \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/${seqdir}_plot_${pID} \\
-p $pID"
echo "$cmd" >> $plot