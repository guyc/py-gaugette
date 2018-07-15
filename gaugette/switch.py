import wiringpi

class Switch:

    def __init__(self, gpio, pin, pull_up=True):
        self.gpio = gpio
        self.pin = pin
        self.pull_up = pull_up
        pull_up_mode = gpio.PUD_UP if pull_up else gpio.PUD_DOWN
        self.gpio.setup(self.pin, self.gpio.IN, pull_up_mode)

    # edge = gpio.EDGE_FALLING or gpio.EDGE_RISING
    # isr = interrupt service routine
    def enable_isr(self, edge, isr):
        self.gpio.trigger(self.pin, edge, isr)

    def get_state(self):
        state = self.gpio.input(self.pin)
        if self.pull_up:
            # If we are pulling up and switching
            # to ground, state will be 1 when the switch is open, and 0
            # when it is closed.  We invert the value here to a more
            # conventional representation of 0:open, 1:closed.
            return 1-state
        else:
            return state
