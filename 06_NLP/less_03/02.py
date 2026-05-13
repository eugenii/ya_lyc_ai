import gensim.downloader as api

# Загружаем Word2Vec, обученный на Google News (1.6 GB, может занять время)
model = api.load("word2vec-google-news-300")

print("Модель загружена!")
# print(f"Размер словаря: {len(model)} слов")
# print(f"Размерность вектора: {model.vector_size}")
# print(f"Самое похожее на 'cat': {model.most_similar('cat')}")

# similarity = model.similarity("cat", "dog")
for  word in ('call', 'battery', 'mobile', 'screen', 'voice'):
    similarity = model.similarity(word, "phone")
    print(f"Схожесть '{word}', 'phone': {similarity}")