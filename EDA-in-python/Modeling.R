rm(list=ls())
suppressWarnings(library(dplyr))
library(readr)
df <- read.csv("df.csv")
target_variable_name <- read_file("target_variable.txt")
if is.numeric(df[[target_variable_name]]){

    lm.full <- lm(as.formula(paste(target_variable_name, " ~ .")), data = df)
    lm.null <- lm(as.formula(paste(target_variable_name, " ~ 1")), data = df)

    model.aic.both <- step(
      lm.full, direction = "both", scope = as.formula(paste("ACTUAL_WORTH ~ ", paste(names(train), collapse = " + ")))
    )
    save(model.aic.both, file="model.aic.both.rda")
}

smp_size <- floor(0.75 * nrow(df))
train_ind <- sample(seq_len(nrow(df)), size = smp_size)
train <- df[train_ind, ]
test <- df[-train_ind, ]
