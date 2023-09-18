import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

api_key = os.getenv('API_KEY')
city = os.getenv('CITY')

threshold = 30
counter = 0

# Construct the API URL
api_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=2'

# Make the API Request
response = requests.get(api_url)

# Parse the Response
data = response.json()

# Extract Cloud Coverage
tomorrow_date = (datetime.now() + timedelta(days=1))

# Extract the sunrise time string from the API response
sunrise_str = data['forecast']['forecastday'][1]['astro']['sunrise']

# Extract time from the sunrise string
sunrise_time = datetime.strptime(sunrise_str.split()[0], '%I:%M')

# Set the date for sunrise_time to match tomorrow_date
sunrise_time = sunrise_time.replace(year=tomorrow_date.year, month=tomorrow_date.month, day=tomorrow_date.day)

noon_time = tomorrow_date.replace(hour=12)

cloud_coverage = []

for hour in data['forecast']['forecastday'][1]['hour']:
    time = datetime.fromisoformat(hour['time'])
    
    # Skip hours before sunrise
    if time < sunrise_time:
        continue
    
    if sunrise_time <= time <= noon_time:
        cloud_percentage = int(hour['cloud'])
        cloud_coverage.append({
            'time': time,
            'cloud_coverage': cloud_percentage,
        })
        
        if cloud_percentage > threshold:
            counter += 1

# Print Cloud Coverage
for entry in cloud_coverage:
    print(f"At {entry['time']}: Cloud Coverage = {entry['cloud_coverage']}%")

# Print the counter
print(f"Cloud coverage exceeded {threshold}% {counter} times.")
