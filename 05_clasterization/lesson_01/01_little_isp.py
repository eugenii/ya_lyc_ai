# 01 Маленькое вступление.
import numpy as np

# координаты точек
X = np.array([5, 6, 2, 2, 5, 4, 4, 7, 6, 6])
Y = np.array([5, 4, 4, 0, 8, 5, 3, 7, 2, 5])

x_mean = np.mean(X)
y_mean = np.mean(Y)

dist = np.sqrt((x_mean)**2 + (y_mean)**2)
dist2 = np.linalg.norm([x_mean, y_mean])
print(dist, dist2.round(0))