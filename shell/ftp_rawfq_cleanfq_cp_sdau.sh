#!/bin/bash
#20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)
seqdir=$1
indir=$2
nfsdir=$3
contractid=$4
pid=$5
[[ $# -lt 5 ]] && echo "The number of parameter is less than 5 Please check!" && exit 0
shdir="/thinker/$nfsdir/public/rawdata/cp_cmd"
expdir="/thinker/$nfsdir/public/rawdata/ftp_exp"
if [[ ! -e $shdir ]]; then
	mkdir -p $shdir
fi
if [[ ! -e $expdir ]]; then
	mkdir -p $expdir
fi

cp="${shdir}/${seqdir}_${contractid}_${pid}_ftp_cp.sh"
exp="${expdir}/${seqdir}_${contractid}_${pid}_ftp_cp.exp"

echo "#!/bin/bash" > $cp
echo "######cp" >> $cp
echo " " >> $cp
cmd="python /thinker/nfs5/public/wuliuyu/wuliuyu/project/rawfq_cleanfq_copy.py \\
$indir \\
/thinker/$nfsdir/public/rawdata/${seqdir}_${contractid}_${pid}_ftp \\
/thinker/nfs2/longrw/runPipelineInfo/20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)/$seqdir/sequence_${seqdir}.csv \\
$contractid \\
$pid"

echo "$cmd" >> $cp
echo "#!/usr/expect/bin/expect" > $exp
echo " " >> $exp
echo "spawn sftp guest2@137.189.43.55:guest2" >> $exp
echo "set timeout 72000" >> $exp
echo "expect \"guest2@137.189.43.55's password:\"" >> $exp
echo "send \"guest2@1234\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"mkdir ${contractid}_${pid}\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"put -r /thinker/$nfsdir/public/rawdata/${seqdir}_${contractid}_${pid}_ftp/* ${contractid}_${pid}/\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"bye\r\"" >> $exp
if [[ ! -e $exp ]]; then
	echo "$exp not exists!!!" && exit 0
fi
echo "/usr/expect/bin/expect $exp" >> $cp