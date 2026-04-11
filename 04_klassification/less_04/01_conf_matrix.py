# 01 Матрица ошибок

import numpy as np

count = int(input())
y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])


def conf_matrix(y_true, y_pred):
    conf_matrix = [[0] * count for i in range(count)]
    for i in range(len(y_true)):
        conf_matrix[y_true[i]][y_pred[i]] += 1
    return np.array(conf_matrix)

print(conf_matrix(y_true, y_pred))
# for row in conf_matrix(y_true, y_pred):
#     print(row)

