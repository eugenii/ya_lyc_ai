# 04 Интерпретация результатов кластеризации
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

RANDOM_STATE = 42

# Загрузка данных
raw_data = pd.read_csv('../high_popularity_spotify_data.csv')

# Выбор признаков
features = ['energy', 'danceability', 'tempo', 'loudness', 'valence', 'acousticness', 'speechiness']
data = raw_data[features]

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# PCA
pca = PCA(n_components=3, random_state=RANDOM_STATE)
X_pca = pca.fit_transform(X_scaled)  # Получаем спроецированные данные

# Loadings (компоненты)
loadings = pca.components_.T  # Транспонируем, чтобы строки - признаки, столбцы - PC

# 1. Для каждой PC находим признак с максимальным абсолютным loading
max_loadings_indices = np.argmax(np.abs(loadings), axis=0)  # индекс для каждой PC
max_loadings_features = [features[idx] for idx in max_loadings_indices]

print("Признаки с максимальной нагрузкой для каждой PC:")
for i, (feature, pc_num) in enumerate(zip(max_loadings_features, range(1, 4))):
    print(f"PC{pc_num}: {feature} (loading = {loadings[max_loadings_indices[i], i]:.4f})")

# 2. Проецируем данные на 2 компоненты (первые две)
X_2d = X_pca[:, :2]

# 3. KMeans на X_2d
kmeans = KMeans(n_clusters=4, random_state=RANDOM_STATE, n_init=10)
clusters = kmeans.fit_predict(X_2d)

# 4. Silhouette score
sil_score = silhouette_score(X_2d, clusters)
print(f"\nSilhouette Score: {sil_score:.4f}")

# 5. Создаем DataFrame для loadings
loadings_df = pd.DataFrame({
    'PC1_loading': np.round(loadings[:, 0], 4),
    'PC2_loading': np.round(loadings[:, 1], 4),
    'PC3_loading': np.round(loadings[:, 2], 4),
    'feature': features
})

# 6. Добавляем строку с silhouette_score
# Создаем новую строку как словарь
sil_row = pd.DataFrame({
    'PC1_loading': [np.round(sil_score, 4)],
    'PC2_loading': [0],
    'PC3_loading': [0],
    'feature': ['silhouette_score']
})

# Добавляем строку в DataFrame
loadings_df = pd.concat([loadings_df, sil_row], ignore_index=True)

# Сохраняем в CSV
loadings_df.to_csv('loadings.csv', index=False)

print("\nloadings.csv успешно создан!")
print("\nПервые несколько строк файла:")
print(loadings_df.head())

# Дополнительно: выведем информацию о кластеризации
print(f"\nРаспределение по кластерам:")
print(pd.Series(clusters).value_counts().sort_index())