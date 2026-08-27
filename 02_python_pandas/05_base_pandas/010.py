# Количество фильмов в 2000 году.
import pandas as pd

df = pd.read_csv('../data/kinopoisk-top250.csv')

df_2000 = df[df['year'] == 2000]

print(len(df_2000))