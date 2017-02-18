import gaugette.gpio
import gaugette.platform

# -- need to implement PWM on beaglebone to support this class
if not gaugette.platform.isRaspberryPi:
    raise NotImplementedError('rgbled is not supported on this platform')

import wiringpi
import threading

class RgbLed:

    def __init__(self, gpio, r_pin, g_pin, b_pin):
        self.gpio = gpio
        self.r_pin = r_pin
        self.b_pin = b_pin
        self.g_pin = g_pin
        self.r_pwm = wiringpi.softPwmCreate(r_pin, 0, 100)
        self.g_pwm = wiringpi.softPwmCreate(g_pin, 0, 100)
        self.b_pwm = wiringpi.softPwmCreate(b_pin, 0, 100)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.set(0, 0, 0)

    def set(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        wiringpi.softPwmWrite(self.r_pin, red)
        wiringpi.softPwmWrite(self.g_pin, green)
        wiringpi.softPwmWrite(self.b_pin, blue)

    def fade(self, red, green, blue, delay=500, step=5):
        for i in range(0, delay, step):
            f = (0.0+i)/delay
            r = self.red   + (red  -self.red)   * f
            wiringpi.softPwmWrite(self.r_pin, int(r))
            g = self.green + (green-self.green) * f
            wiringpi.softPwmWrite(self.g_pin, int(g))
            b = self.blue  + (blue -self.blue)  * f

            wiringpi.softPwmWrite(self.b_pin, int(b))
            wiringpi.delay(step)
        self.red = red
        self.blue = blue
        self.green = green

    #----------------------------------------------------------------------
    # Optional subclass provides background services for running colour fade sequences
    #----------------------------------------------------------------------

    class Worker(threading.Thread):
        def __init__(self, gpio, r_pin, g_pin, b_pin):
            threading.Thread.__init__(self)
            self.rgbled = RgbLed(gpio, r_pin, g_pin, b_pin)
            self.sequences = [[10, 0, 0, 1000], [0, 0, 10, 1000], [0, 10, 0, 1000]]  # initial pattern
            self.condition = threading.Condition()
            self.daemon = True
            self.changed = False
            self.red = 0
            self.green = 0
            self.blue = 0
            self.sequence = None
            self.set(self.red, self.green, self.blue)

        def set_sequence(self, sequence):
            self.condition.acquire()
            self.sequence = sequence
            self.changed = True
            self.condition.notify()
            self.condition.release()

        def set(self, r, g, b):
            self.red = r
            self.green = g
            self.blue = b
            self.rgbled.set(r, g, b)

        def run(self):
            self.condition.acquire()
            self.changed = True
            while True:
                if self.changed:
                    self.changed = False
                    sequence = self.sequence
                    count = len(sequence)
                    i = 0

                action = sequence[i]
                i = (i + 1) % count
                if hasattr(action, '__iter__'):
                    if len(action) == 3:
                        self.set(action[0], action[1], action[2])
                        self.condition.wait()
                    else:
                        red   = action[0]
                        green = action[1]
                        blue  = action[2]
                        delay = action[3]
                        step = 10
                        for j in range(0, delay, step):
                            f = (j+0.0) / delay
                            r = int(self.red + (red - self.red)   * f)
                            g = int(self.green + (green - self.green) * f)
                            b = int(self.blue + (blue - self.blue)  * f)
                            self.rgbled.set(r, g, b)
                            self.condition.wait(step / 1000.0)
                            if self.changed:
                                break
                        self.set(red, green, blue)
                else:
                    # must be a simple delay
                    self.condition.wait(action / 1000.0)
