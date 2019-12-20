distance <- dist(df, method = "euclidean")
cluster <- hclust(distance, method = "ward") # The <ward> method cares about the distance between clusters using centric distance and also variance(shayad yehi word bola) of each cluster 
plot(clusters)