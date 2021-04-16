#!/bin/bash
expdir=$1
laneid=$2
runfolderdir=$3
movedir=$4
[[ $# -lt 4 ]] && echo "The number of parameter is less than 4 Please check!" && exit 0
exp="$expdir/L00${laneid}/config.exp"
echo "#!/usr/bin/expect" > $exp
echo "spawn sftp -P 8288 ftpuser005@www.omicsbean.com:ftpuser005" >> $exp
echo "set timeout 36000" >> $exp
echo "expect \"ftpuser005@www.omicsbean.com's password:\"" >> $exp
echo "send \"ftpuser005\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"put -r ${runfolderdir}/Data/Intensities/s.locs ${movedir}/Data/Intensities/\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"put -r ${runfolderdir}/*.xml ${movedir}/\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"put -r ${runfolderdir}/Data/Intensities/BaseCalls/L00${laneid}/*.filter ${movedir}/Data/Intensities/BaseCalls/L00${laneid}/\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"bye\r\"" >> $exp