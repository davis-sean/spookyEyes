#!/usr/bin/python3
import random
import time
from machine import Pin

def main():

    Pin("LED", Pin.OUT).value(1)

    eye_quantity = 3
    for i in range(eye_quantity):
        Pin(i, Pin.OUT).value(0)

    while True:
        blink(random.randint(0, eye_quantity))
        time.sleep(random.uniform(0.0, 3.0))  # Min and max possible time between blinks


def blink(id):
    print(f"id: {id}  blink")
    light_off(id)
    time.sleep(0.2)  # Duration of blink
    rando = random.randint(0 , 4)
    if (rando <= 1):
      light_off(id)  
    if (rando > 1):
        light_on(id)


def light_on(id):
    # Use GPIO to turn light on
    Pin(id, Pin.OUT).value(1)


def light_off(id):
    # Use GPIO to turn light off
    Pin(id, Pin.OUT).value(0)

main()