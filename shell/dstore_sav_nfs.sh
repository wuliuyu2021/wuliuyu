#!/bin/bash
seqdir=$1
dstore_sav="/thinker/nfs5/public/rawdata/dstore_${seqdir}_sav.sh"
monthdirs=(`ls -d /thinker/dstore/rawseq/${seqdir}* | sort`)
echo "#!/bin/bash" > $dstore_sav
for monthdir in ${monthdirs[@]}
do
	if [ ! -d /thinker/nfs5/public/rawdata/sav/$(echo -n ${monthdir} | cut -d'/' -f 5 | head -c 29 | sort | uniq) ];then
		mkdir -p /thinker/nfs5/public/rawdata/sav/$(echo -n ${monthdir} | cut -d'/' -f 5 | head -c 29 | sort | uniq)
	fi
	echo "cd ${monthdir};tar -xvf InterOp.tar -C /thinker/nfs5/public/rawdata/sav/$(echo -n ${monthdir} | cut -d'/' -f 5 | head -c 29 | sort | uniq);\
ds cp RunInfo.xml runParameters.xml /thinker/nfs5/public/rawdata/sav/$(echo -n ${monthdir} | cut -d'/' -f 5 | head -c 29 | sort | uniq)/InterOp " >> $dstore_sav
done