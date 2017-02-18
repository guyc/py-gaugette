# Sample code for both the RotaryEncoder class and the Switch class.
# The common pin for the encoder should be wired to ground.
# The sw_pin should be shorted to ground by the switch.

import gaugette.rotary_encoder
import gaugette.switch
import gaugette.gpio
import time

A_PIN  = 7
B_PIN  = 8
SW_PIN = 9

gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(gpio, SW_PIN)
last_state = None

while True:
    delta = encoder.get_steps()
    if delta!=0:
        print ("rotate %d" % delta)
    else:
        time.sleep(0.05)

    sw_state = switch.get_state()
    if sw_state != last_state:
        print ("switch %d" % sw_state)
        last_state = sw_state
