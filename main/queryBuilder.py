

def buildQuery(weatherCode, temp, humid, windspeed, precip, cloudspercentage):
    
    query = f"""Create a picture of scandinavian city landscape with focus on the weather.
      The weather is {weatherCode}, it is {temp} degrees celsius, the humidity is {humid} percent, the wind speed is {windspeed},
      the amount of downfall is {precip} and the sky has a {cloudspercentage} percentage cloud coverage"""
    
    return query

def buildTextQuery(weatherCode, temp, humid, windspeed, precip, cloudspercentage):
    
    query = f"""Give short helpful recommendations on what clothes to wear and what to take care of in the given weather.
      Do not respond with any questions at all, assume i am unable to further message you. The response should not be longer than 5 lines and not more than 100 tokens.
      Before writing the recommendation, list the details of the weather that i provide to you. List the details in a systematic list.
      The following is the weather information:
      The location is Norway. The weather is {weatherCode}, it is {temp} degrees celsius, the humidity is {humid} percent, the wind speed is {windspeed},
      the amount of downfall is {precip} and the sky has a {cloudspercentage} percentage cloud coverage"""
   
    return query