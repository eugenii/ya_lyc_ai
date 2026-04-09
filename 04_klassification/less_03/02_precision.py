import numpy as np

y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])

def precision(y_true, y_pred):
    tp = 0
    fp = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            if y_true[i] == 1:
                tp += 1
        if y_true[i] != y_pred[i]:
            if y_true[i] == 1:
                fp += 1
    return tp / (tp + fp)

result = precision(y_true, y_pred)
print('precision: {:.3f}'.format(result))