import wiringpi

class Switch:

    def __init__(self, pin):
        self.pin = pin

        self.gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.gpio.pinMode(self.pin, self.gpio.INPUT)
        self.gpio.pullUpDnControl(self.pin, self.gpio.PUD_UP)

    def get_state(self):
        state = self.gpio.digitalRead(self.pin)
        # We are pulling-high and switching
        # to ground, so state will be 1 when the switch is open, and 0
        # when it is closed.  We invert the value here to a more
        # conventional representation of 0:open, 1:closed.
        return 1-state;
