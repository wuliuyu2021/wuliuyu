#!/bin/bash
#20$(echo -n $seqdir | cut -d'_' -f 1 | head -c 4)
seqdir=$1
outdir=$2
nfsdir=$3
lane=$4
dest=$5
paltform=$6

[[ $# -lt 6 ]] && echo "The number of parameter is less than 6 Please check!" && exit 0

shdir="/thinker/$nfsdir/public/rawdata/cp_cmd"
if [[ ! -e $shdir ]]; then
	mkdir -p $shdir
fi

bcl_cp="${shdir}/${seqdir}_lane${lane}_${paltform}_${dest}_bcl_cp.sh"
bcl_dir="/thinker/samba/haplox-samba-user/seqdata/rawseq/${seqdir}"
if [[ ! -e $bcl_dir ]]; then
	echo "No such $bcl_dir"
	exit 0
fi

if [[ $paltform == 'nova' ]]; then
	if [[ $dest == 'oss' ]]; then
	echo "cd /thinker/$nfsdir/public/rawdata" > $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${bcl_dir}/Data/Intensities/BaseCalls/L00${lane}/ ${outdir}${seqdir}/Data/Intensities/BaseCalls/L00${lane}/" >> $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${bcl_dir}/Data/Intensities/s.locs ${outdir}${seqdir}/Data/Intensities/" >> $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${bcl_dir}/RunInfo.xml ${outdir}${seqdir}/" >> $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${bcl_dir}/RunParameters.xml ${outdir}${seqdir}/" >> $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${bcl_dir}/RTAComplete.txt ${outdir}${seqdir}/" >> $bcl_cp
	fi
	if [[ $dest == 'hd' ]]; then
	echo "if [[ ! -e ${outdir}/${seqdir}/Data/Intensities/BaseCalls/ ]]; then" > $bcl_cp
	echo "mkdir -p ${outdir}/${seqdir}/Data/Intensities/BaseCalls/" >> $bcl_cp
	echo "fi" >> $bcl_cp
	echo "cp -rf ${bcl_dir}/Data/Intensities/BaseCalls/L00${lane} ${outdir}/${seqdir}/Data/Intensities/BaseCalls/" >> $bcl_cp
	echo "cp -f ${bcl_dir}/Data/Intensities/s.locs ${outdir}/${seqdir}/Data/Intensities/" >> $bcl_cp
	echo "cp -f ${bcl_dir}/*.xml ${outdir}/${seqdir}/" >> $bcl_cp
	echo "cp -f ${bcl_dir}/RTAComplete.txt ${outdir}/${seqdir}/" >> $bcl_cp
	fi
fi
if [[ $paltform == 'xten' ]]; then
	if [[ $dest == 'oss' ]]; then
	echo "cd /thinker/samba/haplox-samba-user/seqdata/rawseq" > $bcl_cp
	echo "tar -vcf /thinker/$nfsdir/public/rawdata/${seqdir}_lane${lane}_${paltform}_bcl.tar \
	${seqdir}/Data/Intensities/s.locs ${seqdir}/Data/Intensities/BaseCalls/L00${lane} ${seqdir}/RTAComplete.txt ${seqdir}/*.xml" >> $bcl_cp
	echo "cd /thinker/$nfsdir/public/rawdata" >> $bcl_cp
	echo "ossutil cp -ru --jobs=1 ${seqdir}_lane${lane}_${paltform}_bcl.tar $outdir" >> $bcl_cp
	fi
	if [[ $dest == 'hd' ]]; then
	echo "cd /thinker/samba/haplox-samba-user/seqdata/rawseq" > $bcl_cp
	echo "tar -vcf /thinker/$nfsdir/public/rawdata/${seqdir}_lane${lane}_${paltform}_bcl.tar \
	${seqdir}/Data/Intensities/s.locs ${seqdir}/Data/Intensities/BaseCalls/L00${lane} ${seqdir}/RTAComplete.txt ${seqdir}/*.xml" >> $bcl_cp
	echo "cd /thinker/$nfsdir/public/rawdata" >> $bcl_cp
	echo "cp -f ${seqdir}_lane${lane}_${paltform}_bcl.tar $outdir" >> $bcl_cp
	fi
fi
