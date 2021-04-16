#!/bin/bash
seqdir=$1
pID=$2
timedir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0
upload_data_to_hapcloud="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/upload_data_to_hapcloud_${pID}_csv.sh"

echo "#!/bin/bash" > $upload_data_to_hapcloud
echo "######upload_data_to_hapcloud_stat" >> $upload_data_to_hapcloud
echo " " >> $upload_data_to_hapcloud
echo "ds cp /thinker/dstore/rawfq/$seqdir/Stats/Stats.json /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir" >> $upload_data_to_hapcloud
cmd="python /thinker/nfs5/public/wuliuyu/wuliuyu/python/upload_data_to_hapcloud.py \\
-f $seqdir \\
-p $pID"
echo "$cmd" >> $upload_data_to_hapcloud