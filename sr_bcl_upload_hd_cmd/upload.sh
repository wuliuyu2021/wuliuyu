fc=$1
time=20$(echo $fc |awk -F "" '{print $1$2$3$4}')
while [ 0 ];
do
if [ -f "/thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/CopyComplete.txt" ];then
ossutil  cp -ru /thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/Data/ oss://sz-hapseq/rawseq/$time/$fc/Data/
ossutil  cp -ru /thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/RunInfo.xml oss://sz-hapseq/rawseq/$time/$fc/
ossutil  cp -ru /thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/RunParameters.xml oss://sz-hapseq/rawseq/$time/$fc/
if [ ! -d "/thinker/nfs2/longrw/bclstream/$time/$fc" ];then
mkdir -p /thinker/nfs2/longrw/bclstream/$time/$fc
fi
tar -vcf /thinker/nfs2/longrw/bclstream/$time/$fc/InterOp.tar /thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/InterOp
ossutil  cp -ru /thinker/nfs2/longrw/bclstream/$time/$fc/InterOp.tar oss://sz-hapseq/rawseq/$time/$fc/
echo "$fc bcl upload complete"
exit 0
else
ossutil  cp -ru /thinker/samba/haplox-samba-user/seqdata/rawseq/$fc/Data/ oss://sz-hapseq/rawseq/$time/$fc/Data/
echo "wait 1h"
sleep 1h
fi
done
