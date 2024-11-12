import json
from datetime import datetime, timezone

class WeatherDataParser:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.json_data = file.read()
        self.data = json.loads(self.json_data) if isinstance(self.json_data, str) else self.json_data
        self.current_time_data = self._get_current_time_data()

    def _get_current_time_data(self):
        # Use timezone-aware UTC datetime
        current_time = datetime.now(timezone.utc).isoformat()
        for entry in self.data['properties']['timeseries']:
            if entry['time'] >= current_time:
                return entry['data']
        return None

    def get_temperature(self):
        return self.current_time_data.get("instant", {}).get("details", {}).get("air_temperature", "N/A")

    def get_wind_speed(self):
        return self.current_time_data.get("instant", {}).get("details", {}).get("wind_speed", "N/A")

    def get_humidity(self):
        return self.current_time_data.get("instant", {}).get("details", {}).get("relative_humidity", "N/A")

    def get_cloud_area_fraction(self):
        return self.current_time_data.get("instant", {}).get("details", {}).get("cloud_area_fraction", "N/A")

    def get_precipitation_next_1_hour(self):
        # Get precipitation amount for the next 1 hour
        return self.current_time_data.get("next_1_hours", {}).get("details", {}).get("precipitation_amount", 0)

    def get_symbol_code(self):
        # Get the symbol code for the type of weather (e.g., "lightrain", "cloudy", etc.)
        return self.current_time_data.get("next_1_hours", {}).get("summary", {}).get("symbol_code", "N/A")

# Example usage

parser = WeatherDataParser('weather_data.json')
print("Temperature:", parser.get_temperature())
print("Wind Speed:", parser.get_wind_speed())
print("Humidity:", parser.get_humidity())
print("Cloud Area Fraction:", parser.get_cloud_area_fraction())
print("Precipitation (next 1 hour):", parser.get_precipitation_next_1_hour())
print("Weather Symbol Code:", parser.get_symbol_code())
