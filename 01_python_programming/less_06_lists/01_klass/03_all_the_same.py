# 03 Все равны.

data = []

while word := input():
    data.append(word)
max_len = len(max(data, key=len))

for word in data[::-1]:
    left = (max_len - len(word)) // 2
    right = max_len - len(word) - left
    print("-" * left + word + "-" * right)