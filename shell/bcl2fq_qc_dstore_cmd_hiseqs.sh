#!bin/bash
seqdir=$1
nfs=$2
gm55=$3
pid=$4
if [ $# -lt 4 ]
then
	echo "The number of parameter is less than 4. Please check!"
	exit 0
fi

Targetdir="/thinker/nfs2/longrw/runPipelineInfo/$seqdir"
if [ ! -d $Targetdir ]
then
	echo "Please check the dir is exist or not!"
	exit 0
fi

bcl2fq="/thinker/nfs2/longrw/runPipelineInfo/$seqdir/${seqdir}_${pid}_bcl2fq.sh"
runQC="/thinker/nfs2/longrw/runPipelineInfo/$seqdir/${seqdir}_${pid}_qc.sh"
clum="/thinker/nfs2/longrw/runPipelineInfo/$seqdir/${seqdir}_clum.sh"


#######bcl2fq
echo "#!/bin/bash" > $bcl2fq
echo "" >> $bcl2fq
echo 'runtime="/thinker/nfs2/longrw/runPipelineInfo/'$seqdir'/timestat.txt"' >> $bcl2fq
echo 'echo "bcl2fastq_start at `date` --> '$pid'" > $runtime' >> $bcl2fq
cmd="/thinker/dstore/world/software/bcl2fastq2/run/2.19/bin/bcl2fastq -r 28 -p 28 -w 28 \\
-R /thinker/samba/haplox-samba-user/seqdata/rawseq/$seqdir \\
--sample-sheet /thinker/nfs2/longrw/runPipelineInfo/$seqdir/SampleSheet.csv \\
-o /thinker/$nfs/longrw/rawfq/$seqdir \\
--tiles s_[1-8] --barcode-mismatches=0 \\
> /thinker/nfs2/longrw/runPipelineInfo/$seqdir/bcl2fq.o \\
2>/thinker/nfs2/longrw/runPipelineInfo/$seqdir/bcl2fq.e"
echo "$cmd" >> $bcl2fq



###########rawfastqStat
echo "#!/bin/bash" > $runQC
echo "" >> $runQC
echo 'runtime="/thinker/nfs2/longrw/runPipelineInfo/'$seqdir'/timestat.txt"' >> $runQC
echo "####rawfastqStat" >> $runQC
echo 'echo "rawfastqstat_start at `date` --> '$pid'" >> $runtime' >> $runQC
cmd="pypy /thinker/nfs2/longrw/mygit/rawdataQCs/rawfastqStat_$pid.py \\
-i /thinker/dstore/rawfq/$seqdir \\
-y /thinker/nfs2/longrw/runPipelineInfo/$seqdir/sequence_${seqdir}.csv \\
-o /thinker/nfs2/longrw/runPipelineInfo/$seqdir/rawfqstat_$pid \\
-g /thinker/$nfs/longrw/cleanfq/$seqdir/rawfqstat_$pid \\
> /thinker/nfs2/longrw/runPipelineInfo/$seqdir/rawfastqStat_$pid.py.o \\
2> /thinker/nfs2/longrw/runPipelineInfo/$seqdir/rawfastqStat_$pid.py.e"
echo "$cmd" >> $runQC
echo "" >> $runQC

############sample_data_stat
echo "####sample_data_stat" >> $runQC
echo 'echo "sample_data_stat_start at `date` --> '$pid'" >> $runtime' >> $runQC
cmd="pypy /thinker/nfs2/longrw/mygit/rawdataQCs/sample_data_stat.py \\
/thinker/nfs2/longrw/runPipelineInfo/$seqdir/sequence_${seqdir}.csv \\
/thinker/nfs2/longrw/runPipelineInfo/$seqdir/rawfqstat_$pid/${seqdir}_qc.csv \\
$seqdir \\
/thinker/nfs2/longrw/runPipelineInfo/$seqdir/rawfqstat_$pid"
echo "$cmd" >> $runQC
echo 'echo "sample_data_stat_end at `date` --> '$pid'" >> $runtime' >> $runQC



##########clum
if [ ! -f $clum ]
then
    echo "#!/bin/bash" > $clum
    echo "" >> $clum
    echo 'runtime="/thinker/nfs2/longrw/runPipelineInfo/'$seqdir'/timestat.txt"' >> $clum
    echo "" >> $clum
    echo 'echo "clum_start at `date`" >> $runtime' >> $clum
    cmd="pypy /thinker/nfs2/longrw/mygit/tumor_ctDNA/clumpify_sr.py /thinker/dstore/rawfq/$seqdir /thinker/$nfs/longrw/clum/$seqdir /thinker/$nfs/longrw/tmp/$seqdir"
    ds_cp="ds cp /thinker/$nfs/longrw/clum/$seqdir /thinker/dstore/clum"
    echo "$cmd" >> $clum
    echo "####ds_cp" >> $clum
    echo "$ds_cp" >> $clum
    echo "" >> $clum
    echo 'echo "clum_end at `date`" >> $runtime' >> $clum
fi


