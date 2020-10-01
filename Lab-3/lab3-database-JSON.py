#!/usr/bin/env python3
import sqlite3
from urllib.request import * 
from urllib.parse import * 
import json

#Function to send ThingSpeak channel data
def writeToThingSpeak(field1):
    URL = 'https://api.thingspeak.com/update?api_key='
    KEY = 'JXSUGRG1EZF1TVSC'  # Write API Key
    HEADER = ('&field1=%d' % (field1))
    FULL_URL = URL + KEY + HEADER   #URL for the get request

    return urlopen(FULL_URL).read()

#Function to get ThingSpeak channel data in JSON format
def readThingspeakData():
    URL = 'https://api.thingspeak.com/channels/1168053/feeds.json?api_key='
    KEY = 'AQFAMUVM32U2I9YZ'
    HEADER = '&results=1'
    FULL_URL = URL + KEY + HEADER   #URL for the get request

    return urlopen(FULL_URL).read()

def getCityWeatherInfo(city):
    # The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa

    # As of October 2015, you need an API key.
    # I have registered under my Carleton email.
    apiKey = "a808bbf30202728efca23e099a4eecc7"

    # Build the URL parameters
    params = {"q":city, "units":"metric", "APPID":apiKey }
    arguments = urlencode(params)
    # Get the weather information
    address = "http://api.openweathermap.org/data/2.5/weather"
    url = address + "?" + arguments
    
    #print (url)
    webData = urlopen(url)
    results = webData.read().decode('utf-8')
    # results is a JSON string
    webData.close()
    
    return results


#-----------------------Connecting to database-------------------------
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();


#-----------------------Querying and obtain weather data-------------------------
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")
results = getCityWeatherInfo(city)

#print (results)
#save JSON in a file
f = open("dump.json", "a")
f.write(results)
f.close()
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API
rawWeatherData = json.loads(results)


#-----------------------Writing and reading the wind data to and from ThingSpeak-------------------------
#Write the wind speed to ThingSpeak
writeToThingSpeak(rawWeatherData["wind"]["speed"])
print("\nSuccessfully wrote wind data to ThingSpeak...")

#Reading data from ThingSpeak
data = json.loads(readThingspeakData())
print("Successfully read data from ThingSpeaK...\n")


#-----------------------Writing the data from ThingSpeak to data base-------------------------
#Create new 'sensor' table if not existing
cursor.execute('''CREATE TABLE IF NOT EXISTS cityWind (city TEXT, wind NUMERIC);''')
dbconnect.commit();

feeds = data['feeds']    #extract from the pairs of feeds (only 1 in this case)
#Extract data from each feed
wind = feeds[0]['field1']
#execute insert statement
cursor.execute('''insert into cityWind values (?, ?)''', (city, wind));
dbconnect.commit();


#-----------------------Printing the data base 'cityWind' table-------------------------
cursor.execute('SELECT * FROM cityWind');
print("----------PRINTING ALL DATA FROM 'cityWind' TABLE----------")
for row in cursor:
    print(row['city'],row['wind']);

#close the connection
dbconnect.close();


#-----------------------Printing all of the city weather data to console-------------------------
current = rawWeatherData["main"]
degreeSym = chr(176)
print("\n----------PRINTING %s WEATHER INFORMATION----------" % city)
print ("Temperature: %d%sC" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )
print ("Wind : %s" % wind)
