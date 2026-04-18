import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('high_popularity_spotify_data.csv')

X = df[['energy', 'danceability']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# центроиды (в масштабированном пространстве, но инвертируем для оригинальных единиц)
centroids_scaled = kmeans.cluster_centers_
centroids = scaler.inverse_transform(centroids_scaled)

centroids_df = pd.DataFrame(centroids, columns=['energy', 'danceability'])
centroids_df.to_csv('centroids.csv', index=False, float_format='%.5f')
