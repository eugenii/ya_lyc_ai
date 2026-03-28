# 03  Предсказание модели.
import numpy as np

count = int(input())

weights = np.array([float(i) for i in input().split()])

real = np.array([float(i) for i in input().split()])

def predict(x):
    return weights[0] + np.dot(weights[1:], x)

for _ in range(count):
    x = np.array([float(i) for i in input().split()])
    print(predict(x))