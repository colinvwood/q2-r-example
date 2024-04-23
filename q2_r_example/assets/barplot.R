#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly=TRUE)
input.table.fp <- args[1]
visualization.fp <- args[2]

df <- read.csv(input.table.fp)
rownames(df) <- df[['id']]
df <- subset(df, select=-c(id))

sample.sums <- rowSums(df)
sample.sums <- sort(sample.sums, decreasing=TRUE)

svg(visualization.fp)
barplot(
    sample.sums,
    main="Total Frequency per Sample",
    xlab="Sample",
    ylab="Total Frequency",
    names.arg=names(sample.sums),
)
dev.off()
