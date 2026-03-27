""" 
=================   KMeans Clustering ================
-- an unsupervised clustering method
-- no prior undestatning of the data,
 --  Group data in to K cluster
 -- A centroid is set at the center.
 
 
 Pysodocode---
 
 1. pick our k initial centriod
 2. Assign each points to the nearest centroid
 3. Recompute centroids of clusters as the mean of assigned points
 4. Repeat until centroid stop changing---i.e, founded two groups if k=2
 
 
 How to select k values:
 --
"""
import numpy as np


class KMeans:
    def __init__(self, k=2, max_iters=10):
        self.k = k
        self.centroids = None
        self.max_iters = max_iters

    # function to calculate Euclidean distance from one point to all centroids
    def euclidean_distance(self, data_point, centroids):
        return np.sqrt(np.sum((centroids - data_point) ** 2, axis=1))

    def fit(self, X):
        # initialize the centroids by randomly picking from data
        indices = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[indices]

        for _ in range(self.max_iters):
            y = []

            # Step 2: assign points to nearest centroid
            for point in X:
                distances = self.euclidean_distance(point, self.centroids)
                cluster_num = np.argmin(distances)
                y.append(cluster_num)

            y = np.array(y)

            # Step 3: update centroids
            new_centroids = []
            for i in range(self.k):
                cluster_points = X[y == i]

                if len(cluster_points) == 0:
                    new_centroids.append(self.centroids[i])
                else:
                    new_centroids.append(np.mean(cluster_points, axis=0))

            new_centroids = np.array(new_centroids)

            # stop if centroids have converged
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

        return y


X = np.array([
    [1, 2], [1.5, 1.8], [2, 2.2], [1.2, 0.8], [0.8, 1.5],
    [5, 8], [6, 9], [5.5, 8.5], [6.5, 9.5], [7, 10]
])

kmeans = KMeans(k=3)
labels = kmeans.fit(X)

print("================= K-Means Implementation =================")
print("Sample Space:")
print(X)
print("\nLabels:", labels)
print("\nCentroids:")
print(kmeans.centroids)
