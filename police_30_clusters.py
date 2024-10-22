import pandas as pd
from sklearn.cluster import KMeans
import os

# Load the data
data = pd.read_csv('geocoded_police_2023.csv')

# Assuming the CSV has 'latitude' and 'longitude' columns
coordinates = data[['Latitude', 'Longitude']]

# Perform KMeans clustering
kmeans = KMeans(n_clusters=30, random_state=42)
data['cluster'] = kmeans.fit_predict(coordinates)

# Get the cluster centers
centers = kmeans.cluster_centers_

# Save the cluster centers to a new CSV file
cluster_centers_df = pd.DataFrame(centers, columns=['latitude', 'longitude'])
cluster_centers_df.to_csv('2023_policecalls_30clusters.csv', index=False)

print("Cluster centers saved to 2023_policecalls_30clusters.csv")