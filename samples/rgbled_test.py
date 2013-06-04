import gaugette.rgbled
import time
import wiringpi2

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

led = gaugette.rgbled.RgbLed(4,6,5)
led.fade(100,0,0,500)
time.sleep(1)
led.fade(100,0,100,500)
time.sleep(1)
led.fade(0,0,100,500)
time.sleep(1)
led.fade(0,0,0,500)

