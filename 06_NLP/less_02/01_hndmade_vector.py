import string
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
# Обработка текстов
stop_words = set(stopwords.words('russian'))

data = {0: "робот", 1: "потом", 2: "плотно", 3: "закрыл", 4: "открыл", 5: "здание", 6: "дверь", 7: "зашёл", 8: "вышел", 9: "дом"}

text = "Робот открыл дверь, потом робот зашёл в здание и плотно закрыл дверь"

text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
text_no_stop = [word for word in text_no_punct.lower().split() if word not in stop_words]
print(text_no_stop)
print("потом" in stop_words)
set.remove(stop_words, "потом")
print("потом" in stop_words)
counts = Counter(text_no_stop)
res = ''
for key, value in data.items():
    if value in counts:
        res += str(counts[value])
    else:
        res += '0'

print(','.join(res))

