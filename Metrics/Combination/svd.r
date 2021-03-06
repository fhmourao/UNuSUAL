args <- commandArgs(trailingOnly = TRUE)
file1 <- args[1]
fileoutput <- args[2]

f1 <- read.table(file1)

r <- svd(f1)
#dim <- 1
#u <- as.matrix(r$u[, 1:dim])
#v <- as.matrix(r$v[, 1:dim])
#d <- as.matrix(diag(r$d)[1:dim, 1:dim])

#soma <- 0
#for (i in 1:length(r$d)){
#	soma <- soma + r$d[i]
#}
#print(r$d[1]/soma)
print("Variance of each component:")
head(r$d^2/sum(r$d^2))

sink(fileoutput)
for (i in 1:nrow(f1)){
    variable <- 0
    for (j in 1:ncol(f1)){
        variable <- variable + r$v[1,j] * f1[i,j]
    }
    cat(variable)
    cat("\n")
} 
sink()
