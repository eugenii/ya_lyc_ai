# Пациенты.

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


y_pred = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
y_true = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1]

tp = 0
fn = 0
fp = 0
tn = 0

for i in range(len(y_pred)):
    conf_matrix(y_pred[i], y_true[i])

print(tp, fn, fp, tn)

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * precision * recall / (precision + recall)
print(round(f1_score, 2))