#!/bin/bash
seqdir=$1
taskfq=$2
pID=$3
timedir=$4
[[ $# -lt 4 ]] && echo "The number of parameter is less than 4 Please check!" \
&& exit 0
hapcloud_info_stat="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/hapcloud_info_stat_$pID.sh"

echo "#!/bin/bash" > $hapcloud_info_stat
echo " " >> $hapcloud_info_stat
echo "########rawfastqStat_hapcloud" >> $hapcloud_info_stat
cmd1="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/rawfastqStat_hapcloud.py \\
-i /thinker/dstore/rawfq/$seqdir \\
-j /thinker/dstore/$taskfq \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/rawfqstat_$pID \\
-y /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/sequence_$seqdir.csv \\
-p $pID"
echo "$cmd1" >> $hapcloud_info_stat
echo " " >> $hapcloud_info_stat
echo "########sample_data_stat" >> $hapcloud_info_stat
cmd2="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/sample_data_stat.py \\
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/sequence_$seqdir.csv \\
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/rawfqstat_${pID}/${seqdir}_qc.csv \\
$seqdir \\
/thinker/dstore/rawfq/$seqdir \\
/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/rawfqstat_$pID"
echo "$cmd2" >> $hapcloud_info_stat