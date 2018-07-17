# Sample code for both the RotaryEncoder class and the Switch class.
# The common pin for the encoder should be wired to ground.
# The sw_pin should be shorted to ground by the switch.

import time
import gaugette.gpio
import gaugette.switch

SW_PIN = 21

def pushed():
    print("Switch pushed!")

gpio = gaugette.gpio.GPIO()
sw = gaugette.switch.Switch(gpio, SW_PIN)
# Calls pushed() on a falling edge
sw.enable_isr(gpio.EDGE_FALLING, pushed)

while True:
    time.sleep(100)
