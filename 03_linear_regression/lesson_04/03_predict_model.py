# 03  Предсказание модели.
import numpy as np

count = int(input())

weights = np.array([float(i) for i in input().split()])

real = np.array([float(i) for i in input().split()])


def predict(x):
    return weights[0] + np.dot(weights[1:], x)


def mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)


predicts = []
errors = []
for _ in range(count):
    x = np.array([float(i) for i in input().split()])
    predicts.append(predict(x))


result = np.linalg.norm(real - predicts)

print(result.round(2))