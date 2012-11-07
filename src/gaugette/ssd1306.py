#----------------------------------------------------------------------
# ssd1306.py from https://github.com/guyc/py-gaugette
# ported by Guy Carpenter, Clearwater Software
#
# This library is for the Adafruit 128x32 SPI monochrome OLED 
# based on the SSD1306 driver.
#   http://www.adafruit.com/products/661
#
# This library does not directly support the larger 128x64 module,
# but could with minor changes.
#
# The code is based heavily on Adafruit's Arduino library
#   https://github.com/adafruit/Adafruit_SSD1306
# written by Limor Fried/Ladyada for Adafruit Industries.
#
# The datasheet for the SSD1306 is available
#   http://www.adafruit.com/datasheets/SSD1306.pdf
#
# WiringPi pinout reference
#   https://projects.drogon.net/raspberry-pi/wiringpi/pins/
#
# Some important things to know about this device and SPI:
#
# - The SPI interface has no MISO connection.  It is write-only.
#
# - The spidev xfer and xfer2 calls overwrite the output buffer
#   with the bytes read back in during the SPI transfer.
#   Use writebytes instead of xfer to avoid having your buffer overwritten.
#
# - The D/C (Data/Command) line is used to distinguish data writes
#   and command writes - HIGH for data, LOW for commands.  To be clear,
#   the attribute bytes following a command opcode are NOT considered data,
#   data in this case refers only to the display memory buffer.
#   keep D/C LOW for the command byte including any following argument bytes.
#   Pull D/C HIGH only when writting to the display memory buffer.
#   
# - The pin connections between the Raspberry Pi and OLED module are:
#
#      RPi     SSD1306
#      CE0   -> CS
#      GPIO2 -> RST   (to use a different GPIO set reset_pin to wiringPi pin no)
#      GPIO1 -> D/C   (to use a different GPIO set dc_pin to wiringPi pin no)
#      SCLK  -> CLK
#      MOSI  -> DATA
#      3.3V  -> VIN
#            -> 3.3Vo
#      GND   -> GND
#----------------------------------------------------------------------

import spidev
import wiringpi
import time
import font5x8
import sys

class SSD1306:

    # Class constants are externally accessible as gaugette.ssd1306.SSD1306.CONST
    # or my_instance.CONST

    # TODO - insert underscores to rationalize constant names

    EXTERNALVCC = 0x1
    SWITCHCAPVCC = 0x2
        
    SETCONTRAST = 0x81
    DISPLAYALLON_RESUME = 0xA4
    DISPLAYALLON = 0xA5
    NORMALDISPLAY = 0xA6
    INVERTDISPLAY = 0xA7
    DISPLAYOFF = 0xAE
    DISPLAYON = 0xAF
    SETDISPLAYOFFSET = 0xD3
    SETCOMPINS = 0xDA
    SETVCOMDETECT = 0xDB
    SETDISPLAYCLOCKDIV = 0xD5
    SETPRECHARGE = 0xD9
    SETMULTIPLEX = 0xA8
    SETLOWCOLUMN = 0x00
    SETHIGHCOLUMN = 0x10
    SETSTARTLINE = 0x40
    MEMORYMODE = 0x20
    COMSCANINC = 0xC0
    COMSCANDEC = 0xC8
    SEGREMAP = 0xA0
    CHARGEPUMP = 0x8D
    
    ACTIVATE_SCROLL = 0x2F
    DEACTIVATE_SCROLL = 0x2E
    SET_VERTICAL_SCROLL_AREA = 0xA3
    RIGHT_HORIZONTAL_SCROLL = 0x26
    LEFT_HORIZONTAL_SCROLL = 0x27
    VERTICAL_AND_RIGHT_HORIZONTAL_SCROLL = 0x29
    VERTICAL_AND_LEFT_HORIZONTAL_SCROLL = 0x2A

    # Device name will be /dev/spidev-{bus}.{device}
    # dc_pin is the data/commmand pin.  This line is HIGH for data, LOW for command.
    # We will keep d/c low and bump it high only for commands with data
    # reset is normally HIGH, and pulled LOW to reset the display

    def __init__(self, bus=0, device=0, dc_pin=1, reset_pin=2):
        self.cols = 128
        self.rows = 32
        self.buffer_cols = 128
        self.buffer_rows = 64
        self.dc_pin = dc_pin
        self.reset_pin = reset_pin
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 500000
        self.gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.gpio.pinMode(self.reset_pin, self.gpio.OUTPUT)
        self.gpio.digitalWrite(self.reset_pin, self.gpio.HIGH)
        self.gpio.pinMode(self.dc_pin, self.gpio.OUTPUT)
        self.gpio.digitalWrite(self.dc_pin, self.gpio.LOW)
        self.font = font5x8.Font5x8
        #self.font = font10x16.Font10x16
        self.buffer = [0] * (self.buffer_cols * self.buffer_rows / 8)

    def reset(self):
        self.gpio.digitalWrite(self.reset_pin, self.gpio.LOW)
        self.gpio.delay(10) # 10ms
        self.gpio.digitalWrite(self.reset_pin, self.gpio.HIGH)

    def command(self, *bytes):
        #self.gpio.digitalWrite(self.dc_pin, self.gpio.LOW)
        self.spi.writebytes(list(bytes))

    def data(self, bytes):
        self.gpio.digitalWrite(self.dc_pin, self.gpio.HIGH)
        self.spi.writebytes(bytes)
        self.gpio.digitalWrite(self.dc_pin, self.gpio.LOW)
        
    def begin(self, vcc_state = SWITCHCAPVCC):
        self.gpio.delay(1) # 1ms
        self.reset()
        self.command(self.DISPLAYOFF)
        self.command(self.SETDISPLAYCLOCKDIV, 0x80)
        self.command(self.SETMULTIPLEX, 0x1F)
        self.command(self.SETDISPLAYOFFSET, 0x00)
        self.command(self.SETSTARTLINE | 0x00)
        if (vcc_state == self.EXTERNALVCC):
            self.command(self.CHARGEPUMP, 0x10)
        else:
            self.command(self.CHARGEPUMP, 0x14)
        self.command(self.MEMORYMODE, 0x00)
        self.command(self.SEGREMAP | 0x01)
        self.command(self.COMSCANDEC)
        self.command(self.SETCOMPINS, 0x02)
        self.command(self.SETCONTRAST, 0x8f)
        if (vcc_state == self.EXTERNALVCC):
            self.command(self.SETPRECHARGE, 0x22)
        else:
            self.command(self.SETPRECHARGE, 0xF1)
        self.command(self.SETVCOMDETECT, 0x40)
        self.command(self.DISPLAYALLON_RESUME)
        self.command(self.NORMALDISPLAY)
        self.command(self.DISPLAYON)
        
    def clear_display(self):
        for i in range(0,len(self.buffer)):
            self.buffer[i] = 0

    def invert_display(self):
        self.command(self.INVERTDISPLAY)

    def normal_display(self):
        self.command(self.NORMALDISPLAY)

    def display(self):
        self.command(self.SETLOWCOLUMN | 0x0)
        self.command(self.SETHIGHCOLUMN | 0x0)
        self.command(self.SETSTARTLINE | 0x0)
        self.data(self.buffer)

    def start_scroll_right(self, start, stop):
        pass

    def draw_pixel(self, x, y, on=True):
        if (x<0 or x>=self.buffer_cols or y<0 or y>=self.buffer_rows):
            return
        mem_col = x
        mem_row = y / 8
        bit_mask = 1 << (y % 8)
        offset = mem_row * self.buffer_cols + mem_col
        #print [x,y,mem_row, mem_col, offset]
        if on:
            self.buffer[offset] |= bit_mask
        else:
            self.buffer[offset] &= (0xFF - bit_mask)
        
    def draw_text(self, x, y, string):
        font_bytes = self.font.bytes
        font_rows = self.font.rows
        font_cols = self.font.cols
        for c in string:
            p = ord(c) * font_cols
            for col in range(0,font_cols):
                mask = font_bytes[p]
                p+=1
                for row in range(0,8):
                    self.draw_pixel(x,y+row,mask & 0x1)
                    mask >>= 1
                x += 1

    def draw_text2(self, x, y, string, size):
        font_bytes = self.font.bytes
        font_rows = self.font.rows
        font_cols = self.font.cols
        for c in string:
            p = ord(c) * font_cols
            for col in range(0,font_cols):
                mask = font_bytes[p]
                p+=1
                py = y
                for row in range(0,8):
                    for sy in range(0,size):
                        px = x
                        for sx in range(0,size):
                            self.draw_pixel(px,py,mask & 0x1)
                            px += 1
                        py += 1
                    mask >>= 1
                x += size
    
