import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


raw_data = pd.read_csv('high_popularity_spotify_data.csv')
data = raw_data[['energy', 'danceability']]
# print(data.info())
scaler = StandardScaler()

data_scaled = scaler.fit_transform(data) 


model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(data_scaled)              
cluster_centers = model.cluster_centers_
centers = scaler.inverse_transform(cluster_centers)

# Создание DataFrame для центроидов
df_centers = pd.DataFrame(centers, columns=['energy', 'danceability'])

# Сохранение центроидов в файл centroids.csv
df_centers.to_csv('centroids.csv', index=False, float_format='%.3f')

# print("Центроиды успешно сохранены в centroids.csv")
# print(cluster_centers)
