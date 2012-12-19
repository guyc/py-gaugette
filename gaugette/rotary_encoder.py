#----------------------------------------------------------------------
# rotary_encoder.py from https://github.com/guyc/py-gaugette
# Guy Carpenter, Clearwater Software
#
# This is a class for reading quadrature rotary encoders
# like the PEC11 Series available from Adafruit:
#   http://www.adafruit.com/products/377
# The datasheet for this encoder is here:
#   http://www.adafruit.com/datasheets/pec11.pdf
#
# This library expects the common pin C to be connected
# to ground.  Pins A and B will have their pull-up resistor
# pulled high.
# 
# Usage:
#
#     import gaugette.rotary_encoder
#     A_PIN = 7  # use wiring pin numbers here
#     B_PIN = 9
#     encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
#     while 1:
#       delta = encoder.delta() # returns 0,1,or -1
#       if delta!=0:
#         print delta

import wiringpi
import math
import threading
import time

class RotaryEncoder:

    # Turning the encoder clockwise generates these
    # r_state values (binary):  00 01 11 10 
    # STATE_TABLE maps these values back to sequence values [0,1,2,3]
    # Coincidentally the transformation table contains exactly the
    # r_state values, but it is just a coincidence that the transform
    # is symmatrical - ie 
    #    sequence = STATE_TABLE[r_state]
    # and
    #    r_state = STATE_TABLE[sequence].
    # lookup table below, where sequence = STATE_TABLE[r_state]
    STATE_TABLE = [ 0, 1, 3, 2 ]

    #----------------------------------------------------------------------
    # Pass the wiring pin numbers here.  See:
    #  https://projects.drogon.net/raspberry-pi/wiringpi/pins/
    #----------------------------------------------------------------------
    def __init__(self, a_pin, b_pin):
        self.a_pin = a_pin
        self.b_pin = b_pin

        self.gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

        self.gpio.pinMode(self.a_pin, self.gpio.INPUT)
        self.gpio.pullUpDnControl(self.a_pin, self.gpio.PUD_UP)

        self.gpio.pinMode(self.b_pin, self.gpio.INPUT)
        self.gpio.pullUpDnControl(self.b_pin, self.gpio.PUD_UP)

        self.last_delta = 0
        self.r_state = self.rotation_state()

    # Gets the 2-bit rotation state of the current position
    def rotation_state(self):
        a_state = self.gpio.digitalRead(self.a_pin)
        b_state = self.gpio.digitalRead(self.b_pin)
        r_state = a_state | b_state << 1
        return r_state

    # Returns offset values of -2,-1,0,1,2
    def get_delta(self):
        delta = 0
        r_state = self.rotation_state()
        if r_state != self.r_state:
            delta = (self.STATE_TABLE[r_state] - self.STATE_TABLE[self.r_state] + 4) % 4
            if delta==3:
                delta = -1
            elif delta==2:
                delta = int(math.copysign(delta, self.last_delta))  # same direction as previous, 2 steps
                
            self.last_delta = delta
            self.r_state = r_state

        return delta

    class Worker(threading.Thread):
        def __init__(self, a_pin, b_pin):
            threading.Thread.__init__(self)
            self.lock = threading.Lock()
            self.encoder = RotaryEncoder(a_pin, b_pin)
            self.daemon = True
            self.delta = 0

        def run(self):
            while True:
                delta = self.encoder.get_delta()
                with self.lock:
                    self.delta += delta
                time.sleep(0.001)

        def get_delta(self):
            # revisit - should use locking
            with self.lock:
                delta = self.delta
                self.delta = 0
            return delta
