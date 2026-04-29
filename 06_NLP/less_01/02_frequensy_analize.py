import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Скачиваем необходимые данные
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


df = pd.read_csv('short_imdb.csv', encoding='utf-8')


text_column = 'review'

# Обработка текстов
stop_words = set(stopwords.words('russian'))
# print(stop_words)

def process_text(text):
    if pd.isna(text):
        return []  # возвращаем пустой список
    text_clean = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text_clean.lower(), language='russian')
    return [word for word in tokens if word not in stop_words and len(word) > 1 and word not in('br', 'bbc')]


df['tokens'] = df['review'].apply(process_text)

all_words = [word for tokens in df['tokens'] for word in tokens]
print(all_words[:10])
word_freq = Counter(all_words)
print(word_freq.most_common(5))