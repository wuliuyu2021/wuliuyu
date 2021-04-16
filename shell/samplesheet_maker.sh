#!/bin/bash
seqdir=$1
sd=$2
timedir=$3
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" \
&& exit 0

samplesheet="/thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/cmd_samplesheet_maker.sh"

echo "#!/bin/bash" > $samplesheet
echo "######samplesheet_stat" >> $samplesheet
echo " " >> $samplesheet
cmd="python /thinker/nfs2/longrw/mygit/tumor_ctDNA/samplesheetMaker.py \\
-r $seqdir \\
-s /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir/sequence_${seqdir}.csv \\
-f $sd \\
-t tech \\
-o /thinker/nfs2/longrw/runPipelineInfo/$timedir/$seqdir"
echo "$cmd" >> $samplesheet