from microbit import *
import music
import radio

radio.reset()
radio.config(group=1)
radio.on()

while True:
    sleep(50)
    msg = radio.receive()
    if msg is not None:
        if msg == "short":
            music.play("c4:1", wait=False)
        elif msg == "long":
            music.play("c4:3", wait=False)

    a_pressed = button_a.was_pressed()
    b_pressed = button_b.was_pressed()
    if a_pressed and b_pressed:
        radio.send("end")
    elif a_pressed:
        display.show(Image.ARROW_W)
        radio.send("short")
    elif b_pressed:
        display.show(Image.ARROW_E)
        radio.send("long")
