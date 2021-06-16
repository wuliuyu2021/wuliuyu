#!/bin/bash
FC=$1
flowcellid=$(echo $FC |awk -F "_" '{print $NF}')
time=$(echo $FC |awk -F "" '{print "20"$1$2$3$4}')
basedir=/data/users/hapseq/runPipelineInfo/$time/$FC
sed "1d" $basedir/00_cmd/sequence_${FC}.csv > $basedir/sequence_${FC}_no_header.csv
oss_base=oss://sz-hapseq/rawfq/$time/$FC
head="R1,flowcellid,laneid,index1seq,index2seq,projectid,clientdemandid,qcflag,poolid,sampleid,reads_to_process"
for info in `cat $basedir/sequence_${FC}_no_header.csv`;
do
ord=$(echo $info |awk -F "," '{print $1}')
hgc=$(echo $info |awk -F "," '{print $2}')
sampleid=$(echo $info |awk -F "," '{print $4}')
projectid=$(echo $info |awk -F "," '{print $6}')
clientdemandid=$(echo $info |awk -F "," '{print $8}')
laneid=$(echo $info |awk -F "," '{print $12}')
index1seq=$(echo $info |awk -F "," '{print $14}')
index2seq=$(echo $info |awk -F "," '{print $16}')
poolid=$(echo $info |awk -F "," '{print $25}')
ossR1=$(ossutil ls $oss_base/${ord}_${qcflag}_${hgc}_${flowcellid} |grep "R1_001.fastq.gz" |awk -F " " '{print $NF}')
echo "ossR1"
R1=$(sed -i "s/oss:\/\/sz-hapseq//g" $ossR1)
echo "$head" > $basedir/${FC}_qc.csv
echo "$R1,$flowcellid,$laneid,$index1seq,$index2seq,$projectid,$clientdemandid,qc-hgc-C,$poolid,$sampleid," >> $basedir/${FC}_qc.csv
done
