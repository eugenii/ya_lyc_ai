import pandas as pd

df = pd.read_csv('../data/kinopoisk-top250.csv')

common_avg = df['rating_ball'].mean() # 8.4693
common_rating_round = common_avg.round(3)

print(common_rating_round)
