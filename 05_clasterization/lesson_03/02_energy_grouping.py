import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Загрузка данных
raw_data = pd.read_csv('high_popularity_spotify_data.csv')
data = raw_data[['energy', 'speechiness', 'instrumentalness']]

# Масштабирование
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Хранение результатов
results = []

for min_samples in range(3, 11):  # от 3 до 10 включительно
    dbscan = DBSCAN(eps=0.4, min_samples=min_samples)
    labels = dbscan.fit_predict(data_scaled)
    
    # Число кластеров (без шума)
    unique_labels = set(labels)
    n_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
    
    # Доля шума
    noise_ratio = np.sum(labels == -1) / len(labels)
    noise_ratio_rounded = round(noise_ratio, 4)
    
    results.append({
        'min_samples': min_samples,
        'n_clusters': n_clusters,
        'noise_ratio': noise_ratio_rounded
    })
    
    print(f"min_samples={min_samples}, кластеров={n_clusters}, шум={noise_ratio_rounded}")

# Выбор min_samples с максимальным числом кластеров и долей шума < 0.2
valid_results = [r for r in results if r['noise_ratio'] < 0.2]

if valid_results:
    max_clusters_val = max(r['n_clusters'] for r in valid_results)
    candidates = [r for r in valid_results if r['n_clusters'] == max_clusters_val]
    # Если несколько, берём минимальное min_samples
    best = min(candidates, key=lambda x: x['min_samples'])
    
    print(f"\nРезультат: {best['min_samples']},{best['n_clusters']},{best['noise_ratio']:.4f}")
else:
    print("Нет подходящих вариантов с долей шума < 0.2")

# >3,12,0.0397<


