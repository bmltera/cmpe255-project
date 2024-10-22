import pandas as pd
import os
from dotenv import load_dotenv
import gmplot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

# Load environment variables
load_dotenv()
API_KEY = os.getenv("googleapi")

# Read coordinates from CSV
coords_df = pd.read_csv('2023_hitnrun_30clusters.csv')

# Assuming the CSV has 'latitude' and 'longitude' columns
latitudes = coords_df['latitude']
longitudes = coords_df['longitude']

# Create a map centered around San Jose
gmap = gmplot.GoogleMapPlotter(37.3382, -121.8863, 13, apikey=API_KEY)

# Overlay the coordinates
gmap.scatter(latitudes, longitudes, color='red', size=40, marker=False)

# Save the map as an HTML file temporarily
html_file = "san_jose_map.html"
gmap.draw(html_file)

# Set up Selenium to take a screenshot
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_service = Service('path/to/chromedriver')  # Update with your ChromeDriver path
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the HTML file in the browser
driver.get(f"file://{os.path.abspath(html_file)}")

# Wait for the map to render
time.sleep(5)  # Adjust time if necessary

# Take a screenshot
screenshot_file = "san_jose_map.png"
driver.save_screenshot(screenshot_file)

# Close the browser
driver.quit()

# Optionally, you can crop the image if needed
# img = Image.open(screenshot_file)
# img_cropped = img.crop((left, top, right, bottom))  # Define your crop box
# img_cropped.save("san_jose_map_cropped.png")

print(f"Map screenshot saved as {screenshot_file}")