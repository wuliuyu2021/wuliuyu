fc=$1
laneid=$2
num=$(echo $laneid |awk -F"," '{print NF}')

time=20$(echo $fc |awk -F "" '{print $1$2$3$4}')
samdir=/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc
basedir=$samdir/Data/Intensities/BaseCalls

hddir=/data/rawdata/mnt/$fc/Data/Intensities/BaseCalls
mkdir -p $hddir


if [ $num == 1 ];then
while [ 0 ];
do
if [ -f "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/CopyComplete.txt" ];then
rsync -r -t $basedir/L00${laneid} ${hddir}
rsync -r -t $samdir/Data/Intensities/s.locs /data/rawdata/mnt/$fc/Data/Intensities/
rsync -r -t $samdir/RunInfo.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/RunParameters.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/InterOp /data/rawdata/mnt/$fc/
echo "$fc bcl upload complete"
exit 0
else
rsync -r -t $basedir/L00${laneid} ${hddir}
echo "wait 1h"
sleep 1h
fi
done
fi


if [ $num == 2 ];then
lane1=$(echo $laneid |awk -F"," '{print $1}')
lane2=$(echo $laneid |awk -F"," '{print $2}')
while [ 0 ];
do
if [ -f "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/CopyComplete.txt" ];then
rsync -r -t $basedir/L00${lane1} ${hddir} & rsync -r -t $basedir/L00${lane2} ${hddir}
rsync -r -t $samdir/Data/Intensities/s.locs /data/rawdata/mnt/$fc/Data/Intensities/
rsync -r -t $samdir/RunInfo.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/RunParameters.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/InterOp /data/rawdata/mnt/$fc/
echo "$fc bcl upload complete"
exit 0
else
rsync -r -t $basedir/L00${lane1} ${hddir} & rsync -r -t $basedir/L00${lane2} ${hddir}
echo "wait 1h"
sleep 1h
fi
done
fi


if [ $num == 3 ];then
lane1=$(echo $laneid |awk -F"," '{print $1}')
lane2=$(echo $laneid |awk -F"," '{print $2}')
lane3=$(echo $laneid |awk -F"," '{print $3}')
while [ 0 ];
do
if [ -f "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/CopyComplete.txt" ];then
rsync -r -t $basedir/L00${lane1} ${hddir} & rsync -r -t $basedir/L00${lane2} ${hddir} & rsync -r -t $basedir/L00${lane3} ${hddir}
rsync -r -t $samdir/Data/Intensities/s.locs /data/rawdata/mnt/$fc/Data/Intensities/
rsync -r -t $samdir/RunInfo.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/RunParameters.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/InterOp /data/rawdata/mnt/$fc/
echo "$fc bcl upload complete"
exit 0
else
rsync -r -t $basedir/L00${lane1} ${hddir} & rsync -r -t $basedir/L00${lane2} ${hddir} & rsync -r -t $basedir/L00${lane3} ${hddir}
echo "wait 1h"
sleep 1h
fi
done
fi


if [ $num == 4 ];then
while [ 0 ];
do
if [ -f "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/CopyComplete.txt" ];then
rsync -r -t $basedir/* ${hddir}
rsync -r -t $samdir/Data/Intensities/s.locs /data/rawdata/mnt/$fc/Data/Intensities/
rsync -r -t $samdir/RunInfo.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/RunParameters.xml /data/rawdata/mnt/$fc/
rsync -r -t $samdir/InterOp /data/rawdata/mnt/$fc/
echo "$fc bcl upload complete"
exit 0
else
rsync -r -t $basedir/* ${hddir}
echo "wait 1h"
sleep 1h
fi
done
fi
