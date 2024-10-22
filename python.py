import pandas as pd
import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv('googleapi')
counter = 0

if not API_KEY:
    raise ValueError("API key not found. Please set 'googleapi' in your .env file.")
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('misdemeanor.csv')

# Function to geocode an address
def geocode_address(address):

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Prepare the parameters for the request
    params = {
        'address': address,
        'key': API_KEY
    }

    # Encode the parameters and build the request URL
    url = f"{base_url}?{urlencode(params)}"

    try:
        # Send the GET request to the Google Geocoding API
        response = requests.get(url)
        response.raise_for_status()
        geocode_result = response.json()
        counter+=1
        print(counter)
        if geocode_result['status'] == 'OK':
            # Extract latitude and longitude from the response
            location = geocode_result['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"Geocoding error for address '{address}': {geocode_result['status']}")
            return None, None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return None, None

# Create new columns for latitude and longitude
df['Latitude'] = None
df['Longitude'] = None

# Iterate over the DataFrame rows and geocode each address
for index, row in df.iterrows():
    counter+=1
    print(counter)
    address_components = [str(row['ADDRESS']), str(row['CITY']), str(row['STATE'])]
    full_address = ', '.join(filter(None, address_components))
    print(f"Geocoding address: {full_address}")
    lat, lng = geocode_address(full_address)
    df.at[index, 'Latitude'] = lat
    df.at[index, 'Longitude'] = lng

# Save the updated DataFrame to a new CSV file
df.to_csv('geocoded_police_2023.csv', index=False)
print("Geocoding completed. The results have been saved to 'geocoded_police_2023.csv'.")