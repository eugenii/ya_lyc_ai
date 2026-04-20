# 01 Акустическое сканирование
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler


raw_data = pd.read_csv('high_popularity_spotify_data.csv')

data = raw_data[['energy', 'acousticness']]

scaler = StandardScaler()

data_scaled = scaler.fit_transform(data)

dbscan = DBSCAN(eps=0.5, min_samples=5)

dbscan.fit_predict(data_scaled)

labels_ = dbscan.labels_

# print(cluster_labels)

labels_count = len(set(labels_[labels_ != -1]))
print(labels_count)

noise_part = sum(labels_ == -1) / len(labels_)

print('{},{:.4f}'.format(labels_count, noise_part))