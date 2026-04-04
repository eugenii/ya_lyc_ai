# Ошибки.


y_predict = [0.25, 0.38, 0.85, 0.60, 0.50]
y_real = [0, 1, 1, 0, 0]
treshhold = 0.4

# mistakes = [1 if abs(y_predict[i] - y_real[i]) > treshhold else 0 for i in range(len(y_predict))]
mistakes = []

for pred in range(len(y_predict)):
    if abs(y_predict[pred] - y_real[pred]) > treshhold:
        mistakes.append(1)
    else:
        mistakes.append(0)

print(sum(mistakes))