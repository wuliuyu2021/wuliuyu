#!/bin/bash
dir=$1
out=$2
if [ ! -d $out ];then
mkdir -p $out
fi
cd $dir
for fa in `ls *fa`;
do
awk 'BEGIN{getline;a=$0}{if($0!=""){if(a!=""){print a;a=$0}else{a=$0}}else{a=""}}END{print a}'  $fa > $out/${fa}.new
mv $out/${fa}.new $out/${fa}
done
