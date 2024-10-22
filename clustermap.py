import pandas as pd

# Step 1: Read the CSV files
police_data = pd.read_csv('geocoded_police_2023.csv')
traffic_data = pd.read_csv('hitnrun_crash_2023.csv')

# Add a column to identify the type of data
police_data['typeofdata'] = 'police'
traffic_data['typeofdata'] = 'traffic'

# Select only the relevant columns
police_data = police_data[['Latitude', 'Longitude', 'typeofdata']]
traffic_data = traffic_data[['Latitude', 'Longitude', 'typeofdata']]

# Combine the two DataFrames
combined_data = pd.concat([police_data, traffic_data], ignore_index=True)

# Output to combinedpolicecrash.csv
combined_data.to_csv('combinedpolicecrash.csv', index=False)

print("Combined data saved to combinedpolicecrash.csv")