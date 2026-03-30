import requests
import json
import os
from config import api_key
from datetime import datetime

FAVORITE_FILE = "favorite.text"

def load_favorites():
    favorites = []
    if os.path.exists(FAVORITE_FILE):
        try:
            with open(FAVORITE_FILE , 'r') as f :
                favorites = [line.strip() for line in f .readlines()]
        except:
            favorites = []
    return favorites

def save_favorites(favorites):
     try:
        with open(FAVORITE_FILE , 'W') as f :
         for city in favorites:
             f.write(city + "\n")
        return True
     except:
         return False
     
def save_to_history(city):
    history = load_history()
    history.append(city)
    if len(history) > 10 :
        history = history[-10:]
    with open("history.txt", "w") as f:
        for c in history:
            f.write( c + "\n")

def load_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    return[]

def show_dashboard(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"

    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        print(f"\n Error : {data['data']['message']}")
        return
    
    temps = []
    dates = []
    conditions = []

    for day in data['forecast']['forecastday']:
        temps.append(day['day']['maxtemp_c'])
        dates.append(day['date'])
        conditions.append(day['day']['condition']['text'])

    print(f"\n Temperature Dashboard - {city.upper()}")
    print("="*50)
    print("\nTemperature graph:\n")
    print("="*50)
    max_temp = max(temps)
    
    for i in range(len(temps)):
        temp = temps[i]
        date = dates[i]
        condition = conditions[i]

        bar_length = int((temp/max_temp)*40)
        print("\n")
        bar = "█"* bar_length + "░" * (40-bar_length)
        short_date = date[5:]

        print(f"{short_date}: {temp:3}C {bar} ({condition})")
    print("\n" +  "="*50)
    print(f"Max: {max(temps)}C | Min: {min(temps)}C | Avg: {sum(temps)/len(temps):.1f}C")

    print("\n Trend:")
    for i in range(len(temps) - 1 ):
        diff = temps[i+1] - temps[i]
        if diff > 0:
            print(f"   Day {i+1} → Day {i+2}: ↑ +{diff}°C (Getting warmer)")
        elif diff < 0:
            print(f"   Day {i+1} → Day {i+2}: ↓ {diff}°C (Getting cooler)")
        else:
            print(f"   Day {i+1} → Day {i+2}: → Stable")
    
    print("="*50)

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            save_to_history(city)

            city_name = data['location']['name']
            country = data['location']['country']
            temp_c = data['current']['temp_c']
            feels_like = data ['current']['feelslike_c']
            humidity = data['current']['humidity']
            condition = data['current']['condition']['text']
            wind_kph = data['current']['wind_kph']

            print("\n"+"-"*45)
            print(f"Weather in {city_name} , {country}")
            print("="*45)
            print(f"Temperature : {temp_c} C")
            print(f"Feels like : {feels_like} C")
            print(f"Humidity : {humidity} %")
            print(f"Condition : {condition}")
            print(f"Wind Speed : {wind_kph} km/h")
            print("-"*45)
            return True

        else:
            print(f"\n {city} Not Found")
            print("Please Check the spelling and try again")
            return False

    except requests.exceptions.ConnectionError:
        print("\n No Internet Connection!")
        return False
    except requests.exceptions.Timeout:
        print("\nRequest timed out , Try Again")
        return False
    except Exception as e :
        print(f"\n Error: {e}")
        return False

print("Weather App")
print("="*35)
print("Get real-time Weather for any city")
print("="*35)

favorites = load_favorites()
print(f"loaded {len(favorites)} favorite cities")

def show_forecast(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"

    try:
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            print(f"\n Error {data['error']['message']}")
            return
        if 'forecast' not in data or 'forecastday' not in data['forecast']:
            print("Forecast data not available for this city")
            return
            
        print(f"\n 3 Days Forecast for {city.upper()}")
        print("="*40)

        for day in data['forecast']['forecastday']:
            date = day['date']
            max_temp = int(day['day']['maxtemp_c'])
            min_temp = int(day['day']['mintemp_c'])            
            condition = day['day']['condition']['text']
            rain = day['day']['daily_chance_of_rain']

            print(f"{date}: {max_temp}C / {min_temp}C - {condition} ({rain}% rain)")
            print("="*40)
    except Exception as e:
        print(f"\nError getting forecast: {e}")

while True:
    print("\n Options: ")
    print("1. Check weather")
    print("2. view favorites")
    print("3. Add to favorites")
    print("4. Remove From favorites")
    print("5. Recent History")
    print("6. 3 Days forecast")
    print("7. Temperature DashBoard")
    print("8. Exit")

    choice = input("\n Choose Between (1-8) : ")

    if choice == "1":
        city = input("Enter City name : ")
        get_weather(city)
    
    elif choice == "2":
        if favorites and len(favorites) > 0:
            print("\n Your favorites : ")
            print("-"*35)
            for i, city in enumerate(favorites,1):
                print(f" {i} , {city} ")
        else:
            print("\n No favorites yet , Add some cities!")
            print("-"*35)
    elif choice == "3":
        city = input("City to add: ").strip()
        if city:
            if favorites is None:
                favorites =[]
            if city not in favorites:
                print("Verifying city...")
                if get_weather(city):
                    favorites.append(city)
                    if save_favorites(favorites):
                        print(f"{city} added to favorites")
                    else:
                        print("Could not save to file")
                else: 
                    print(f" Can not add {city} - city not found")
            else:
                print(f"{city} is already in favorites")
        else:
            print("please Enter a correct city name")
    elif choice == "4":
        if favorites and len(favorites) > 0 :
            print("\n Your favorites")
            print("-"*45)
            for i, city in enumerate(favorites , 1):
                print(f"{i} , {city}")
            try:
                num = int(input("\n Number to remove: "))
                if 1 <= num <= len(favorites):
                    removed = favorites.pop(num-1)
                    if save_favorites(favorites):
                        print(f"'{removed}' is removed from favorites.")
                    else :
                        print("could not save to file ")
                else :
                        print(f"Please enter a number between 1 and {len(favorites)}")
            except  ValueError :
                print("Please Enter a valid number")
        else:
            print("\n No favorites to remove")
    elif choice == "5":
        history = load_history()
        if history:
            print("\n Recent searches:")
            for i, city in enumerate(reversed(history) , 1 ):
                print(f"{i}. {city}")
        else:
            print("\n No searches yet")
    elif choice == "6":
        city = input("Enter city name for forecast: ")
        show_forecast(city)
    elif choice == "7":
        city = input("\n Enter city for Dashboard: ")
        show_dashboard(city)
    elif choice == "8":
        print("\n Goodbye! have a nice day...")
    else:
        print("Invalid Choice please Choose between (1-5)")