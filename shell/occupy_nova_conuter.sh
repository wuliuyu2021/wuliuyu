#!/bin/bash
seqdir=$1
n=$2
timedir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0

occupy="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/${seqdir}.occupy.sh"

echo "#!/bin/bash" > $occupy
echo "######occupy_stat" >> $occupy
echo " " >> $occupy
echo "mkdir -p /thinker/nfs1/longrw/sav/$timedir/$seqdir" >> $occupy
cmd="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/interop_parser.py \\
-r /thinker/nfs1/longrw/sav/$timedir/$seqdir/InterOp \\
-n $n \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/${seqdir}_InterOp.csv"
echo "$cmd" >> $occupy