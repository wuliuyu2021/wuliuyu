#!/bin/bash
expdir=$1
laneid=$2
cycle=$3
targetdir=$4
movedir=$5
[[ $# -lt 5 ]] && echo "The number of parameter is less than 5 Please check!" && exit 0
exp="$expdir/L00${laneid}/${cycle}.exp"
echo "#!/usr/bin/expect" > $exp
echo "spawn sftp -P 8288 ftpuser005@www.omicsbean.com:ftpuser005" >> $exp
echo "set timeout 36000" >> $exp
echo "expect \"ftpuser005@www.omicsbean.com's password:\"" >> $exp
echo "send \"ftpuser005\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"mkdir ${movedir}\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"cd ${movedir}\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"mkdir Data\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"cd ${movedir}/Data\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"mkdir Intensities\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"cd ${movedir}/Data/Intensities\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"mkdir BaseCalls\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"put -r ${targetdir} ${movedir}/Data/Intensities/BaseCalls/\r\"" >> $exp
echo "expect \"sftp>\"" >> $exp
echo "send \"bye\r\"" >> $exp