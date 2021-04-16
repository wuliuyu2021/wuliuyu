#!/bin/bash
seqdir=$1
#project=$2
taskfq=$2
taskmd5=$3
cID=$4
city=$5
pID=$6
dest=$7
[[ $# -lt 7 ]] && echo "The number of parameter is less than 7 Please check!" \
&& exit 0

cp_to_usb="/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/${seqdir}_cp_to_usb_${cID}_${city}_${pID}.sh"

echo "#!/bin/bash" > $cp_to_usb
echo " " >> $cp_to_usb
echo "#####cp_rename_checkmd5" >> $cp_to_usb
cmd="python /thinker/nfs2/longrw/mygit/hapcloud_info_stat/copyutil/cp_rename_checkmd5_bgi-A.py \\
$taskfq \\
$taskmd5 \\
${dest}${cID}_${city}_$(echo -n $seqdir | cut -d'_' -f 2 | tail -c 4)$(echo -n $seqdir | cut -d'_' -f 4 | head -c 1)_${pID}/Rawdata \\
$pID \\
$cID \\
$city \\
/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/sequence_${seqdir}.csv"
echo "$cmd" >> $cp_to_usb
echo "####rm Rawdata/*/*.md5" >> $cp_to_usb
echo "rm -f ${dest}${cID}_${city}_$(echo -n $seqdir | cut -d'_' -f 2 | tail -c 4)$(echo -n $seqdir | cut -d'_' -f 4 | head -c 1)_${pID}/Rawdata/*/*.md5" >> $cp_to_usb