feeling <- c('happy', 'sad')
for (i in feeling)
  print(switch(i, happy = 'welcome', sad = 'haplox'))


mystats <- function(x, parametric=TRUE, print=FALSE) {
  if (parametric) {
    center <- mean(x); spread <- sd(x)
  } else {
    center <- median(x); spread <- mad(x)
  }
  if (print & parametric) {
    cat('mean=', center, '\n', 'SD=', spread, '\n')
  }
  result <- list(center=center, spread=spread)
  return(result)
}
set.seed(1234)
x <- rnorm(500)
y <- mystats(x, parametric = FALSE, print=TRUE)

mydata <- function(type='short') {
  switch(type, short=format(Sys.time(), '%A %B %d %Y'), long=format(Sys.time(), '%m-%d-%y'),
        cat(type, 'is not a recognized type\n')
        )
}

mydata('long')
mydata('short')
mydata('medium')