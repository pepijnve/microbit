import random

from microbit import *

curr_x = 2
curr_y = 0
score = 0

drop_every = 10

new_line = True

display.clear()
display.show(["3", "2", "1"], delay=1000, wait=True, clear=True)
display.set_pixel(curr_x, curr_y, 9)

game_over = False
counter = 0
score = 0
hole_x = 2

while True:
    if new_line:
        while True:
            next_hole_x = random.randint(0, 4)
            if next_hole_x != hole_x:
                hole_x = next_hole_x
                break

        display.set_pixel(0, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(4, 4, 9)
        display.set_pixel(hole_x, 4, 0)
        new_line = False

    sleep(100)

    left = button_a.get_presses()
    right = button_b.get_presses()
    delta = right - left

    x = curr_x + delta
    if x < 0:
        x = 0
    elif x > 4:
        x = 4

    counter += 1
    if counter == drop_every:
        counter = 0
        y = curr_y + 1
        if y == 5:
            new_line = True
            y = 0
            score += 1
            if score % 3 == 0 and drop_every > 0:
                drop_every -= 1
        elif y == 4:
            if display.get_pixel(x, y) != 0:
                game_over = True
                break
    else:
        y = curr_y

    if display.get_pixel(x, y) == 0:
        display.set_pixel(curr_x, curr_y, 0)
        display.set_pixel(x, y, 9)
        curr_x = x
        curr_y = y

display.clear()
display.show(Image.SAD)
sleep(1000)
display.scroll(str(score), wait=True, loop=True)