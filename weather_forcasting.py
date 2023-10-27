"""
Author: @AhmedNumanPervane
Title: Weather Forcasting Through ThingSpeak

It is a module for the forcasting the temperatur data on 
the real world map. That is not showing the values on the 
map or not to show as data.

Each temperature value is proper for its longitude and 
latitude variable. 

***--------***-----***-----------***-----***--------***

This module is done for the school project. The aim of 
the project is: getting the temperature of the outside
by designing a portable device and sending the temperature
and position data of itself through Wi-Fi module.

School: Izmir Katip Celebi University
Department: Mechatronics Engineering 
Class: Sensor
Main Project Title: Temperature Sensing Mobile Device
"""

import requests as rq
import folium
from folium.plugins import HeatMap


def Status(URL_stat):
    response = rq.get(URL_stat)
    if response.status_code != 200:
        print("Error in the HTTP request")
        quit()
    return response

def Coordinates(URL_coor) -> float: #Coordinates of the locations by their names
    response = Status(URL_coor)
    data_ = response.json()
    Lat, Lon = float(data_["feeds"][1]["field1"]), float(data_["feeds"][1]["field2"])   # Extracting the coordinate variabes (latitude and longitude) from the WEB data base
    coordinates = Lat, Lon
    return coordinates  # returning the coordinate varibles as tuple form of float varibles

def Temperature(URL_temp) -> float:  #Extracting the temperatur data of location
    response = Status(URL_temp)
    data_ = response.json()
    temperature = float(data_["feeds"][0]["field3"])
    return temperature  # returning the temperature variable as float form

def Mapping( URL_map, heatMapping:bool = True, dataFrame:list[list[float]] = [[]], Zoom:int=14, dispName:str= 'Show'):    # Creating the maps by their locations
    C = Coordinates(URL_coor=URL_map)
    m = folium.Map(location = C, zoom_start = Zoom)
    if heatMapping: #Adding the heat values on the map
        HeatMap(data= dataFrame).add_to(m)
    m.save(f"C:/Users/anper/Desktop/Programlama_projeler/{str(dispName)}_map.html")
    

def main(): # The example code for the operations
    BASE_URL = "Thingspeak https address" # That code have designed for only ThingSpeak. It may give error if not using the ThingSpeak. 
    # But, the code maybe redesign for other programs like OpenWeather.
    API_KEY = "Your API Key"
    URL = BASE_URL + "&appid=" + API_KEY

    BASE_DATA_FRAME = []

    while True:
        DATA_FRAME = []

        time_now = time.ctime()
        print(time_now)
        temp = Temperature(URL)
        lat, lon = Coordinates(URL)

        delta = random()
        delta = delta/100   # delta variable just used for the randomization fo varibales to show proper values on the map
        # these delta variable have to deleted after GPS integration done.

        DATA_FRAME.append([lat+(delta*random()*1.6),lon+(delta*random()*1.2),temp+(100*(random()+0.5)*delta-(random()-random())*100 )])
        BASE_DATA_FRAME.append(DATA_FRAME[0])

        Mapping(URL_map=URL, heatMapping = True, dataFrame=BASE_DATA_FRAME, Zoom=16, dispName="Deneme")

if __name__ == "__main__":
    main()
