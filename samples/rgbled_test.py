import gaugette.rgbled
import time
import wiringpi

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

led = gaugette.rgbled.RgbLed(4,6,5)
led.fade(100,0,0,500)
time.sleep(1)
led.fade(100,0,100,500)
time.sleep(1)
led.fade(0,0,100,500)
time.sleep(1)
led.fade(0,0,0,500)

