import gaugette.rgbled
import gaugette.gpio
import time

gpio = gaugette.gpio.GPIO()
led = gaugette.rgbled.RgbLed(gpio, 6,5,4)
led.fade(100,0,0,500)
time.sleep(1)
led.fade(100,100,0,500)
time.sleep(1)
led.fade(0,100,0,500)
time.sleep(1)
led.fade(0,100,100,500)
time.sleep(1)
led.fade(0,0,100,500)
time.sleep(1)
led.fade(100,0,100,500)
time.sleep(1)
led.fade(100,0,0,500)
time.sleep(1)
led.fade(0,0,0,500)
