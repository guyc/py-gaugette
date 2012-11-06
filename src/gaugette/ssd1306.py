import spidev
import wiringpi
import time

# Datasheet: http://www.adafruit.com/datasheets/SSD1306.pdf
# Arduino library: https://github.com/adafruit/Adafruit_SSD1306

class SSD1306:

    # externally accessible as gaugette.ssd1306.SSD1306.CONST
    # or instance.CONST

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
    def __init__(self, bus=0, device=0, reset_pin=1):
        self.reset_pin = reset_pin
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.gpio.pinMode(self.reset_pin, self.gpio.OUTPUT)
        self.gpio.digitalWrite(self.reset_pin, self.gpio.HIGH)

    def reset(self):
        self.gpio.digitalWrite(self.reset_pin, self.gpio.LOW)
        self.gpio.delay(10) # 10ms
        self.gpio.digitalWrite(self.reset_pin, self.gpio.HIGH)

    def command(self, *bytes):
        self.spi.xfer2(list(bytes))
        
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
        pass

    def invert_display(self):
        pass

    def display(self):
        pass

    def start_scroll_right(self, start, stop):
        pass

    def draw_pixel(self, x, y, color):
        pass

    
