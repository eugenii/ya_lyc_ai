# 02 детектор агрессии.
import string
from math import exp


AGGRO_WORDS = {
    "дурак": 2.0,
    "достал": 1.1,
    "глупый": 0.5,
    "наивный": 0.7,
    "ужасный": 1.9,
    "ненавижу": 2.7,
    "сказку": -0.25
} 


def normalize_text(text):
    lowered = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    return lowered.translate(translator)


def sigmoid(z):
    return 1 / (1 + exp(-z))


def predict_agress(text):
    text = normalize_text(text)	 # приводим высказывание в удобный вид
    score = -1.5    # базовое смещение: по умолчанию высказывание не агрессивное
    probability = 0.0
    is_agress = False
    for word, weight in AGGRO_WORDS.items():
        if word in text:
            score += weight	 # каждое ключевое слово добавляет «доказательства» агрессии
    probability = sigmoid(score)	# переводим итог в вероятность от 0 до 1
    is_agress = probability >= 0.5    # применяем пороговое решение
    return probability, is_agress

probs = [
    'Привет, дурак!',
    'Сестра попросила почитать ей сказку про Ивана-дурака!',
    'Какой же ты глупый!',
    'Какой же сегодня ужасный день!',
    'Я ненавижу его!'
]

# message = input()
for message in probs:
    prob, label = predict_agress(message)
    print(message)
    print("Вероятность агрессии: {:.2f}".format(prob))
    print(label)

# messages = [
#     'Привет, дурак!',
#     'Сестра попросила почитать ей сказку про Ивана-дурака!',
#     'Какой же ты глупый!',
#     'Какой же сегодня ужасный день!',
#     'Я ненавижу его!'
# ]

# for message in messages:
#     prob, label = predict_agress(message)
#     print(f"Вероятность агрессии: {prob:.2f}")
#     print("Это агрессия" if label else "Это нормально..")
