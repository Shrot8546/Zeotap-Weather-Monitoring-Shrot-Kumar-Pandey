# weather_data.py
import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    """Fetch weather data for a given city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Convert temperature to Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve weather data for {city}: {response.status_code}")
        return None

def get_weather_for_all_cities():
    """Fetch weather data for all specified cities."""
    weather_data = {}
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data[city] = data
    return weather_data

# weather_data.py
from collections import defaultdict

def process_weather_data(weather_data):
    """Calculate daily aggregates for the provided weather data."""
    temp_data = defaultdict(list)
    condition_count = defaultdict(int)
    
    for city, data in weather_data.items():
        temp_data['temperature'].append(data['main']['temp'])
        temp_data['max_temp'].append(data['main']['temp_max'])
        temp_data['min_temp'].append(data['main']['temp_min'])
        condition_count[data['weather'][0]['main']] += 1
    
    # Calculate daily aggregates
    avg_temp = sum(temp_data['temperature']) / len(temp_data['temperature'])
    max_temp = max(temp_data['max_temp'])
    min_temp = min(temp_data['min_temp'])
    dominant_condition = max(condition_count, key=condition_count.get)
    
    return {
        'average_temperature': avg_temp,
        'maximum_temperature': max_temp,
        'minimum_temperature': min_temp,
        'dominant_condition': dominant_condition
    }
