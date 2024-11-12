import requests
import json

# Coordinates for Bergen. Temporary before user can input own location
latitude = 60.39
longitude = 5.32

# API endpoint
url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

# User identifier
headers = {
    'User-Agent': 'WeatherVisualizer/0.1 github.com/598115/WeatherVisualizer'
}

# Location parameters
params = {
    'lat': latitude,
    'lon': longitude
}

def makeWeatherDataRequest(url, headers, params):

    # Request
    response = requests.get(url, headers=headers, params=params)

    # Respone handling
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Process the data as neededc
        with open('weather_data.json', 'w') as file:
            json.dump(data, file, indent=2)
    else:
        print(f"Error: {response.status_code}")

makeWeatherDataRequest(url, headers, params)