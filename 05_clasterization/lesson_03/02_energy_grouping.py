import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler


raw_data = pd.read_csv('high_popularity_spotify_data.csv')
data = raw_data[['energy', 'speechiness', 'instrumentalness']]

scaler = StandardScaler()

data_scaled = scaler.fit_transform(data)    

dbscan_all = []

max_clusters = 0
for min_sample in range(3, 10):
    dbscan = DBSCAN(eps=0.4, min_samples=min_sample)
    dbscan.fit_predict(data_scaled)
    labels = dbscan.labels_
    if len(labels) > max_clusters:
        max_clusters = len(labels)
    noise_part = sum(labels == -1) / len(labels)
    dbscan_all.append((len(labels), min_sample, noise_part))

result = [(max_clusters, min_sample, float(noise_part)) for (max_clusters, min_sample, noise_part) 
          in dbscan_all if (max_clusters == min_sample) and noise_part < 0.2]

print(dbscan_all)
print(result)


