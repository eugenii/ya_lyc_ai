# f1_score
import numpy as np

y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])


def conf_matrix(y_pred, y_true):
    global tp, fn, fp, tn
    if y_pred == y_true:
        if y_pred == 1:
            tp += 1
        else:
            tn += 1
    if y_pred != y_true:
        if y_pred == 1:
            fp += 1
        else:
            fn += 1


def f1_score(y_pred, y_true):
    if len(y_pred) != len(y_true):
        return 0
    if len(y_pred) == 0:
        return 0
    
    global tp, fn, fp, tn
    for i in range(len(y_pred)):
        conf_matrix(y_pred[i], y_true[i])
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * precision * recall / (precision + recall)

tp = 0
fn = 0
fp = 0
tn = 0

result = f1_score(y_pred, y_true)
print('f1_score: {:.3f}'.format(result))