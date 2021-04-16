#!/bin/bash

seqdir=$1
ymth=$2 #year_month
b1_startCycle=$3 #PE_length
index_type=$4 #i88 i80 i60
[[ $# -lt 3 ]] && echo "The number of parameter is less than 3 Please check!" && exit 0

basicdir="/data/users/mgiseq/mgiseq2000/R2100400190094"
configdir="$basicdir/$seqdir"

mkdir -p $configdir/L01
mkdir -p $configdir/L02
mkdir -p $configdir/L03
mkdir -p $configdir/L04

head="barcodes,fq1,fq2,b1_length,b1_mismatchNum,\
b1_startCycle,b2_length,b2_mismatchNum,\
b2_startCycle,is_merge,is_pe,is_rename,\
is_reverse,laneid,outdir,sample"

if [[ $index_type == i88 ]]; then
b2_startCycle=$(echo $b1_startCycle + 8|bc)

L01_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L01.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_2.fq.gz,\
8,0,$b1_startCycle,8,0,$b2_startCycle,\
false,true,false,false,\
1,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L01_b88"

L02_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L02.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_2.fq.gz,\
8,0,$b1_startCycle,8,0,$b2_startCycle,\
false,true,false,false,\
2,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L02_b88"

L03_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L03.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_2.fq.gz,\
8,0,$b1_startCycle,8,0,$b2_startCycle,\
false,true,false,false,\
3,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L03_b88"

L04_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L04.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_2.fq.gz,\
8,0,$b1_startCycle,8,0,$b2_startCycle,\
false,true,false,false,\
4,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L04_b88"
fi
if [[ $index_type == i80 ]]; then
b2_startCycle=$(echo $b1_startCycle + 8|bc)

L01_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L01.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_2.fq.gz,\
8,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
1,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L01_b80"

L02_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L02.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_2.fq.gz,\
8,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
2,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L02_b80"

L03_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L03.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_2.fq.gz,\
8,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
3,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L03_b80"

L04_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L04.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_2.fq.gz,\
8,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
4,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L04_b80"
fi

if [[ $index_type == i60 ]]; then
b2_startCycle=$(echo $b1_startCycle + 6|bc)

L01_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L01.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L01_read_2.fq.gz,\
6,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
1,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L01_b60"

L02_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L02.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L02_read_2.fq.gz,\
6,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
2,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L02_b60"

L03_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L03.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L03_read_2.fq.gz,\
6,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
3,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L03_b60"

L04_csv="oss://sz-hapbin/runPipelineInfo/$ymth/R2100400190094/$seqdir/${seqdir}_L04.txt,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_1.fq.gz,\
oss://sz-hapseq/rawfq/$ymth/R2100400190094/$seqdir/L01/${seqdir}_L04_read_2.fq.gz,\
6,0,$b1_startCycle,0,0,$b2_startCycle,\
false,true,false,false,\
4,\
$ymth/R2100400190094/${seqdir}/,\
${seqdir}_L04_b60"
fi

echo "$head" > $configdir/L01/splitBarcode.csv
echo "$head" > $configdir/L02/splitBarcode.csv
echo "$head" > $configdir/L03/splitBarcode.csv
echo "$head" > $configdir/L04/splitBarcode.csv

echo "$L01_csv" >> $configdir/L01/splitBarcode.csv
echo "$L02_csv" >> $configdir/L02/splitBarcode.csv
echo "$L03_csv" >> $configdir/L03/splitBarcode.csv
echo "$L04_csv" >> $configdir/L04/splitBarcode.csv