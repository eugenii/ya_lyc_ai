# Биграммы. без nltk
import string

stop_words = ['в', 'на', 'а', 'из']

text = input().lower()

text_no_punct = text.translate(str.maketrans('', '', string.punctuation))

words = [word for word in text_no_punct.lower().split() if word not in stop_words]

bigrams = set()

for i in range(len(words)):
    bigrams.add(words[i])
    if i < len(words) - 1:
        bigrams.add(words[i] + ' ' + words[i + 1])
sorted_bigrams = list(bigrams)
sorted_bigrams.sort()
print(*sorted_bigrams, sep='\n')