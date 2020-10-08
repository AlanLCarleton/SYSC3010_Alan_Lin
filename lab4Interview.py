from sense_hat import SenseHat
#from sense_emu import SenseHat

sense = SenseHat()

#function to set orientation of SenseHAT LED matrix
# NOTE: THIS AUTO ORIENTATION FUNCTION IS BUGGY WHEN RAN ON EMULATOR
def setOrientation(x, y):
    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)


# My intials are "AL"
intials = ['T', 'A']
counter = 0
sense.show_letter(intials[0])
while True:
    #grab accelerometer data to set up display orientation
    x, y, z = sense.get_accelerometer_raw().values()
    x = round(x, 0)
    y = round(y, 0) 
    #setOrientation of letter
    setOrientation(x, y)

    for event in sense.stick.get_events():
        #when joystick is pressed
        if event.action == "pressed":
                if (event.direction == "up" or
                event.direction == "down" or
                event.direction == "left" or
                event.direction == "right" or
                event.direction == "middle"):
                    #change the displaying letter
                    if (counter == 2):
                        sense.show_letter(intials[0])
                    elif (counter == 4):
                         sense.show_letter(intials[1])
                         counter =0

                    counter+=1
                    
                    
