library(ggplot2)
library(grid)
data =read.table(file="isoforms.filter.txt",header=TRUE,row.names=1)
volcano <- ggplot(data=data,aes(log2FC,-1*log10(FDR))) + 
  geom_point(aes(color =significant)) +
  labs(title="Volcanoplot",x='log2FC', y='-log10(FDR)') +
  scale_color_manual(values = c("green","black", "red")) + 
  geom_hline(yintercept=1.3,linetype=4) +
  geom_vline(xintercept=c(-1,1),linetype=4)
grid.draw(volcano)
ggsave('volcano.png',volcano)



