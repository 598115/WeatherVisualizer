from weatherJsonReader import WeatherDataParser
from chatGPTRequest import generateImage, generateText
from queryBuilder import buildQuery, buildTextQuery
from weatherRequests import makeWeatherDataRequest
import re

def appfunction(lat, lon):

    # Default coordinates for Bergen.
    defaultlatitude = 60.39
    defaultlongitude = 5.32

     # API endpoint
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

     # User identifier
    headers = {
    'User-Agent': 'WeatherVisualizer/0.1 github.com/598115/WeatherVisualizer'
     }

    if lat != '' and lon != '' and is_valid_lat_lon(lat, coord_type='lat') and is_valid_lat_lon(lat, coord_type='lon'):
          params = {
               'lat': lat,
               'lon': lon
          }
    else:
          params = {
               'lat': defaultlatitude,
               'lon': defaultlongitude
          }
          
    makeWeatherDataRequest(url, headers, params)
    #Getting weather json reader
    weather = WeatherDataParser('weather_data.json')

    # Retrieve the required parameters dynamically
    weather_code = weather.get_symbol_code()
    temperature = weather.get_temperature()
    humidity = weather.get_humidity()
    cloud_fraction = weather.get_cloud_area_fraction()
    windspeed = weather.get_wind_speed()
    precip = weather.get_precipitation_next_1_hour()

    # Build the query
    picquery = buildQuery(weather_code, temperature, humidity, windspeed, precip, cloud_fraction, lat, lon)
    textquery = buildTextQuery(weather_code, temperature, humidity, windspeed, precip, cloud_fraction, lat, lon)

    # Generate the image based on the query
    image = generateImage(picquery)
    text = generateText(textquery)

    return image, text

def is_valid_lat_lon(s, coord_type):
    # Regular expression to match numbers with exactly two decimal places
    pattern = r"^-?\d+\.\d{2}$"
    
    # Check if the string matches the decimal format with two decimal places
    if not re.match(pattern, s):
        return False
    
    # Convert to float and check bounds based on coordinate type
    value = float(s)
    
    if coord_type == 'lat':  # Latitude check
        return -90.00 <= value <= 90.00
    elif coord_type == 'lon':  # Longitude check
        return -180.00 <= value <= 180.00
    else:
        raise ValueError("coord_type must be either 'lat' or 'lon'")