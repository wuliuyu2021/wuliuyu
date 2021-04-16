#!/bin/bash
seqdir=$1
nbdir=$2
pID=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0

dscp_dstore_nbcloud="/thinker/nfs2/longrw/runPipelineInfo/$seqdir/dscp_dstore_nbcloud_$seqdir.sh"

echo "#!/bin/bash" > $dscp_dstore_nbcloud
echo " " >> $dscp_dstore_nbcloud
echo "######dscp_dstore_nbcloud" >> $dscp_dstore_nbcloud
cmd="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/dscp_dstore_hpcloud.py \\
-d /thinker/dstore/rawfq/$seqdir \\
-p $pID \\
-n /thinker/dstore/nbCloud/public/rawData/@2018-04/$nbdir"
echo "$cmd" >> $dscp_dstore_nbcloud