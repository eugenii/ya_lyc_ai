import numpy as np

y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])

def recall(y_true, y_pred):
    if len(y_true) != len(y_pred):
        return 0
    if len(y_true) == 0:
        return 0
    tp = np.sum((y_true == 1) & (y_pred == 1))  # TP: истинные значения = 1 И предсказанные значения = 1
    fn = np.sum((y_true == 1) & (y_pred == 0))  # FP: истинные значения = 0 И предсказанные значения = 1

    return tp / (tp + fn)


result = recall(y_true, y_pred)
print('recall: {:.3f}'.format(result))