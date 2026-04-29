import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')


text = """Бот в потоке путал фразы. Потоком правила катились, 
в датасете сократились. Бот торопился, слова дробились, 
и в смыслы всё же превратились"""

stop_words = set(stopwords.words('russian'))
text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
text_low_no_punct = text_no_punct.lower()   

tokens = word_tokenize(text_low_no_punct, language='russian')
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print(filtered_tokens)
print(len(filtered_tokens))