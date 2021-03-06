#Rscript for calculating the correlation between two ranked files

args <- commandArgs(trailingOnly = TRUE)
file1 <- args[1]
file2 <- args[2]
correlation_method <-args[3]

f1 <- read.table(file1)
f2 <- read.table(file2)

paste("Correlation ", correlation_method, sep = "")
result <- cor.test(f1$V1, f2$V1, method=correlation_method)
result
