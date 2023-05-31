import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/tr-TR/weather/today/l/a6ae974ab6d54e31d092094d11d3e04d41a1f81adefe6a49a939c2c1c4bf2696"

window = Tk()
window.title("⛈️Weather App🌦")
window.config(bg="#17274c")

image = Image.open("weather.png")
image = image.resize((200,200))
image = ImageTk.PhotoImage(image)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
    weatherPrediction = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p").text

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)

    temperatureLabel.after(60000,getWeather)
    window.update()

locationLabel = Label(window, font=("Droid Sans Mono bold", 30), fg="#dcff05", bg="#17274c")
locationLabel.grid(row=0, column=0)

temperatureLabel = Label(window, font=("Droid Sans Mono bold",70), fg="#dcff05", bg="#17274c")
temperatureLabel.grid(row=1, column=0,  pady=10)

Label(window, image=image, bg="#17274c").grid(row=1, column=1)

weatherPredictionLabel = Label(window, font=("Droid Sans Mono bold", 25), fg="#dcff05", bg="#17274c")
weatherPredictionLabel.grid(row=2, column=0, pady=10)


getWeather()
window.mainloop()
