import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('combinedpolicecrash.csv')

# Assuming the coordinates are in columns named 'Latitude' and 'Longitude'
coordinates = data[['Latitude', 'Longitude']].dropna()

# Step 2: Cluster the data into 30 clusters
kmeans = KMeans(n_clusters=30, random_state=42)
data['cluster'] = kmeans.fit(coordinates)

# Calculate the adjusted ratio of police to traffic tags for each cluster
cluster_ratios = data.groupby('cluster').apply(
    lambda x: ((x['typeofdata'] == 'police').sum() / 3) / (x['typeofdata'] == 'traffic').sum() if (x['typeofdata'] == 'traffic').sum() > 0 else 0
)

# Print the ratios
for cluster, ratio in cluster_ratios.items():
    print(f'Cluster {cluster}: Adjusted Police to Traffic Ratio = {ratio:.2f}')

# Plotting the clusters
plt.figure(figsize=(12, 8))
plt.scatter(data['Longitude'], data['Latitude'], c=data['cluster'], cmap='viridis', marker='o', alpha=0.5)

# Plot the cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 1], centers[:, 0], c='red', marker='X', s=200, label='Cluster Centers')

plt.title('K-means Clustering of Police and Traffic Data')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='Cluster Label')
plt.legend()
plt.grid()
plt.show()