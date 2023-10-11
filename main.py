#!/usr/bin/python3

import random
import threading
import time

def main():

    eyes_quantity = 20
    eyes = []

    for i in range(eyes_quantity):
        eyes.append(Eye(i, True))

    # for i in eyes:
    #     print(f"id: {i.id}  on: {i.on}")
    # print()

    while True:
        random_eye = random.choice(eyes)
        if random_eye.on == True:
            if random.random() > 0.1:  # Chance of hiding
                random_eye.blink()
            else:
                hide_eye = threading.Thread(target=random_eye.hide)
                hide_eye.start()
        time.sleep(random.uniform(0.0, 3.0))  # Min and max possible time between blinks


def light_on():
    # Use GPIO to turn light on
    pass


def light_off():
    # Use GPIO to turn light off
    pass


class Eye:

    def __init__(self, eye_id, light_on):
        self.id = eye_id
        self.on = light_on

    # Turn off for fraction of a second
    def blink(self):
        print(f"id {self.id}  blink")
        self.on = False
        light_off()
        time.sleep(0.2)  # Duration of blink
        self.on = True
        light_on()
        

    # Turn off for several seconds
    def hide(self):
        print(f"id: {self.id}  hide start")
        self.on = False
        light_off()
        time.sleep(random.uniform(10.0, 30.0))  # Min and max possible duration of hide
        print(f"id: {self.id}  hide end")
        self.on = True
        light_on()


main()