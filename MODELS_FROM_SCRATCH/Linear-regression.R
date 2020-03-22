x=c(3,9,8,3,2)
y=c(7,2,1,4,3)
x.mean <- mean(x)
y.mean <- mean(y)
n = nrow(df)
sd.x <- sd(x)
sd.y <- sd(y)

cor <- sum(
  ((x - x.mean) / sd.x) * ((y - y.mean) / sd.y)
) / (n - 1)

b1 <- round((sd.y / sd.x) * cor, 5)
b0 <- round(y.mean - b1 * x.mean,5)
predictions <- round(b0 + b1 * x, 5)
errors <- x - predictions
Rss <- sum((y - predictions)^2)
Tss <- sum((y - y.mean)^2)
R.squared <- round((Tss - Rss) / Tss,7)



df <- data.frame(cbind(x, y))
model <- lm(y ~ x, data = df)
model_predictions <- round(as.vector(predict(model, newdata = df)), 5)
model_slope = round(summary(model)$coefficients[2,1],5)
model_intercept <- round(summary(model)$coefficients[1,1],5)
model_R.square <- round(summary(model)$r.squared,7)
print(summary(model))
if (all(predictions == model_predictions))
  print("Model predictions equal to our manual predictions")
if (model_intercept == b0)
  print(paste("Model intersept is equal to our manual intercept, which is:", b0))
if (model_slope == b1)
  print(paste("Model Slope is equal to our manual Slope, which is:        ", b1))
if (model_R.square == R.squared)
  print(paste("Model R.square is equal to our manual R.square, which is:  ", R.squared))
