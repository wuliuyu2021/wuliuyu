library(grid)
library(VennDiagram)

A=80:200
B=c(100:150,300:350)
C=c(50:80,300:380)
D=c(80:200, 250:300)

E<-venn.diagram(list(A=A,B=B,C=C,D=D),filename=NULL,lwd=1,lty=2,
                col=c('red','green','blue','black'),
                fill=c('red','green','blue','black'),
                cat.col=c('red','green','blue','black'),
                rotation.degree=80,reverse=FALSE)

grid.draw(E)

