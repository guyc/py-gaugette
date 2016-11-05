import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time

ROWS = 32

if gaugette.platform.isRaspberryPi:
    RESET_PIN = 15
    DC_PIN    = 16
else:  # beagebone
    RESET_PIN = "P9_15"
    DC_PIN    = "P9_13"


spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)
print("init")
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=ROWS, cols=128)
print("begin")
led.begin()
print("clear")
led.clear_display()
led.display()

led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)

offset = 0 # flips between 0 and 32 for double buffering

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
        text = time.strftime("%A")
        print("draw")
        led.draw_text2(0,0,text,2)
        text = time.strftime("%e %b %Y")
        print("draw")
        led.draw_text2(0,16,text,2)
        text = time.strftime("%X")
        print("draw")
        led.draw_text2(0,32+4,text,3)
        print("display")
        led.display()
        time.sleep(0.2)
    else:
        time.sleep(0.5)

    # vertically scroll to switch between buffers
    print("scroll")
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)
