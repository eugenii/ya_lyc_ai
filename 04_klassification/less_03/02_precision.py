import numpy as np

y_true = np.array([int(i) for i in input().split()])
y_pred = np.array([int(i) for i in input().split()])


def precision(y_true, y_pred):
    # Вычисляем True Positives (TP) и False Positives (FP)
    tp = np.sum((y_true == 1) & (y_pred == 1))  # TP: истинные значения = 1 И предсказанные значения = 1
    fp = np.sum((y_true == 0) & (y_pred == 1))  # FP: истинные значения = 0 И предсказанные значения = 1
    
    # Гарантируется, что TP > 0, поэтому деление безопасно
    return tp / (tp + fp)


result = precision(y_true, y_pred)
print('precision: {:.3f}'.format(result))