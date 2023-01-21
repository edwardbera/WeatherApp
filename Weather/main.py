import requests
import json
import tkinter
from tkinter import *


def getWeather(location):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=372484f8d3eea195fa4ac935dc8dbda6"
    results = requests.get(url)

    if results.status_code == 200:
        data = results.json()
        f = open('weather.json', 'w')
        json.dump(data, f, indent=2)
        f.close()


def readJson():
    j = open('weather.json', "r")
    jdata = json.loads(j.read())
    j.close()

    w = jdata['weather']
    m =jdata['main']
    c = jdata['name']
    wind = jdata['wind']
    sky = w[0]['description']
    humidity = m['humidity']
    max_temp = m['temp_max']
    min_temp = m['temp_min']
    wind = wind['speed']
    city = c

    weather = []
    weather.append(sky)
    weather.append(humidity)
    weather.append(max_temp)
    weather.append(min_temp)
    weather.append(city)
    weather.append(wind)
    return weather


def update(cl, hm, mx, mn, location, wind):
    wlabel1.config(text = location)
    wlabel5.config(text = cl)
    wlabel2.config(text = hm)
    wlabel3.config(text = mx)
    wlabel4.config(text = mn)
    wlabel6.config(text = wind)
   
    
def getInput():
    inp = input.get(1.0, END)
    inp = inp.strip()
    getWeather(inp)
    wData = readJson()
    clouds = wData[0]
    humidity = wData[1]
    max = wData[2]
    min = wData[3]
    location = wData[4]
    wind = wData[5]
    update(clouds, humidity, max, min, location, wind)    
    msg =   "Location : " + location + "\n\n Clouds : " + clouds + "\n Humidity : " + str(humidity) + "\n Maximum Temperature : " + str(max) + "\n Minimum Temperature : " + str(min) + "\n Wind Speed   : " + str(wind)
    #msg = "Clouds : "+ clouds +" \n Humidity : " + shum


top = tkinter.Tk()
top.title("Insta Weather")
top.configure(bg = '#343d46')

input = tkinter.Text(top, show=None, height=1, width= 25, font =('michroma', 12) )
input.grid(row=2, column=2, padx = 15,
pady=15)
btn = tkinter.Button(top, text = "GO", width=10,command=getInput)
label = tkinter.Label(top, text= "Insta Weather" , font='michroma 25 bold italic', bg = "#343d46", fg="#eeeeee", relief=tkinter.FLAT).grid(row=0, column=2, padx=20)
label1 = tkinter.Label(top, text= "City", font='michroma 15 bold',bg = "#343d46", fg="#eeeeee", relief=tkinter.FLAT).grid(row=2, column=1)  
label1 = tkinter.Label(top, text= "Location", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=5, column=1)
label1 = tkinter.Label(top, text= "Clouds ", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=6, column=1)
label2 = tkinter.Label(top, text= "Humidity", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=7, column=1)
label3 = tkinter.Label(top, text= "Max Temperature", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=8, column=1) 
label4 = tkinter.Label(top, text= "Min Temperature", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=9, column=1)
label5 = tkinter.Label(top, text= "Wind", font='michroma 12',bg = "#343d46", fg="#c0c5ce", relief=tkinter.FLAT).grid(row=10, column=1)

wlabel1 =  tkinter.Label(top, show= None, font='michroma 10 bold' ,bg = '#343d46', fg = "red",relief=tkinter.FLAT)
wlabel1.grid(row=5, column=2)
wlabel5 =  tkinter.Label(top, show= None, font='michroma 10 bold' , bg = '#343d46',fg = "red",relief=tkinter.FLAT)
wlabel5.grid(row=6, column=2)
wlabel2 =  tkinter.Label(top, show= None,  font='michroma 10 bold' , bg = '#343d46',fg = "red",relief=tkinter.FLAT)
wlabel2.grid(row=7, column=2)
wlabel3 =  tkinter.Label(top, show= None ,font='michroma 10 bold' ,bg = '#343d46', fg = "red",relief=tkinter.FLAT)
wlabel3.grid(row=8, column=2)
wlabel4 =  tkinter.Label(top, show= None ,font='michroma 10 bold' ,bg = '#343d46', fg = "red",relief=tkinter.FLAT)
wlabel4.grid(row=9, column=2)
wlabel6 =  tkinter.Label(top, show= None ,font='michroma 10 bold' ,bg = '#343d46', fg = "red",relief=tkinter.FLAT)
wlabel6.grid(row=10, column=2)
btn.grid(row=11, column=2, pady = 15)
top.mainloop()
