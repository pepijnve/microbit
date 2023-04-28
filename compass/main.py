from microbit import *

def set(x, y):
    global prev_x
    global prev_y
    if x != prev_x or y != prev_y:
        display.set_pixel(x, y, 9)
        display.set_pixel(prev_x, prev_y, 0)
        prev_x = x
        prev_y = y


prev_x = 0
prev_y = 0

compass.calibrate()
display.clear()

while True:
    heading = 360 - compass.heading()

    if (heading > 348):
        x = 2
        y = 0
    elif (heading > 326):
        x = 1
        y = 0
    elif (heading > 303):
        x = 0
        y = 0
    elif (heading > 281):
        x = 0
        y = 1
    elif (heading > 258):
        x = 0
        y = 2
    elif (heading > 236):
        x = 0
        y = 3
    elif (heading > 213):
        x = 0
        y = 4
    elif (heading > 191):
        x = 1
        y = 4
    elif (heading > 168):
        x = 2
        y = 4
    elif (heading > 146):
        x = 3
        y = 4
    elif (heading > 123):
        x = 4
        y = 4
    elif (heading > 101):
        x = 4
        y = 3
    elif (heading > 78):
        x = 4
        y = 2
    elif (heading > 56):
        x = 4
        y = 1
    elif (heading > 33):
        x = 4
        y = 0
    elif (heading > 11):
        x = 3
        y = 0
    else:
        x = 2
        y = 0

    set(x, y)