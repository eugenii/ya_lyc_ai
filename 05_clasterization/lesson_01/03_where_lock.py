# 03 Где замок.
import random


random.seed(42)
f = open('A.txt')
raw_data = f.read().strip()
data = raw_data.replace(',', '.').split('\n')
points = [[float(i) for i in pair.split()] for pair in data if 'X' not in pair]


class Castle:
    def __init__(self, k=2, max_iters=100, tolerance=1e-4):
            self.k = k
            self.max_iters = max_iters
            self.tolerance = tolerance
            self.centroids = []
            self.clusters = []

    def fit(self, data):
        for i in range(self.k):
            self.centroids.append([random.randint(0, 100), random.randint(0, 100)])
        self.clusters = [[] for i in range(self.k)]
        for point in data:
            if self._calculate_distance(point, self.centroids[0]) < self._calculate_distance(point, self.centroids[1]):
                self.clusters[0].append(point)
            else:
                self.clusters[1].append(point)
    

    def predict(self, data):
         pass # предсказание модели


    def _assign_clusters(self, data):
        pass  # внутренний метод

    def _calculate_distance(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# print(points)

clust = Castle()
clust.fit(points)
print(clust.centroids)