import requests

#Function to get ThingSpeak channel data in JSON format
def readThingspeakData():
	URL = 'https://api.thingspeak.com/channels/1156645/feeds.json?api_key='
	KEY = '5IQYTQFYRHBJWQM8'
	HEADER = '&results=3'
	FULL_URL = URL + KEY + HEADER	#URL for the get request
	#print(FULL_URL + '\n')

	return requests.get(FULL_URL).json()
	
if __name__ == "__main__":
	getData = readThingspeakData()
	
	channelId = getData['channel']['id']	#extract the channel ID
	print('Channel ID: ', channelId, '\n')
	
	feeds = getData['feeds']	#extract the pairs of feeds
	i = 1
	#Extract data from each feed
	for feed in feeds:
		print('Feed ' , i)
		print('\tCPU Temperature: %sC\n\tRoom Humidity: %s%s\n\tRoom Pressure: %smbar'
				% (feed['field1'], feed['field2'], '%', feed['field3']))
		i += 1
