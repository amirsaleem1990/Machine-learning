glm_model = glm(target_var ~ ., data = df, family = binomial)

train_prediction = predict(glm_model, type="response") 
test_prediction  = predict(glm_model, newdata=test, type="response") 
# let us check if model works or not
tapply(test_prediction, df$target_var, mean)
# 0       1
# 0.1	  0.44
# This means the models predict on average grater values for those are actually 1


