# 02 Выбери меня.
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
raw_data = pd.read_csv('../high_popularity_spotify_data.csv')

data = raw_data[['loudness', 'instrumentalness', 'speechiness', 'liveness', 'energy', 'tempo']]

scaler = StandardScaler()

data_scaled = scaler.fit_transform(data)

pca = PCA(random_state=RANDOM_STATE)

X_pca = pca.fit(data_scaled)

res = pca.explained_variance_ratio_
# res.sort()
print('{:.4f},{:.4f},{:.4f}'.format(*res[:3]))