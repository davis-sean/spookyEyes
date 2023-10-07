#!/usr/bin/python3

import random
import time

def main():

    eyes_quantity = 20
    eyes = []

    blink_frequency = 10 / eyes_quantity

    for i in range(eyes_quantity):
        eyes.append(Eye(i, True))

    for i in eyes:
        print(f"id: {i.id}  on: {i.on}")

    while True:
        random_eye = random.choice(eyes)
        if random_eye.on == True:
            random_eye.blink()
            print(f"id: {random_eye.id}  blink")
            time.sleep(random.uniform(0.0, blink_frequency))
        


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
        light_off()
        self.on = False
        time.sleep(0.2)
        light_on()
        self.on = True
        

    # Turn off for several seconds
    def hide(self):
        light_off()
        self.on = False
        # sleep for some amount of time
        light_on()
        self.on = True


main()