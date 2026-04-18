from sklearn.cluster import KMeans
import numpy as np
import random

# random.seed(42)
f = open('A.txt')
raw_data = f.read().strip()
data = raw_data.replace(',', '.').split('\n')
points = [[float(i) for i in pair.split()] for pair in data if 'X' not in pair]
# Sample data
X = np.array(points)

# Initialize and fit
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)

# Центры кластеров
centers = kmeans.cluster_centers_
print("Cluster centers:", centers)

# Вычисление средних координат центров
Px = 0.5 * (centers[0][0] + centers[1][0])
Py = 0.5 * (centers[0][1] + centers[1][1])

# Масштабирование и суммирование целых частей
scaled_Px = int(abs(Px) * 10000)
scaled_Py = int(abs(Py) * 10000)

result = scaled_Px + scaled_Py
print(f"Scaled Px: {scaled_Px}, Scaled Py: {scaled_Py}")
print(f"Result: {result}")
# # Results
# # print(kmeans.labels_)          # Cluster labels for each point
# print(kmeans.cluster_centers_) # Coordinates of the centroids

# x = 0.5 * (kmeans.cluster_centers_[0][0] + kmeans.cluster_centers_[1][0]) * 10000
# y = 0.5 * (kmeans.cluster_centers_[0][1] + kmeans.cluster_centers_[1][1]) * 10000

# print(x, y)
# print(int(x) + int(y))

# 141099