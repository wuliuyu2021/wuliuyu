#!/bin/bash

infile=$1
outdir=$2
csv=$(echo $infile |awk -F "/" '{print $NF}')

for info in `cat $infile`;
do
S1=$(echo $info |awk -F "," '{print $1}')
S2=$(echo $info |awk -F "," '{print $2}')
S3=$(echo $info |awk -F "," '{print $3}')
S4=$(echo $info |awk -F "," '{print $4}')
S5=$(echo $info |awk -F "," '{print $5}')
S6=$(echo $info |awk -F "," '{print $6}')
S7=$(echo $info |awk -F "," '{print $7}')
S8=$(echo $info |awk -F "," '{print $8}')
S9=$(echo $info |awk -F "," '{print $9}')
S10=$(echo $info |awk -F "," '{print $10}')
S11=$(echo $info |awk -F "," '{print $11}')
S12=$(echo $info |awk -F "," '{print $12}')
S13=$(echo $info |awk -F "," '{print $13}')
S14=$(echo $info |awk -F "," '{print $14}')
S15=$(echo $info |awk -F "," '{print $15}')
S16=$(echo $info |awk -F "," '{print $16}')
S17=$(echo $info |awk -F "," '{print $17}')#type
S18=$(echo $info |awk -F "," '{print $18}')
S19=$(echo $info |awk -F "," '{print $19}')#tanzhen
S20=$(echo $info |awk -F "," '{print $20}')
S21=$(echo $info |awk -F "," '{print $21}')
S22=$(echo $info |awk -F "," '{print $22}')
S23=$(echo $info |awk -F "," '{print $23}')
S24=$(echo $info |awk -F "," '{print $24}')
S25=$(echo $info |awk -F "," '{print $25}')
S26=$(echo $info |awk -F "," '{print $26}')
S27=$(echo $info |awk -F "," '{print $27}')
S28=$(echo $info |awk -F "," '{print $28}')#jiaofu
S29=$(echo $info |awk -F "," '{print $29}')
S30=$(echo $info |awk -F "," '{print $30}')
S31=$(echo $info |awk -F "," '{print $31}')
S32=$(echo $info |awk -F "," '{print $32}')
S33=$(echo $info |awk -F "," '{print $33}')
S28NF=$(echo $info |awk -F "," '{print $28}' |awk -F "/"  '{print $NF}')
S28NF_1=$(echo $info |awk -F "," '{print $28}' |awk -F "/"  '{print $(NF-1)}')
S28NF_2=$(echo $info |awk -F "," '{print $28}' |awk -F "/"  '{print $(NF-2)}')

if [[ $S28 == "vcf" ]] || [[ $S28NF == "vcf" ]] || [[ $S28NF_1 == "vcf" ]] || [[ $S28NF_2 == "vcf" ]];then
echo '$S1","${S2}-${S17}-${19}","$S3","$S4","$S5","$S6","$S7","$S8","$S9","$S10","$S11","$S12","$S13","$S14","$S15","$S16","$S17","$S18","$S19","$S20","$S21","$S22","$S23","$S24","$S25","$S26","$S27","$S28","$S29","$S30","$S31","$S32","$S33' >> ${outdir}_${csv}_tmp

else
echo '$S1","$S2","$S3","$S4","$S5","$S6","$S7","$S8","$S9","$S10","$S11","$S12","$S13","$S14","$S15","$S16","$S17","$S18","$S19","$S20","$S21","$S22","$S23","$S24","$S25","$S26","$S27","$S28","$S29","$S30","$S31","$S32","$S33' >> ${outdir}_${csv}_tmp

fi
done
