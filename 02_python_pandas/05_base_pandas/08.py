# Три самых плодотворных года. Сумма количества фильмов.
import pandas as pd

df = pd.read_csv('../data/kinopoisk-top250.csv')

df_by_films_count = df.value_counts('year', ascending=False).head(3)
print(df_by_films_count)
