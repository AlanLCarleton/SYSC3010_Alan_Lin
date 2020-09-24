import requests
import time
from sense_hat import SenseHat

#Function to get ThingSpeak channel data in JSON format
def writeToThingSpeak(field1, field2, field3):
    URL = 'https://api.thingspeak.com/update?api_key='
    KEY = 'UIQP5K8SUOKUMPLM'  # Write API Key
    HEADER = ('&field1=%d&field2=%d&field3=%d' % (field1, field2, field3))
    FULL_URL = URL + KEY + HEADER	#URL for the get request
    #print(FULL_URL + '\n')

    return requests.get(FULL_URL)

        
sense = SenseHat()
if __name__ == "__main__":
    for i in range(0, 5):
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temperature = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        humidity = round(sense.get_humidity())
        pressure = round(sense.get_pressure())
        print('CPU Temperature=%dC\nRoom Humidity=%d\nRoom Pressure=%d\n' %(temperature, humidity, pressure))
        #Write the data to Thingspeak
        writeToThingSpeak(temperature, humidity, pressure)
        time.sleep(3)   #pause for 3 seconds before grabbing more data
