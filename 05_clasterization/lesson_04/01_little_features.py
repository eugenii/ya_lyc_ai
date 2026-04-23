# 01 Маленькие признаки.
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
raw_data = pd.read_csv('../high_popularity_spotify_data.csv')

data = raw_data[['energy', 'tempo', 'danceability', 'loudness']]

scaler = StandardScaler()

data_scaled = scaler.fit_transform(data)

pca = PCA(n_components=2, random_state=RANDOM_STATE)

pca.fit(data_scaled)

res1 = pca.explained_variance_ratio_[0]
res2 = pca.explained_variance_ratio_[1]

print('{:.4f},{:.4f}'.format(res1, res2))    # 0.4353,0.2822