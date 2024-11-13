

def buildQuery(weatherCode, temp, humid, windspeed, precip, cloudspercentage, lat, lon):
    
    query = f"""Create a picture of landscape with focus on the weather. The weather and landscape should fit the given location. The location is
    at latitude {lat} and longitude {lon}.
      The weather is {weatherCode}, it is {temp} degrees celsius, the humidity is {humid} percent, the wind speed is {windspeed},
      the amount of downfall is {precip} and the sky has a {cloudspercentage} percentage cloud coverage"""
    
    return query

def buildTextQuery(weatherCode, temp, humid, windspeed, precip, cloudspercentage, lat, long):
    
    query = f"""Give short helpful recommendations on what clothes to wear and what to take care of in the given weather.
      Do not respond with any questions at all, assume i am unable to further message you. The response should not be longer than 10 lines and not more than 100 tokens.
      Before writing the recommendation, list the details of the weather that i provide to you. List the details in a systematic list. 
      Including all the details like temperature, type of weather, downfall in mm and windspeed. Also list the location (country, or city) if possible
      The recommendation should be tailored for the location. The location this is relevant for is at latitude {lat} and longitude {long}.
      The following is the weather information:
      The weather is {weatherCode}, it is {temp} degrees celsius, the humidity is {humid} percent, the wind speed is {windspeed} m/s,
      the amount of downfall is {precip} and the sky has a {cloudspercentage} percentage cloud coverage"""
   
    return query