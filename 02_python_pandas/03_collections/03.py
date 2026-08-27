words = []
while word := input():
    words.append(word)
words = list(reversed(words))
m = len(max(words, key=len))
for word in words:
    left = (m - len(word)) // 2
    right = m - len(word) - left
    print('-' * left, word, '-' * right, sep='')