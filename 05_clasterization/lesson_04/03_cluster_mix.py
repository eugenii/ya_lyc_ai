# 03 Кластерный микс.
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

RANDOM_STATE = 42

# Загрузка данных
raw_data = pd.read_csv('../high_popularity_spotify_data.csv')

# Выбор признаков
data = raw_data[['danceability', 'energy', 'valence', 'acousticness', 'tempo']]

# Проверка на наличие пропусков
print(data.isna().sum())

# Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# Применение PCA
pca = PCA(n_components=2, random_state=RANDOM_STATE)
X_pca = pca.fit_transform(X_scaled)

# Применение KMeans с PCA
kmeans_pca = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init=10)
labels_pca = kmeans_pca.fit_predict(X_pca)

# Применение KMeans без PCA
kmeans_no_pca = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init=10)
labels_no_pca = kmeans_no_pca.fit_predict(X_scaled)

# Расчет silhouette_score
res_pca = silhouette_score(X_pca, labels_pca)
res_no_pca = silhouette_score(X_scaled, labels_no_pca)

# Вывод результатов
print('{:.4f},{:.4f}'.format(res_pca, res_no_pca))  # должно быть 0.3951,0.2263