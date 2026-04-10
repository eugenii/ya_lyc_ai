# 05 Трешхолд (порог).
import numpy as np


y_true = np.array([int(i) for i in input().split()])

y_prob = np.array([float(i) for i in input().split()])

thresholds = np.unique(y_prob)
thresholds = np.concatenate([[0], thresholds, [1]])

f1_scores = []
best_threshold = None
best_f1 = -1  # Инициализируем минимальным значением

for threshold in thresholds:
    y_pred = (y_prob >= threshold).astype(int)
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        # Сохранение F1-score и обновление лучшего threshold
    if f1 > best_f1 or (f1 == best_f1 and threshold > best_threshold):
        best_f1 = f1
        best_threshold = threshold

# Вывод результата с тремя знаками после запятой
print(f"{best_threshold:.3f} {best_f1:.3f}")