# Sample code for both the RotaryEncoder class and the Switch class.
# The common pin for the encoder should be wired to ground.
# The sw_pin should be shorted to ground by the switch.

import time
import gaugette.gpio
import gaugette.rotary_encoder

# Rotary encoder pins
A_PIN = 23
B_PIN = 22

def rotated(direction):
    print("Rotated ", direction)

gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN, rotated)
encoder.start()

while True:
    time.sleep(100)
