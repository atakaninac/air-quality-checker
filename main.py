import tkinter as tk
import requests

#Function for Taking the Average of Lists
def average(list):
    return sum(list)/len(list)


#Take User Input as Latitude and Longitude and Put It in API
def take_input():
    latitude = entry_lat.get()
    longitude = entry_long.get()

    data = requests.get(url=f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&hourly=pm10,pm2_5&forecast_days=1").json()

    pm10 = data["hourly"]["pm10"]
    pm2_5 = data["hourly"]["pm2_5"]

    average_pm10 = average(pm10)
    average_pm25 = average(pm2_5)

    label_pm10.config(text=f"Average PM10 is {average_pm10} μg/m³")
    label_pm25.config(text=f"Average PM2.5 is {average_pm25} μg/m³")

    location_data = data = requests.get(url=f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={latitude}&longitude={longitude}&localityLanguage=en").json()

    city = location_data["city"]
    locality = location_data["locality"]

    label_city.config(text=f"{city}")
    label_locality.config(text=f"{locality}")

#Window
window = tk.Tk()
window.title("Air Quailty")
window.config(padx=80, pady=80)
window.resizable(False, False)

#Entries
entry_long = tk.Entry(width=10, font=("Arial", 16))
entry_long.insert(tk.END, string=("Longitude."))

entry_lat = tk.Entry(width=10, font=("Arial", 16))
entry_lat.insert(tk.END, string=("Latitude."))
entry_lat.focus()

entry_long.grid(row=3, column=0)
entry_lat.grid(row=2, column=0)

#Button
button = tk.Button(text="Insert", font=("Arial", 16), command=take_input)

button.grid(row=2, column=3)

#Label
label = tk.Label(text="Input the longitude and latitude of your location and press Insert to see average air quality.", font=("Arial", 16))
label2 = tk.Label(text="Please use '. (decimal point)' for decimal fractions.", font=("Arial", 16))
label_pm10 = tk.Label(text="Average PM10 is ... μg/m³", font=("Arial", 16))
label_pm25 = tk.Label(text="Average PM2.5 is ... μg/m³", font=("Arial", 16))
label_city = tk.Label(text="", font=("Arial", 16))
label_locality = tk.Label(text="", font=("Arial", 16))

label.grid(row=0, column=0)
label2.grid(row=1, column=0)
label_pm10.grid(row=4, column=0)
label_pm25.grid(row=5, column=0)
label_city.grid(row=6, column=0)
label_locality.grid(row=7, column=0)






window.mainloop()
