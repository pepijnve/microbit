import random

from microbit import *

ring0 = 9
ring0_delta = 1
ring1 = 7
ring1_delta = 1
ring2 = 5
ring2_delta = 1

while True:
    display.set_pixel(2, 2, ring0)

    display.set_pixel(1, 1, ring1)
    display.set_pixel(2, 1, ring1)
    display.set_pixel(3, 1, ring1)
    display.set_pixel(1, 2, ring1)
    display.set_pixel(3, 2, ring1)
    display.set_pixel(1, 3, ring1)
    display.set_pixel(2, 3, ring1)
    display.set_pixel(3, 3, ring1)

    display.set_pixel(0, 0, ring2)
    display.set_pixel(1, 0, ring2)
    display.set_pixel(2, 0, ring2)
    display.set_pixel(3, 0, ring2)
    display.set_pixel(4, 0, ring2)
    display.set_pixel(0, 1, ring2)
    display.set_pixel(4, 1, ring2)
    display.set_pixel(0, 2, ring2)
    display.set_pixel(4, 2, ring2)
    display.set_pixel(0, 3, ring2)
    display.set_pixel(4, 3, ring2)
    display.set_pixel(0, 4, ring2)
    display.set_pixel(1, 4, ring2)
    display.set_pixel(2, 4, ring2)
    display.set_pixel(3, 4, ring2)
    display.set_pixel(4, 4, ring2)

    if ring0 == 0 or ring0 == 9:
        ring0_delta = -ring0_delta
    ring0 += ring0_delta
    if ring1 == 0 or ring1 == 9:
        ring1_delta = -ring1_delta
    ring1 += ring1_delta
    if ring2 == 0 or ring2 == 9:
        ring2_delta = -ring2_delta
    ring2 += ring2_delta

    sleep(150)