fc=$1
laneid=$2
outdir=$3
hddir=$4
num=$(echo $laneid |awk -F"," '{print NF}')
time=20$(echo $fc |awk -F "" '{print $1$2$3$4}')

if [ $num == 1 ];then
while [ 0 ];
do
CopyComplete=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt |grep "CopyComplete.txt" |awk -F " " '{print $NF}')
InterOp=$(ossutil ls oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar |grep "InterOp.tar" |awk -F " " '{print $NF}')
if [[ $CopyComplete == "oss://sz-hapseq/rawseq/$time/$fc/CopyComplete.txt" ]] && [[ $InterOp == "oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar" ]];then
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${laneid}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
echo "$fc bcl upload complete, and rsync done."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${laneid}/ $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
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
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
echo "$fc bcl upload complete, and rsync done."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
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
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane3}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
echo "$fc bcl upload complete, and rsync done."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane1}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane2}/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/BaseCalls/L00${lane3}/ $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
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
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/ $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/Intensities/s.locs $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunInfo.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/RunParameters.xml $outdir
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/InterOp.tar $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
echo "$fc bcl upload complete, and rsync done."
exit 0
else
ossutil cp -ru oss://sz-hapseq/rawseq/$time/$fc/Data/ $outdir
rsync -r -t $outdir/rawseq/$time/$fc $hddir
echo "wait 15m"
sleep 15m
fi
done
fi
