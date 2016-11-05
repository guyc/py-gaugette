import wiringpi

class Switch:

    def __init__(self, gpio, pin, pullUp=True):
        self.gpio = gpio
        self.pin = pin
        self.pullUp = pullUp
        pullUpMode = gpio.PUD_UP if pullUp else gpio.PUD_DOWN
        self.gpio.setup(self.pin, self.gpio.IN, pullUpMode)

    def get_state(self):
        state = self.gpio.input(self.pin)
        if self.pullUp:
            # If we are pulling up and switching
            # to ground, state will be 1 when the switch is open, and 0
            # when it is closed.  We invert the value here to a more
            # conventional representation of 0:open, 1:closed.
            return 1-state
        else:
            return state
