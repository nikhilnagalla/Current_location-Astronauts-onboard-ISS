

# json convert the python dictionary
# above into a json
import json 
import turtle
#import requests
# urllib.request fetch URLs using
# a variety of different protocols
import urllib.request
import time
 
# webbrowser provides a high-level interface
# to allow displaying Web-based documents
# to users
import webbrowser
 
# geocoder takes the data and locate these
# locations in the map
import geocoder
 
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " +
            # prints number of astronauts
           str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
 
# prints names of crew
for p in people:
    file.write(p['name'] + " - on board" + "\n")
# print long and lat
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")
