import requests


def get_weather(city):
    """Fetch Weather data with detailed error checking"""

    api_key = "dc03c6d068d4495d8a394636262603"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            city_name = data['location']['name']
            country = data['location']['country']
            temp_c = data['current']['temp_c']
            feels_like = data ['current']['feelslike_c']
            humidity = data['current']['humidity']
            condition = data['current']['condition']['text']
            wind_kph = data['current']['wind_kph']

            print("\n"+"="*45)
            print(f"Weather in {city_name} , {country}")
            print("="*45)
            print(f"Temperature : {temp_c} C")
            print(f"Feels like : {feels_like} C")
            print(f"Humidity : {humidity}")
            print(f"Condition : {condition}")
            print(f"Wind Speed : {wind_kph}")
            print("="*45)

        else:
            print(f"\n {city} Not Found")
            print("Please Check the spelling and try again")

    except requests.exceptions.ConnectionError:
        print("\n No Internet Connection!")
    except requests.exceptions.Timeout:
        print("\nRequest timed out , Try Again")
    except Exception as e :
        print(f"\n Error: {e}")

print("Weather App")
print("-"*35)
print("Get real-time Weather for any city")
print("-"*35)

city = input("\n Enter city : ")
get_weather(city)
    