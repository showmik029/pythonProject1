import requests

def get_weather(api, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api}

    try:
        response = requests.get(base_url, params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}: {data['weather'][0]['description']}")
            print(f"Temperature: {data['main']['temp'] - 273.15:.2f} °C")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"ERROR {e}")


api = '6585a5b86f8872158cf5946c470a6488'
city = input("Enter municipality name: ")

get_weather(api, city)
