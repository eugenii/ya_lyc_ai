import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('high_popularity_spotify_data.csv')

data = data[['energy', 'loudness', 'acousticness']]

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data) 
K = np.arange(1, 11)
inertias = []

for k in K:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(data_scaled)              
    inertias.append(model.inertia_)  

    
differences = [inertias[i-1] - inertias[i] for i in range(1, len(inertias))],

second_diff = [differences[0][i-1] - differences[0][i] for i in range(1, len(differences[0]))]

optimal_k = np.argmax(second_diff) + 2

plt.plot(K, inertias, marker='o')
plt.xlabel('Число кластеров k')
plt.ylabel('WCSS (inertia)')
plt.title('Метод локтя')
plt.show()

print("!", differences)
print("!", second_diff)
print(optimal_k)