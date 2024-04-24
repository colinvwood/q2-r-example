#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly=TRUE)

input_table_fp <- args[1]
output_table_fp <- args[2]

df <- read.csv(input_table_fp, check.names=FALSE)
for (col in names(df)) {
    if ( !is.character(df[[col]]) ) {
        df[[col]] <- sample(1:1000, nrow(df), replace=TRUE)
    }
}

write.csv(df, output_table_fp, row.names=FALSE)
