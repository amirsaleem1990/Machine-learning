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
            predictors <- names(X)[!i == names(X)]
            f <- as.formula(paste(target_var_name, 
                                  paste(predictors, collapse = " + "),sep = " ~ "))
            model <- lm(formula = f, data = df)
            model_coefficients <- data.frame(summary(model)$coefficients)
            a <- model_coefficients[which.min(model_coefficients[2:nrow(model_coefficients),4])+1,]
            significance <- rbind(significance, list(row.names(a), a[,4]))
            print("Not all variables are numeric, and Most significant var [for Linear Regression] is: ")
            most_correlated_var_with_target <- significance[which.min(significance[,2]), ]
            print("amir")
            return (c(most_correlated_var_with_target[1], most_correlated_var_with_target[2]))
      }
  }
}