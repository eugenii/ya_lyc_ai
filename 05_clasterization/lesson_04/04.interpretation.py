# 04 Интерпретация результатов кластеризации
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

RANDOM_STATE = 42

# Загрузка данных
raw_data = pd.read_csv('../high_popularity_spotify_data.csv')

data = raw_data[['energy', 'danceability', 'tempo', 'loudness', 'valence', 'acousticness', 'speechiness']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

pca = PCA(n_components=3, random_state=RANDOM_STATE)
pca.fit(X_scaled)

loadings = pca.components_.T

print(loadings)