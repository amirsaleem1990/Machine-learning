df <- data.frame(cbind(x=c(3,9,8,3,2),y=c(7,2,1,4,3)))
x.mean <- mean(df$x)
y.mean <- mean(df$y)
n = nrow(df)
sd.x <- sd(df$x)
sd.y <- sd(df$y)

cor <- sum(
  ((df$x - x.mean) / sd.x) * ((df$y - y.mean) / sd.y)
) / (n - 1)

b1 <- round((sd.y / sd.x) * cor, 5)
b0 <- y.mean - b1 * x.mean
print(b1)
print(b0)
predictions <- round(b0 + b1 * df$x, 5)
errors <- df$x - predictions
Rss <- sum((df$y - predictions)^2)
Tss <- sum((df$y - y.mean)^2)
R.squared <- round((Tss - Rss) / Tss,7)



model <- lm(y ~ x, data = df)
print(summary(model))
model_predictions <- round(as.vector(predict(model, newdata = df$d)), 5)
model_slope = round(summary(model)$coefficients[2,1],5)
model_intercept <- summary(model)$coefficients[1,1]
model_R.square <- round(summary(model)$r.squared,7)
if (all(predictions == model_predictions))
  print("Model predictions equal to our manual predictions")
if (model_intercept == b0)
  print("Model intersept is equal to our manual intercept")
if (model_slope == b1)
  print("Model Slope is equal to our manual Slope")
if (model_R.square == R.squared)
  print("Model R.square is equal to our manual R.square")
