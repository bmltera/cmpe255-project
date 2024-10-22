import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the data from combinedpolicecrash.csv
df = pd.read_csv('combinedpolicecrash.csv')

# Extract the Latitude and Longitude for clustering
X = df[['Latitude', 'Longitude']].dropna()

# Apply KMeans clustering with 30 clusters
kmeans = KMeans(n_clusters=30, random_state=42)
df['Cluster'] = kmeans.fit(X)

# Initialize a list to store ratios
ratios = []

print("Police to Traffic Ratios for each cluster:")

# Loop over each cluster to calculate the adjusted ratio
for cluster_num in range(30):
    cluster_data = df[df['Cluster'] == cluster_num]
    
    # Count the number of 'police' and 'traffic' entries
    police_count = cluster_data[cluster_data['typeofdata'] == 'police'].shape[0]
    traffic_count = cluster_data[cluster_data['typeofdata'] == 'traffic'].shape[0]
    
    # Adjust the police count by dividing by 3
    adjusted_police_count = police_count / 3
    
    # Calculate the ratio
    if traffic_count > 0:
        ratio = adjusted_police_count / traffic_count
    else:
        # Avoid division by zero; set ratio to NaN or a specific value
        ratio = np.nan  # or set to 0 or some indicative value
    
    ratios.append(ratio)
    print(f"Cluster {cluster_num}: Police to Traffic Ratio = {ratio}")

# Add the ratios to the DataFrame for plotting
# Map each cluster to its ratio
cluster_ratios = {cluster_num: ratio for cluster_num, ratio in enumerate(ratios)}
df['Ratio'] = df['Cluster'].map(cluster_ratios)

# Plot the clusters, coloring by the Police to Traffic ratio
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['Longitude'], df['Latitude'], c=df['Ratio'], cmap='coolwarm', edgecolor='k', alpha=0.7)

plt.colorbar(scatter, label='Adjusted Police to Traffic Ratio')
plt.title('Clusters of Combined Police and Traffic Data with Adjusted Ratios')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()