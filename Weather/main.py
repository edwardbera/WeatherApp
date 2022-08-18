from textwrap import indent
from xml.dom.minidom import Element
import requests
from bs4 import BeautifulSoup
import json
import tkinter
from whatsapp import *

city = "Bulawayo"


def getWeather(location):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=372484f8d3eea195fa4ac935dc8dbda6"
    results = requests.get(url)

    if results.status_code == 200:
        data = results.json()
        f = open('weather.json', 'w')
        json.dump(data, f, indent=2)
        f.close()

        #print(results.json())

def readJson():
    j = open('weather.json', "r")
    jdata = json.loads(j.read())
    j.close()

    w = jdata['weather']
    m =jdata['main']
    c = jdata['name']
    sky = w[0]['description']
    humidity = m['humidity']
    max_temp = m['temp_max']
    min_temp = m['temp_min']
    city = c

    weather = []

    weather.append(sky)
    weather.append(humidity)
    weather.append(max_temp)
    weather.append(min_temp)
    weather.append(city)

    #print( )
    return weather







def gui(sky, humidity, max, min, ct):

    top = tkinter.Tk()
   # top.geometry("500x200")
    str = "Insta Weather"
    input = tkinter.Entry(top, show=None, font =('michroma', 10) ).grid(row=2, column=2)
    btn = tkinter.Button(top, text = "GO").grid(row=2, column=3)
    label = tkinter.Label(top, text= "Insta Weather" , font='michroma 14 bold', relief=tkinter.FLAT).grid(row=0, column=2)
    label1 = tkinter.Label(top, text= "City", font='michroma 10', relief=tkinter.FLAT).grid(row=2, column=0)
    
    label1 = tkinter.Label(top, text= "Location", font='michroma 10', relief=tkinter.FLAT).grid(row=5, column=0)
    
    label1 = tkinter.Label(top, text= "Sky ", font='michroma 10', relief=tkinter.FLAT).grid(row=6, column=0)
    label2 = tkinter.Label(top, text= "Humidity", font='michroma 10', relief=tkinter.FLAT).grid(row=7, column=0)
    label3 = tkinter.Label(top, text= "Max Temperature", font='michroma 10', relief=tkinter.FLAT).grid(row=8, column=0)
    label4 = tkinter.Label(top, text= "Min Temperature", font='michroma 10', relief=tkinter.FLAT).grid(row=9, column=0)

    wlabel1 =  tkinter.Label(top, text= ct , font='michroma 10' , fg = "red",relief=tkinter.FLAT).grid(row=5, column=3) 
    wlabel1 =  tkinter.Label(top, text= sky , font='michroma 10' , fg = "red",relief=tkinter.FLAT).grid(row=6, column=3)
    wlabel2 =  tkinter.Label(top, text= humidity ,  font='michroma 10' , fg = "red",relief=tkinter.FLAT).grid(row=7, column=3)
    wlabel3 =  tkinter.Label(top, text= max  ,font='michroma 10' , fg = "red",relief=tkinter.FLAT).grid(row=8, column=3)
    wlabel4 =  tkinter.Label(top, text= min  ,font='michroma 10' , fg = "red",relief=tkinter.FLAT).grid(row=9, column=3)

    



    
    top.mainloop()


getWeather(city)
wData = readJson()
msg = "The sky has " + wData[0] + ", Humidity is" + str(wData[1]) + ", Maximum Temperature is " + str(wData[2])
sendmsg(msg)
gui(wData[0], wData[1], wData[2], wData[3], wData[4])