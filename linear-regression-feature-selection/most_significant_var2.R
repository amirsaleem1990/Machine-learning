most_significant_var <- function(){
  var.types <- sapply(X, class)
  all_varis_is_numeric = FALSE
  if (all(var.types %in% c("numeric", "integer")))
    all_varis_is_numeric = TRUE
  
  if (all_varis_is_numeric){
    # all vars are numeric, so we can simply taking a most correlated variable with target
    correlations <- data.frame(cor(cbind(X, y)))
    sorted_correlations <- correlations[order(correlations$target, decreasing = T),]
    most_correlated_var_with_target <- row.names(sorted_correlations[2,])
    print("All variables are numeric, and Most significant var [for Linear Regression] is: ")
    return (c(most_correlated_var_with_target, sorted_correlations[2,5]))
  }else{
    significance <- matrix(ncol = 2, nrow = 0)
    for (i in names(X)){
      tryCatch({
      predictors <- names(X)[!i == names(X)]
      f <- as.formula(paste(target_var_name,i,sep = " ~ "))
      model <- lm(formula = f, data = df)
      model_coefficients <- data.frame(summary(model)$coefficients)
      significance <- rbind(significance, list(i, model_coefficients[i,4]))
      }, error=function(e) stop(paste("ERROR: There is ERROR in variable", i, "[data: X]")))
    }
    print("Not all variables are numeric, and Most significant var [for Linear Regression] is: ")
    most_significant_var <- significance[which.min(significance[,2]), ]
    return (c(most_significant_var[1], most_significant_var[2]))
  }
}