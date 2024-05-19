
# app.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

WEATHER_API_KEY = 'efe235c950d14d05bbe215008241905'
WEATHER_API_URL = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=Presidente Prudente'

@app.route('/')
def index():
    weather_data = fetch_weather()
    return render_template('index.html', weather=weather_data)

def fetch_weather():
    try:
        response = requests.get(WEATHER_API_URL)
        response.raise_for_status()
        data = response.json()
        weather = {
            'location': data['location']['name'],
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
        return weather
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)


