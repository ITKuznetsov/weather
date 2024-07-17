from django.db import models
import requests
from geopy.geocoders import Nominatim


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_city_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    return None, None

def get_weather(city):
    latitude, longitude = get_city_coordinates(city)
    if latitude is None or longitude is None:
        return None

    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Europe/Moscow"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    weather_data = response.json()
    forecast = weather_data.get('daily', {})

    structured_weather_data = {
        'city': city,
        'forecast': [
            {
                'day': 'Сегодня',
                'max_temp': forecast['temperature_2m_max'][0],
                'min_temp': forecast['temperature_2m_min'][0],
                'precipitation': forecast['precipitation_sum'][0],
            },
            {
                'day': 'Завтра',
                'max_temp': forecast['temperature_2m_max'][1],
                'min_temp': forecast['temperature_2m_min'][1],
                'precipitation': forecast['precipitation_sum'][1],
            },
            {
                'day': 'Послезавтра',
                'max_temp': forecast['temperature_2m_max'][2],
                'min_temp': forecast['temperature_2m_min'][2],
                'precipitation': forecast['precipitation_sum'][2],
            },
        ]
    }
    
    return structured_weather_data


