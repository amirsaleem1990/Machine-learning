train$target_var <- as.factor(train$target_var)
test$target_var <- as.factor(test$target_var)
model_forest <- randomForest(target_var ~ ., data = train, nodesize=25, ntree=200)
pred_forst <- predict(model_forest, nwedata=test)

# confusion matrix
table(test$target_var, pred_forst)
