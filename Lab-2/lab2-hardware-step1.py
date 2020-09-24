from sense_hat import SenseHat

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
intials = ['A', 'L']
counter = 1
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
                    sense.show_letter(intials[counter%2])
                    counter+=1
