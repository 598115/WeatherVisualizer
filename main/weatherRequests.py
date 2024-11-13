import requests
import json


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
