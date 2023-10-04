def main():

    eyes_quantity = 3
    eyes = []

    for i in range(eyes_quantity):
        eyes.append(Eye(i, True))

    for i in eyes:
        print(f"ID: {i.number}  On: {i.on}")

def light_on():
    # Use GPIO to turn light on
    pass

def light_off():
    # Use GPIO to turn light off
    pass

class Eye:

    def __init__(self, eye_number, light_on):
        self.number = eye_number
        self.on = light_on

    # Turn off for fraction of a second
    def blink(self):
        light_off()
        self.on = False
        # sleep for some amount of time
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