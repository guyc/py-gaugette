
class CapSwitchwhich:
    def __init__(self, gpio, pin):
        self.gpio = gpio
        self.pin = pin
        self.gpio.setup(self.pin, self.gpio.OUT)
        self.max_cycles = 100
        self.repeats = 2
        self.threshold = 40

    def sense(self):
        for _ in range(0, self.repeats):

            # 1) set pin low and to output to discharge
            self.gpio.setup(self.pin, self.gpio.OUT)
            self.gpio.output(self.pin, self.gpio.LOW)

            # 2) make the pin an input without the internal pull-up on
            self.gpio.setup(self.pin, self.gpio.IN, pull_up_down=self.gpio.PUD_OFF)

            # 3) read input and see how long it takes to go high
            cycles = 0
            total = 0.0
            while cycles < self.max_cycles and self.gpio.input(self.pin) == 0:
                cycles += 1

            total += cycles
        mean = total / self.repeats

        return mean > self.threshold
