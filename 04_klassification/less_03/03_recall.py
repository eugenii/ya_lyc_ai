import numpy as np

y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])

def recall(y_true, y_pred):
    if len(y_true) != len(y_pred):
        return 0
    if len(y_true) == 0:
        return 0
    tp = 0
    fn = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            if y_true[i] == 1:
                tp += 1
        if y_true[i] != y_pred[i]:
            if y_true[i] == 1:
                fn += 1
    return tp / (tp + fn)


result = recall(y_true, y_pred)
print('recall: {:.3f}'.format(result))