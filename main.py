#!/usr/bin/python3

import random
import time
from machine import Pin

statusled = Pin("LED", Pin.OUT)

led0 = Pin(0,Pin.OUT)
led1 = Pin(1,Pin.OUT)
led2 = Pin(2,Pin.OUT)
led3 = Pin(3,Pin.OUT)

statusled.value(0)
led0.value(0)
led1.value(0)
led2.value(0)
led3.value(0)

def main():

    while True:
        statusled.value(1)
        random_eye = random.randint(0, 3)  # Number of eyes
        blink(random_eye)
        time.sleep(random.uniform(0.0, 3.0))  # Min and max possible time between blinks


def blink(id):
    print(f"id: {id}  blink")
    light_off(id)
    time.sleep(0.2)  # Duration of blink
    light_on(id)


def light_on(id):
    # Use GPIO to turn light on
    if (id == 0):
        led0.value(1)
    elif (id == 1):
        led1.value(1)
    elif (id == 2):
        led2.value(1)
    elif (id == 3):
        led3.value(1)
    pass


def light_off(id):
    # Use GPIO to turn light off
    if (id == 0):
        led0.value(0)
    elif (id == 1):
        led1.value(0)
    elif (id == 2):
        led2.value(0)
    elif (id == 3):
        led3.value(0)
    pass


main()