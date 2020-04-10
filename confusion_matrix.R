cnf_mtrx <- function(target_var, predictions, cut_point){
  a = confusionMatrix(
    target_var,
    as.factor(ifelse(predictions < cut_point, 0, 1))
  )
  b <- a$table
  TN <- b[1]
  FN <- b[2]
  FP <- b[3]
  TP <- b[4]
  c(TN, TP, FP, FN)
}


summaryy <- function(actual, predicted){
  cut_points <- c()
  lst <- c()
  for (i in seq(0.04, 0.99, 0.01)){
    if (i >= min(predicted)){
      if (i <= max(predicted)){
        result <- cnf_mtrx(actual, predicted, i)
        lst <- append(lst, result)
        cut_points <- append(cut_points, i)
      }}}
  df <- data.frame(matrix(lst, ncol = 4, byrow = T))
  df$Cut_point <- cut_points
  names(df) <- c("TN", "TP", "FP", "FN", "Threshold")
  df$Precision <- df$TP / (df$TP + df$FP)
  df$Recall <- df$TP / (df$TP + df$FN)
  return (df)
plot_file <- "Precision Vs Recall_3"
}

df <- summaryy(churn, p)

jpeg(paste0(plot_file, ".jpg"), width = 2000, height = 1000)
ggplot(df, aes(x = Precision, y = Recall)) +
  geom_line() + 
  geom_point() + 
  scale_x_continuous(breaks = c(seq(from = 0, to = 1, by = 0.05))) + 
  scale_y_continuous(breaks = c(seq(from = 0, to = 1, by = 0.05)))
dev.off()

jpeg(paste0(plot_file, "_with_threshold.jpg"), width = 2000, height = 1000)
adf <- df[,5:7]
adf = reshape2::melt(adf, id.var = "Threshold")
ggplot(adf, aes(x=Threshold, y=value, col=variable)) +
  geom_line() + 
  scale_x_continuous(breaks = c(seq(from = 0, to = 1, by = 0.03))) +
  scale_y_continuous(breaks = c(seq(from = 0, to = 1, by = 0.05))) +
  labs(x = "Threshold", 
       y = "") + 
  theme_bw()
dev.off()