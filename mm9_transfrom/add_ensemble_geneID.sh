#!/bin/bash

file=$1
newfile=$2

perl /thinker/nfs5/public/wuliuyu/wuliuyu/mm9_transfrom/get_all_match_geneID_readscount.pl \
/thinker/nfs5/public/wuliuyu/wuliuyu/mm9_transfrom/all_mm9_match_ensemble_geneID.txt \
$file \
$newfile