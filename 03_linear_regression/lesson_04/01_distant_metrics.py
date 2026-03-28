# Метрики расстояния
import numpy as np

euclideans = []
manhattans = []

point = np.array([1, 5])

shops = [(0, 4), (9, 1), (8, 0), (9, 6)]

for shop in shops:
    shop = np.array(shop)
    euclideans.append(np.linalg.norm(shop - point))

for shop in shops:
    shop = np.array(shop)
    manhattans.append(np.sum(np.abs(shop - point)))

print("euclid: {:.2f}".format(min(euclideans)))
print("manhattan: {:.2f}".format(min(manhattans)))



