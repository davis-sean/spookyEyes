#!/usr/bin/micropython

import random
import time
from machine import Pin

def main():

    Pin("LED", Pin.OUT).value(1)

    eyes_quantity = 8
    eyes = []

    for i in range(eyes_quantity-1):
        eyes.append(Eye(i, True))

    while True:

        random_eye = random.choice(eyes)

        if random_eye.on == True:
            if random.random() < 0.2:  # hide start chance
                random_eye.light_off()
            else:
                random_eye.blink()
        elif random.random() < 0.2:  # hide end chance
            random_eye.light_on()

        time.sleep(random.uniform(0.0, 3.0))  # Min and max possible time between blinks


class Eye:

    def __init__(self, eye_id, light_on):
        self.id = eye_id
        self.on = light_on

    def blink(self):
        print(f"id {self.id}  blink")
        self.light_off()
        time.sleep(0.2)  # Duration of blink
        self.light_on()

    def light_on(self):
        Pin(self.id, Pin.OUT).value(1)
        self.on = True

    def light_off(self):
        Pin(self.id, Pin.OUT).value(0)
        self.on = False


main()