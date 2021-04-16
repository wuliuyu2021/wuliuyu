#!/bin/bash

indir=$1

rnaseq="/thinker/nfs3/RNA-seq/sample/$indir/${indir}_rnaseq.sh"

############rnaseq

echo "#!/bin/bash" > $rnaseq
echo "" >> $rnaseq
cmd="pypy /thinker/nfs1/hapbin/rna-seq/script/RNA_pipeline.py \\
-s /thinker/nfs3/RNA-seq/sample/$indir/sample.txt \\
-F /thinker/nfs3/RNA-seq/sample/$indir/sample.txt \\
-S /thinker/nfs3/RNA-seq/sample/$indir/report \\
-D N \\
-o /thinker/nfs3/RNA-seq/sample/$indir/test"
echo "$cmd" >> $rnaseq


