glm_model = glm(target_var ~ ., data = df, family = binomial)
predict(glm_model, type="response")