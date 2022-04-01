fc=$1
laneid=$2
outdir1=$3
outdir=${outdir1}${fc}
#hddir=$4
num=$(echo $laneid |awk -F"," '{print NF}')
time=20$(echo $fc |awk -F "" '{print $1$2$3$4}')

if [ $num == 1 ];then
while [ 0 ];
do
CopyComplete=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt |grep "CopyComplete.txt" |awk -F " " '{print $NF}')
InterOp=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar |grep "InterOp.tar" |awk -F " " '{print $NF}')
if [[ $CopyComplete == "oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt" ]] && [[ $InterOp == "oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar" ]];then
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${laneid}/ ${outdir}/Data/Intensities/BaseCalls/L00${laneid}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs ${outdir}/Data/Intensities/s.locs
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml ${outdir}/RunInfo.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml ${outdir}/RunParameters.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar ${outdir}/InterOp.tar
#
echo "$fc bcl upload complete."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${laneid}/ ${outdir}/Data/Intensities/BaseCalls/L00${laneid}/
#
echo "wait 15m"
sleep 15m
fi
done
fi

if [ $num == 2 ];then
lane1=$(echo $laneid |awk -F"," '{print $1}')
lane2=$(echo $laneid |awk -F"," '{print $2}')
while [ 0 ];
do
CopyComplete=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt |grep "CopyComplete.txt" |awk -F " " '{print $NF}')
InterOp=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar |grep "InterOp.tar" |awk -F " " '{print $NF}')
if [[ $CopyComplete == "oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt" ]] && [[ $InterOp == "oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar" ]];then
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane1}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane2}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs ${outdir}/Data/Intensities/s.locs
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml ${outdir}/RunInfo.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml ${outdir}/RunParameters.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar ${outdir}/InterOp.tar
#
echo "$fc bcl upload complete."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane1}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane2}/
#
echo "wait 15m"
sleep 15m
fi
done
fi
if [ $num == 3 ];then
lane1=$(echo $laneid |awk -F"," '{print $1}')
lane2=$(echo $laneid |awk -F"," '{print $2}')
lane3=$(echo $laneid |awk -F"," '{print $3}')
while [ 0 ];
do
CopyComplete=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt |grep "CopyComplete.txt" |awk -F " " '{print $NF}')
InterOp=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar |grep "InterOp.tar" |awk -F " " '{print $NF}')
if [[ $CopyComplete == "oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt" ]] && [[ $InterOp == "oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar" ]];then
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane1}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane2}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane3}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane3}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs ${outdir}/Data/Intensities/s.locs
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml ${outdir}/RunInfo.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml ${outdir}/RunParameters.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar ${outdir}/InterOp.tar
#
echo "$fc bcl upload complete."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane1}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane2}/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane3}/ ${outdir}/Data/Intensities/BaseCalls/L00${lane3}/
#
echo "wait 15m"
sleep 15m
fi
done
fi

if [ $num == 4 ];then
while [ 0 ];
do
CopyComplete=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt |grep "CopyComplete.txt" |awk -F " " '{print $NF}')
InterOp=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar |grep "InterOp.tar" |awk -F " " '{print $NF}')
if [[ $CopyComplete == "oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt" ]] && [[ $InterOp == "oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar" ]];then
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/ ${outdir}/Data/
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs ${outdir}/Data/Intensities/s.locs
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml ${outdir}/RunInfo.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml ${outdir}/RunParameters.xml
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar ${outdir}/InterOp.tar
#
echo "$fc bcl upload complete."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/ ${outdir}/Data/
#
echo "wait 15m"
sleep 15m
fi
done
fi
