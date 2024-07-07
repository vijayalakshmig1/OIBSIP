import urllib.request
import json

def get_weather(city):
    api_key = '27b0c771406b50bba222803735812347'# Using OpenWeather App 
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        # Send a GET request to the API
        with urllib.request.urlopen(base_url) as url:
            data = json.loads(url.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)

    if weather_data:
        if weather_data.get('cod') == 200:
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            print(f'Weather in {city}:')
            print(f'Description: {weather_description}')
            print(f'Temperature: {temperature}°C')
            print(f'Humidity: {humidity}%')
            print(f'Wind Speed: {wind_speed} m/s')
        else:
            print(f"Error: {weather_data.get('message')}")
    else:
        print("Failed to fetch weather data. Please try again.")

if __name__ == '__main__':
    main()
