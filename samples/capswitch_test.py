import gaugette.capswitch
import gaugette.rgbled
import time
import wiringpi2

# io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

switch = gaugette.capswitch.CapSwitch(3)
led = gaugette.rgbled.RgbLed(4,6,5)

led.set(0,0,100)
led_on = True

while 1:
    if switch.sense():
        print 'sense'

        if led_on:
            led.fade(100,0,0)
            led_on = False
        else:
            led.fade(0,0,100)
            led_on = True


