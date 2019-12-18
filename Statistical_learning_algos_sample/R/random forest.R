train$target_var <- as.factor(train$target_var)
test$target_var <- as.factor(test$target_var)
model_forest <- randomForest(target_var ~ ., data = train, nodesize=25, ntree=200)
pred_forst <- predict(model_forest, nwedata=test)

# confusion matrix
table(test$target_var, pred_forst)


library(caret)
library(e1071)
# we need 10 folds
numFolds <- trainControl(method="cv", number=10)
# we need to pick the plausible value for <cp> parameter
cpGrid <- expand.grid(.cp=seq(0.01, 0.5, 0.01))
# Now we are ready for cross validation
(cp_values <- train(target_var ~ ., data = train, method="rpart", trControl=numFolds, tuneGrid=cpGrid))
# fron the last line we saw that plausible <cp> is 0.18

# So now lets build a new model with this value <0.18> of cp instead of <minbucket> parameter.
final_rpart_model <- rpart(target_var ~ ., data = train, method="class", cp=0.18) 
