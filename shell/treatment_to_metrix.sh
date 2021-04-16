#!/bin/bash

nbdir=$1
outdir=$2

mkdir -p /thinker/nfs5/public/$outdir
cp /thinker/dstore/$nbdir/*.metrix /thinker/nfs5/public/$outdir
cat /thinker/nfs5/public/$outdir/*.metrix > /thinker/nfs5/public/$outdir/metrix-old
rm /thinker/nfs5/public/$outdir/*.metrix
grep -A 1 "LIBRARY" /thinker/nfs5/public/$outdir/metrix-old > /thinker/nfs5/public/$outdir/metrix-new
grep -v "#" /thinker/nfs5/public/$outdir/metrix-new |awk '{if($0!="--")print}' > /thinker/nfs5/public/$outdir/metrix-newa
sed -i '/LIBRARY/d' /thinker/nfs5/public/$outdir/metrix-newa