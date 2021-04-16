#!/bin/bash
#20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)
seqdir=$1
indir=$2
nfsdir=$3
lane=$4
pid=$5
cptype=$6
[[ $# -lt 6 ]] && echo "The number of parameter is less than 6 Please check!" && exit 0
shdir="/thinker/$nfsdir/public/rawdata/cp_cmd"
hddir="/data/rawdata/mnt/${seqdir}_lane${lane}_${pid}"
outdir="/thinker/$nfsdir/public/rawdata"
targetdir="/thinker/$nfsdir/public/rawdata/${seqdir}_lane${lane}_${pid}"
if [[ ! -e $shdir ]]; then
	mkdir -p $shdir
fi

cp="${shdir}/${seqdir}_lane${lane}_${pid}_cp.sh"

echo "#!/bin/bash" > $cp
echo "######cp" >> $cp
echo " " >> $cp
cmd1="ds cp $indir/*L00${lane}* $hddir ;python /thinker/nfs5/public/wuliuyu/wuliuyu/python/rename_rawfq_cleanfq.py $hddir $seqdir $pid;cd $hddir;md5sum *.gz > md5;md5sum -c md5 > md5.check"
cmd2="ds cp $indir/*L00${lane}* $targetdir ;python /thinker/nfs5/public/wuliuyu/wuliuyu/python/rename_rawfq_cleanfq.py $targetdir $seqdir $pid;cd $targetdir;md5sum *.gz > md5;md5sum -c md5 > md5.check"
if [[ $cptype == 'hd' ]]; then
	echo "if [[ ! -e $hddir ]]; then" >> $cp
	echo "mkdir -p $hddir" >> $cp
	echo "fi" >>$cp
	echo "$cmd1" >> $cp
elif [[ $cptype == 'oss' ]]; then
	echo "if [[ ! -e $targetdir ]]; then" >> $cp
	echo "mkdir -p $targetdir" >> $cp
	echo "fi" >> $cp
	echo "$cmd2" >> $cp
	echo "cd $outdir" >> $cp
	echo "tar -vcf ${seqdir}_lane${lane}_${pid}.tar ${seqdir}_lane${lane}_${pid}" >> $cp
	echo "/thinker/nfs5/public/tools/ossutil/ossutil cp -u -r ${seqdir}_lane${lane}_${pid}.tar oss://sz-hapdeliver/Kefu_Data_hapdeliver/${seqdir}/" >> $cp
	echo "/thinker/nfs5/public/tools/ossutil/ossutil -e oss-cn-shenzhen.aliyuncs.com sign oss://sz-hapdeliver/Kefu_Data_hapdeliver/${seqdir}/${seqdir}_lane${lane}_${pid}.tar --timeout 604800" >> $cp
fi