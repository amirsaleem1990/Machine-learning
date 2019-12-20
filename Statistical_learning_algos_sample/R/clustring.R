distance <- dist(df, method = "euclidean")
cluster <- hclust(distance, method = "ward") # The <ward> method cares about the distance between clusters using centric distance and also variance(shayad yehi word bola) of each cluster 
plot(clusters)


# let us label each data point according to what cluster belong to.
cluster.Groups <- cutree(clusters, k  =10) # since we want 10 clusters

# lst us figger out what clusters are like.
tapply(df$target, cluster.Groups, mean)