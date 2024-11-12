from weatherJsonReader import WeatherDataParser
from chatGPTRequest import generateImage, generateText
from queryBuilder import buildQuery, buildTextQuery

def appfunction():

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
    picquery = buildQuery(weather_code, temperature, humidity, windspeed, precip, cloud_fraction)
    textquery = buildTextQuery(weather_code, temperature, humidity, windspeed, precip, cloud_fraction)

    # Generate the image based on the query
    #image = generateImage(picquery)
    image = 'standin.png'
    #text = generateText(textquery)
    text = "Test text"

    return image, text