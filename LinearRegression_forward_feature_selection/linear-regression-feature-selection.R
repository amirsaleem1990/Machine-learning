rm(list = ls())
library(dplyr)
df <- read.csv("cleaned_data.csv")
if (names(df)[1] == "X"){
  #   print(head(df))
  #   readline("Name of first variable is <X>, this is prbabaily index variable, if so you should remove this variable, press 1 for remove, and 0 for keeping") ->> first_var_is_X
  #   if (first_var_is_X == "1"){
  df <- df %>% 
    select(-c("X"))
}
print(names(df))
# readline("Enter target variable name: ") ->> target_var_name
# target_var_name <- readLine("Enter target variable name: ")
target_var_name <- "SalePrice"
X <- df %>% 
  select(-c(target_var_name))
y <- df %>% 
  select(c(target_var_name))

X <- X[names(X) != "train_or_test"]

source("most_significant_var2.R")
most_significant_vaar = most_significant_var()[1]
most_significant_vaar_p_value = most_significant_var()[2]

final_vars <- c(most_significant_vaar)
balance_vars <- names(X)[!names(X) %in% final_vars]
final_P <- c(most_significant_vaar_p_value)

for (rang in seq(1:length(balance_vars)-1)){
  significance <- matrix(ncol = 2, nrow = 0)
  for (i in balance_vars){
  f <- as.formula(paste(target_var_name, 
                        paste(c(final_vars, i), collapse = " + "),sep = " ~ "))
  
  model <- lm(formula = f, data = df)
  model_coefficients <- data.frame(summary(model)$coefficients)
  
  significance <- rbind(significance, list(i, model_coefficients[i,4]))
  }
if (significance[which.min(significance[,2]), 2] > 0.05){
  break
 }else{
    final_vars <- append(final_vars, significance[which.min(significance[,2]), 1])
    final_P <- append(final_P, significance[which.min(significance[,2]), 2])
    balance_vars <- names(X)[!names(X) %in% final_vars]
 }}
cbind(final_vars, final_P)
