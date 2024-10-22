import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read the CSV file
df = pd.read_csv('hitnrun_crash_2023.csv')

# Select relevant features for clustering (Latitude and Longitude)
X = df[['Latitude', 'Longitude']].dropna()  # Drop rows with NaN values

# Perform K-means clustering
n_clusters = 100
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)

# Get the cluster centers
centers = kmeans.cluster_centers_

# Randomly select 30 cluster centers
if len(centers) > 30:
    selected_indices = np.random.choice(len(centers), size=30, replace=False)
    selected_centers = centers[selected_indices]
else:
    selected_centers = centers  # If there are less than 30 clusters, use all

# Visualize only the selected cluster centers as circles
plt.figure(figsize=(12, 8))

# Draw circles around the selected cluster centers
for center in selected_centers:
    circle = plt.Circle((center[1], center[0]), 0.01, color='red', fill=False, linewidth=2)  # Adjust radius as needed
    plt.gca().add_artist(circle)

# Plot the selected cluster centers as red 'X'
plt.scatter(selected_centers[:, 1], selected_centers[:, 0], c='red', marker='X', s=200, label='Selected Cluster Centers')  # X marks for centers

plt.title('Cluster Centers of Crash Data (2023)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid()
plt.legend()
plt.xlim(df['Longitude'].min() - 0.1, df['Longitude'].max() + 0.1)  # Adjust limits for better visibility
plt.ylim(df['Latitude'].min() - 0.1, df['Latitude'].max() + 0.1)  # Adjust limits for better visibility
plt.show()