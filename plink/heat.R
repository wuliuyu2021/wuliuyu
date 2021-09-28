#!/usr/bin/Rscript
args <- commandArgs(TRUE);
if (length(args) != 2){
        print("Usage: Rscript heatmap.R <input matrix> <out info>");
        quit();
}
outpdf<-paste(args[2], "heatmap.pdf", sep=".");
library(pheatmap)
DIS<-read.table(args[1],sep="\t",header=T,row.names=1)

pdf(outpdf,width=ceiling(length(row.names(DIS))*18/40)+0.5,height=ceiling(length(row.names(DIS))*18/40)+0.5)
pheatmap(DIS,show_rownames=T,cellwidth = 18, cellheight = 18, fontsize = 8,cluster_rows = F,cluster_cols = F,display_numbers=T)
dev.off()

