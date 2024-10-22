import pandas as pd
import requests
from dotenv import load_dotenv
import os
import time

# Load API key from .env file
load_dotenv()
google_api_key = os.getenv("googleapi")

# Define the function to geocode addresses using Google API
def geocode_address(address, city, state, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    full_address = f"{address}, {city}, {state}"
    params = {
        "address": full_address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

# Load the dataset
df = pd.read_csv("policecalls2023.csv")

# Initialize empty lists to store latitudes and longitudes
latitudes = []
longitudes = []

# Loop through the dataset and geocode each address
for index, row in df.iterrows():
    address = row['ADDRESS']
    city = row['CITY']
    state = row['STATE']
    lat, lng = geocode_address(address, city, state, google_api_key)
    latitudes.append(lat)
    longitudes.append(lng)
    
    # Adding a slight delay to prevent hitting the request limit
    time.sleep(0.1)

# Add the latitudes and longitudes to the dataframe
df['LATITUDE'] = latitudes
df['LONGITUDE'] = longitudes

# Save the new dataset to a CSV file
df.to_csv("geocoded_police_2023.csv", index=False)

print("Geocoding complete. File saved as 'geocoded_police_2023.csv'")
