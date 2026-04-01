# 01 Сигмоида.
from math import exp

w0 = 0.2
w1 = 0.5
x = 2


def z(x):
    return w0 + w1 * x


def sigmoid(z):
    return 1 / (1 + exp(-z))


print(round(sigmoid(z(x)), 2))