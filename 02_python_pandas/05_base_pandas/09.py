# Рейтинг выше 8.77. (Сумма годов всех таких фильмов)
import pandas as pd

df = pd.read_csv('../data/kinopoisk-top250.csv')

df_high_rating = df[df['rating_ball'] > 8.77]

result = df_high_rating['year'].sum()

print(result)
