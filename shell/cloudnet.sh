#!/bin/bash

indir=$1

outseq=$(echo $indir | awk -F "/" '{print $(NF-1)}')
piddir=$(echo $indir | awk -F "/" '{print $NF}')

ossutil cp -ru ${indir}/ oss://sz-hapseq/outseq-tech/${outseq}/${piddir}/

echo "${indir} uploaded to oss://sz-hapseq/outseq-tech/${outseq}/${piddir}/ done"
