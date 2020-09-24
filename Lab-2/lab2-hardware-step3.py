from sense_hat import SenseHat
#from sense_emu import SenseHat
import time

sense = SenseHat()

number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

clock_image = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

def displayTime():
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min

    # Map digits to the clock_image array
    pixel_offset = 0
    index = 0
    for index_loop in range(0, 4):
        for counter_loop in range(0, 4):
            if (hour >= 10):
                clock_image[index] = number[int(hour/10)*16+pixel_offset]
            clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
            clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
            clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4

    # Color the hours and minutes
    for index in range(0, 64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = [0,0,255] # Blue
            else:
                clock_image[index] = [255,125,0] # Orange
        else:
            clock_image[index] = [0,0,0] # Black
            
    # Display the time
    sense.low_light = True # Optional
    sense.set_pixels(clock_image)
    
    
def displayTemperature():
    temperature = round(sense.get_temperature())
    message = 'T=%dC' %(temperature)
    #scroll display the temperature
    sense.show_message(message, scroll_speed=(0.1), text_colour=[120,255,0], back_colour=[0,0,0])  

def displayHumidity():
    humidity = round(sense.get_humidity())
    message = 'P=%dmPa' %(humidity)
    #scroll display the humidity
    sense.show_message(message, scroll_speed=(0.1), text_colour=[255,255,255], back_colour=[0,0,0])

while True:
    for event in sense.stick.get_events():
        #when joystick is pressed
        if event.action == "pressed":
            #left arrow press toggles a temporary temperature display
            if event.direction == "left":
                displayTemperature()
            #right arrow press toggles a temporary humidity display
            elif event.direction == "right":
                displayHumidity()
    # Time is displayed by default
    displayTime()