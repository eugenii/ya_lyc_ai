import pandas as pd

df = pd.read_csv('../data/kinopoisk-top250.csv')

print(df.info())

df_sort_by_years = df.sort_values(by=['year', 'rating_ball'], ascending=[False, False])
result_df = (df_sort_by_years['movie'].head(1), df_sort_by_years['movie'].tail(1))

print(*result_df, sep='\n')