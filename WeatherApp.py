from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Weather App")
root.iconbitmap('C:/Users/user/PycharmProjects/Tkinter/images/i2.ico')
root.geometry("600x100")

# create city name function

def CityName():
    # city_name.get()
    # city_nameLabel = Label(root, text=city_name.get())
    # city_nameLabel.grid(row = 1, column=0, columnspan =2)

    try:
        api_request = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=1b3dd1ea7df64828bb5132617200712&q=" + city_name.get() + "&days=1")
        api = json.loads(api_request.content)
        city = api["location"]["name"]
        temp = api["current"]["temp_c"]
        humidity = api["current"]["humidity"]

        if temp > 0 and temp < 19:
            weather_color = "#6342f5"
        elif temp > 20 and temp < 30:
            weather_color = "#42d4f5"
        elif temp > 31 and temp < 40:
            weather_color = "#f5b342"
        elif temp > 41 and temp < 50:
            weather_color = "#f55d42"
        elif temp > 51 and temp < 100:
            weather_color = "#f55d42"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + " Temperature " + str(temp) + " Humidity " + str(humidity),
                        font=("Helvectica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key})

try:
    api_request = requests.get("https://api.weatherapi.com/v1/forecast.json?key=1b3dd1ea7df64828bb5132617200712&q=pune&days=1")
    api = json.loads(api_request.content)
    city = api["location"]["name"]
    temp = api["current"]["temp_c"]
    humidity = api["current"]["humidity"]

    if temp > 0 and temp < 19:
        weather_color = "#6342f5"
    elif temp > 20 and temp < 30:
        weather_color = "#42d4f5"
    elif temp > 31 and temp < 40:
        weather_color = "#f5b342"
    elif temp > 41 and temp < 50:
        weather_color = "#f55d42"
    elif temp > 51 and temp < 100:
        weather_color = "#f55d42"

    root.configure(background=weather_color)

    myLabel = Label(root, text=city + " Temperature " + str(temp) + " Humidity " + str(humidity),font=("Helvectica", 20), background=weather_color)
    myLabel.grid(row=1, column=0, columnspan=2)
except Exception as e:
    api = "Error..."

city_name = Entry(root)
city_name.grid(row=0, column=0,stick= W+E+N+S)

city_nameButton = Button(root, text="City Name", command = CityName)
city_nameButton.grid(row=0, column=1,stick= W+E+N+S)

root.mainloop()