from urllib.request import *
from urllib.parse import *


#Function to send ThingSpeak channel data
def writeToThingSpeak(field1, field2, field3):
    URL = 'https://api.thingspeak.com/update?api_key='
    KEY = 'AT68QYQ94MQEWXL3'  # Write API Key
    HEADER = ('&field1=%s&field2=%s&field3=%s' % (field1, field2, field3))
    FULL_URL = URL + KEY + HEADER   #URL for the get request

    return urlopen(FULL_URL).read()


projectGroup = "L3-T-5"
email = "alanlin@cmail.carleton.ca"
identifier = "c"

#Write the data to ThingSpeak
writeToThingSpeak(projectGroup, email, identifier)
print("\nSuccessfully wrote these values  to ThingSpeak:\nField1: %s\nField2: %s\nField3: %s\n" % (projectGroup, email, identifier))