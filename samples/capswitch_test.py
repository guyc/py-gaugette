import gaugette.capswitch
import gaugette.rgbled
import time

if gaugette.platform == 'raspberrypi':
  SWITCH_PIN = 9
  RGB_RED    = 6
  RGB_GREEN  = 5
  RGB_BLUE   = 4
else:  # beaglebone
  SWITCH_PIN = 'P9_X'
  RGB_RED    = 'P9_X'
  RGB_GREEN  = 'P9_X'
  RGB_BLUE   = 'P9_X'
  raise NotImplementedError('capswitch is not yet supported on the beaglebone')
 
switch = gaugette.capswitch.CapSwitch(SWITCH_PIN)
led = gaugette.rgbled.RgbLed(RGB_RED, RGB_GREEN, RGB_BLUE)

led.set(0,0,100)
led_on = True

while 1:
    if switch.sense():
        print('sense')

        if led_on:
            led.fade(100,0,0)
            led_on = False
        else:
            led.fade(0,0,100)
            led_on = True

