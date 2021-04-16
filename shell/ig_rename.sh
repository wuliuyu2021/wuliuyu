dir=$1
cd $dir
for fq1 in `ls S*R1*gz`;
do
prefix=$(echo $fq1 |awk -F "_" '{print $3}')
outdir=$(echo $prefix |awk -F "-" '{print $1}')
if [ ! -d $outdir ];then
mkdir -p $outdir
fi
mv $fq1 $outdir/${prefix}_R1.fastq.gz
echo "$fq1 moves to $outdir/${prefix}_R1.fastq.gz"
done

for fq2 in `ls S*R2*gz`;
do
prefix=$(echo $fq2 |awk -F "_" '{print $3}')
outdir=$(echo $prefix |awk -F "-" '{print $1}')
if [ ! -d $outdir ];then
mkdir -p $outdir
fi
mv $fq2 $outdir/${prefix}_R2.fastq.gz
echo "$fq2 moves to $outdir/${prefix}_R2.fastq.gz"
done

