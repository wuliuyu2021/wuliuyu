fc=$1
laneid=$2

time=20$(echo $fc |awk -F "" '{print $1$2$3$4}')
samdir=/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc
if [ ! -d "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc" ];then
echo "No such seqdir!!!"
exit 0
fi
basedir=$samdir/Data/Intensities/BaseCalls

while [ 0 ];
do
if [[ -d "$basedir/L001" ]] && [[ -d "$basedir/L002" ]] && [[ -d "$basedir/L003" ]] && [[ -d "$basedir/L004" ]];then
echo "$fc bcl files are ready to hardisk"
sh /thinker/nfs5/public/wuliuyu/wuliuyu/sr_bcl_upload_hd_cmd/hd_rsync.sh $fc $laneid
echo "$fc bcl files rsynced to hardisk"
exit 0
else
echo "$fc bcl files are not ready to hardisk ,please wait 1h"
sleep 1h
fi
done
