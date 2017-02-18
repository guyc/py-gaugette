#----------------------------------------------------------------------
# sh1106.py from https://github.com/guyc/py-gaugette
# by Max Sheehan
# based on ssd1306.py by Guy Carpenter, Clearwater Software
#
# REVISIT : this should be refactored to remove duplicated code from ssd1306.py
# 
# This library works with
#   A 7-PIN 1.3 inch SPI (Not I2C) SH1106 OLED - Example:
#     https://www.amazon.co.uk/128X64-Display-Module-Board-Arduino/dp/B01GC6C1CA
#
# it should work with other SH1106-based displays.
# The datasheet for the SSH1106 is available
#  http://www.held-im-ruhestand.de/_downloads/oled-sh1106-datasheet.pdf
# The datasheet for the SSD1306 is available
#   http://www.adafruit.com/datasheets/SSD1306.pdf
#
# The code is based heavily on Adafruit's Arduino library
#   https://github.com/adafruit/Adafruit_SSD1306
# written by Limor Fried/Ladyada for Adafruit Industries.
#
# Some important differences between the SH1106 and SSD1306
#
# - The SH1106 does not support switching memory mode to vertical.
#   Therefore the logic in the Bitmap helper class has been modified.
#
# - The page and column have to be reset when you reach the end of a line
#   this is handled in the display_block method.
#
# - The memory in the SH1106 is 132x64 although the OLED I have is only
#   128x64. The first 2 and last 2 columns are not displayed.
#   So it's best if these columns are not used.
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
# SPI and GPIO calls are made through an abstraction library that calls
# the appropriate library for the platform.
# For the RaspberryPi:
#     wiring2
#     spidev
# For the BeagleBone Black:
#     Adafruit_BBIO.SPI
#     Adafruit_BBIO.GPIO
#
# - The pin connections between the BeagleBone Black SPI0 and OLED module are:
#
#      BBB       SH1106
#      P9_17  -> CS
#      P9_15  -> RST   (arbirary GPIO, change at will)
#      P9_13  -> D/C   (arbirary GPIO, change at will)
#      P9_22  -> CLK
#      P9_18  -> DATA
#      P9_3   -> VIN
#      P9_1   -> GND
#----------------------------------------------------------------------

import gaugette.platform
import gaugette.gpio
import gaugette.spi
import gaugette.font5x8
import time
import sys

class SH1106:

    # Class constants are externally accessible as gaugette.sh1106.SH1106.CONST
    # or my_instance.CONST

    # TODO - insert underscores to rationalize constant names

    EXTERNAL_VCC   = 0x1
    SWITCH_CAP_VCC = 0x2

    SET_LOW_COLUMN        = 0x00
    SET_HIGH_COLUMN       = 0x10
    #SET_MEMORY_MODE       = 0x20
    #SET_COL_ADDRESS       = 0x21
    RIGHT_HORIZ_SCROLL    = 0x26
    LEFT_HORIZ_SCROLL     = 0x27
    VERT_AND_RIGHT_HORIZ_SCROLL = 0x29
    VERT_AND_LEFT_HORIZ_SCROLL = 0x2A
    DEACTIVATE_SCROLL     = 0x2E
    ACTIVATE_SCROLL       = 0x2F
    SET_START_LINE        = 0x40
    SET_CONTRAST          = 0x81
    CHARGE_PUMP           = 0x8D
    SET_PAGE_ADDRESS      = 0xB0 #0x22
    SEG_REMAP             = 0xA0
    SET_VERT_SCROLL_AREA  = 0xA3
    DISPLAY_ALL_ON_RESUME = 0xA4
    DISPLAY_ALL_ON        = 0xA5
    NORMAL_DISPLAY        = 0xA6
    INVERT_DISPLAY        = 0xA7
    DISPLAY_OFF           = 0xAE
    DISPLAY_ON            = 0xAF
    COM_SCAN_INC          = 0xC0
    COM_SCAN_DEC          = 0xC8
    SET_DISPLAY_OFFSET    = 0xD3
    SET_COM_PINS          = 0xDA
    SET_VCOM_DETECT       = 0xDB
    SET_DISPLAY_CLOCK_DIV = 0xD5
    SET_PRECHARGE         = 0xD9
    SET_MULTIPLEX         = 0xA8

    #MEMORY_MODE_HORIZ = 0x00
    #MEMORY_MODE_VERT  = 0x01
    #MEMORY_MODE_PAGE  = 0x02

    # Device name will be /dev/spidev-{bus}.{device}
    # dc_pin is the data/commmand pin.  This line is HIGH for data, LOW for command.
    # We will keep d/c low and bump it high only for commands with data
    # reset is normally HIGH, and pulled LOW to reset the display

    def __init__(self, gpio, spi, dc_pin="P9_15", reset_pin="P9_13", buffer_rows=64, buffer_cols=132, rows=64, cols=132):
        self.gpio = gpio
        self.spi = spi
        self.cols = cols
        self.rows = rows
        self.buffer_rows = buffer_rows
        self.mem_bytes = self.buffer_rows * self.cols >> 3 # total bytes in SH1106 display ram
        self.dc_pin = dc_pin
        self.reset_pin = reset_pin
        self.gpio.setup(self.reset_pin, self.gpio.OUT)
        self.gpio.output(self.reset_pin, self.gpio.HIGH)
        self.gpio.setup(self.dc_pin, self.gpio.OUT)
        self.gpio.output(self.dc_pin, self.gpio.LOW)
        self.font = gaugette.font5x8.Font5x8
        self.col_offset = 0
        self.bitmap = self.Bitmap(buffer_cols, buffer_rows)
        self.flipped = False

    def reset(self):
        self.gpio.output(self.reset_pin, self.gpio.LOW)
        time.sleep(0.010) # 10ms
        self.gpio.output(self.reset_pin, self.gpio.HIGH)
        time.sleep(0.010) # 10ms

    def command(self, *bytes):
        self.spi.writebytes(list(bytes))

    def data(self, bytes):
        self.gpio.output(self.dc_pin, self.gpio.HIGH)
        # chunk data to work around 255 byte limitation in adafruit implementation of writebytes
        # revisit - change to 1024 when Adafruit_BBIO is fixed.
        max_xfer = 255 if gaugette.platform.isBeagleBoneBlack else 1024
        start = 0
        remaining = len(bytes)
        while remaining > 0:
            count = remaining if remaining <= max_xfer else max_xfer
            remaining -= count
            self.spi.writebytes(bytes[start:start+count])
            start += count
        self.gpio.output(self.dc_pin, self.gpio.LOW)

    def begin(self, vcc_state=SWITCH_CAP_VCC):
        self.reset()
        self.command(self.DISPLAY_OFF)
        self.command(self.SET_DISPLAY_CLOCK_DIV, 0x80)

        # support for 128x32 and 128x64 line models
        if self.rows == 64:
            self.command(self.SET_MULTIPLEX, 0x3F)
            self.command(self.SET_COM_PINS, 0x12)
        else:
            self.command(self.SET_MULTIPLEX, 0x1F)
            self.command(self.SET_COM_PINS, 0x02)

        self.command(self.SET_DISPLAY_OFFSET, 0x00)
        self.command(self.SET_START_LINE | 0x00)
        if vcc_state == self.EXTERNAL_VCC:
            self.command(self.CHARGE_PUMP, 0x10)
        else:
            self.command(self.CHARGE_PUMP, 0x14)
        # self.command(self.SET_MEMORY_MODE, 0x00)
        self.command(self.SEG_REMAP | 0x01)
        self.command(self.COM_SCAN_DEC)
        self.command(self.SET_CONTRAST, 0x8f)
        if vcc_state == self.EXTERNAL_VCC:
            self.command(self.SET_PRECHARGE, 0x22)
        else:
            self.command(self.SET_PRECHARGE, 0xF1)
        self.command(self.SET_VCOM_DETECT, 0x40)
        self.command(self.DISPLAY_ALL_ON_RESUME)
        self.command(self.NORMAL_DISPLAY)
        self.command(self.DISPLAY_ON)

    def clear_display(self):
        self.bitmap.clear()

    def invert_display(self):
        self.command(self.INVERT_DISPLAY)

    def flip_display(self, flipped=True):
        self.flipped = flipped
        if flipped:
            self.command(self.COM_SCAN_INC)
            self.command(self.SEG_REMAP | 0x00)
        else:
            self.command(self.COM_SCAN_DEC)
            self.command(self.SET_COM_PINS, 0x02)

    def normal_display(self):
        self.command(self.NORMAL_DISPLAY)

    def set_contrast(self, contrast=0x7f):
        self.command(self.SET_CONTRAST, contrast)

    def display(self):
        self.display_block(self.bitmap, 0, 0, self.cols, self.col_offset)

    def display_cols(self, start_col, count):
        self.display_block(self.bitmap, 0, start_col, count, self.col_offset)

    # Transfers data from the passed bitmap (instance of sh1106.Bitmap)
    # starting at row <row> col <col>.
    # Both row and bitmap.rows will be divided by 8 to get page addresses,
    # so both must divide evenly by 8 to avoid surprises.
    #
    # bitmap:     instance of Bitmap
    #             The number of rows in the bitmap must be a multiple of 8.
    # row:        Starting row to write to - must be multiple of 8
    # col:        Starting col to write to.
    # col_count:  Number of cols to write.
    # col_offset: column offset in buffer to write from
    #
    def display_block(self, bitmap, row, col, col_count, col_offset=0):
        # The code here differs from the SSD1306
        # since the SH1106 doesn't support SET_COL_ADDRESS
        # or Vertical memory mode
        page_count = bitmap.rows >> 3
        page_start = row >> 3
        page_end   = page_start + page_count - 1
        col_start_l = col & 0x0F
        col_start_h = (col >> 4) & 0x0F
        col_end    = col + col_count - 1

        length = col_count
        while (page_start <= page_end):
            self.command(self.SET_PAGE_ADDRESS | page_start)
            self.command(self.SET_LOW_COLUMN  | col_start_l)
            self.command(self.SET_HIGH_COLUMN | col_start_h)
            start = (col_offset * page_count) + (page_start * bitmap.cols)
            self.data(bitmap.data[start:start+length])
            page_start += 1

    # Diagnostic print of the memory buffer to stdout
    def dump_buffer(self):
        self.bitmap.dump()

    def draw_pixel(self, x, y, on=True):
        self.bitmap.draw_pixel(x, y, on)

    def draw_text(self, x, y, string):
        font_bytes = self.font.bytes
        font_rows = self.font.rows
        font_cols = self.font.cols
        for c in string:
            p = ord(c) * font_cols
            for col in range(0, font_cols):
                mask = font_bytes[p]
                p += 1
                for row in range(0, 8):
                    self.draw_pixel(x, y + row, mask & 0x1)
                    mask >>= 1
                x += 1

    def draw_text2(self, x, y, string, size=2, space=1):
        font_bytes = self.font.bytes
        font_rows = self.font.rows
        font_cols = self.font.cols
        for c in string:
            p = ord(c) * font_cols
            for col in range(0, font_cols):
                mask = font_bytes[p]
                p += 1
                py = y
                for row in range(0, 8):
                    for sy in range(0, size):
                        px = x
                        for sx in range(0, size):
                            self.draw_pixel(px, py, mask & 0x1)
                            px += 1
                        py += 1
                    mask >>= 1
                x += size
            x += space

    def clear_block(self, x0, y0, dx, dy):
        self.bitmap.clear_block(x0, y0, dx, dy)

    def draw_text3(self, x, y, string, font):
        return self.bitmap.draw_text(x, y, string, font)

    def text_width(self, string, font):
        return self.bitmap.text_width(string, font)

    class Bitmap:

        # No longer column major due to the SH1106 not supporting
        # Vertical write mode
        def __init__(self, cols, rows):
            self.rows = rows
            self.cols = cols
            self.bytes_per_col = rows >> 3
            self.data = [0] * (self.cols * self.bytes_per_col)

        def clear(self):
            for i in range(0,len(self.data)):
                self.data[i] = 0

        # Diagnostic print of the memory buffer to stdout
        def dump(self):
            for y in range(0, self.rows):
                mem_row = y >> 3
                bit_mask = 1 << (y % 8)
                line = ""
                for x in range(0, self.cols):
                    mem_col = x
                    offset = mem_row * self.cols + mem_col
                    if self.data[offset] & bit_mask:
                        line += '*'
                    else:
                        line += ' '
                print('|'+line+'|')

        def draw_pixel(self, x, y, on=True):
            if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
                return
            mem_col = x
            mem_row = y >> 3
            bit_mask = 1 << (y % 8)
            offset = mem_row * self.cols + mem_col

            if on:
                self.data[offset] |= bit_mask
            else:
                self.data[offset] &= (0xFF - bit_mask)

        def clear_block(self, x0, y0, dx, dy):
            for x in range(x0, x0 + dx):
                for y in range(y0, y0 + dy):
                    self.draw_pixel(x, y, 0)

        # returns the width in pixels of the string allowing for kerning & interchar-spaces
        def text_width(self, string, font):
            x = 0
            prev_char = None
            for c in string:
                if c < font.start_char or c > font.end_char:
                    if prev_char != None:
                        x += font.space_width + prev_width + font.gap_width
                    prev_char = None
                else:
                    pos = ord(c) - ord(font.start_char)
                    (width, offset) = font.descriptors[pos]
                    if prev_char != None:
                        x += font.kerning[prev_char][pos] + font.gap_width
                    prev_char = pos
                    prev_width = width

            if prev_char != None:
                x += prev_width

            return x

        def draw_text(self, x, y, string, font):
            height = font.char_height
            prev_char = None

            for c in string:
                if c < font.start_char or c > font.end_char:
                    if prev_char != None:
                        x += font.space_width + prev_width + font.gap_width
                    prev_char = None
                else:
                    pos = ord(c) - ord(font.start_char)
                    (width, offset) = font.descriptors[pos]
                    if prev_char != None:
                        x += font.kerning[prev_char][pos] + font.gap_width
                    prev_char = pos
                    prev_width = width

                    bytes_per_row = (width + 7) >> 3
                    for row in range(0, height):
                        py = y + row
                        mask = 0x80
                        p = offset
                        for col in range(0, width):
                            px = x + col
                            if font.bitmaps[p] & mask:
                                self.draw_pixel(px, py, 1)  # for kerning, never draw black
                            mask >>= 1
                            if mask == 0:
                                mask = 0x80
                                p += 1
                        offset += bytes_per_row

            if prev_char != None:
                x += prev_width

            return x

    # This is a helper class to display a scrollable list of text lines.
    # The list must have at least 1 item.
    class ScrollingList:
        def __init__(self, sh1106, list, font):
            self.sh1106 = sh1106
            self.list = list
            self.font = font
            self.position = 0 # row index into list, 0 to len(list) * self.rows - 1
            self.offset = 0   # led hardware scroll offset
            self.pan_row = -1
            self.pan_offset = 0
            self.pan_direction = 1
            self.bitmaps = []
            self.rows = sh1106.rows
            self.cols = sh1106.cols
            self.bufrows = self.rows * 2
            downset = (self.rows - font.char_height) >> 1
            for text in list:
                width = sh1106.cols
                text_bitmap = sh1106.Bitmap(width, self.rows)
                width = text_bitmap.draw_text(0, downset, text, font)
                if width > 128:
                    text_bitmap = sh1106.Bitmap(width + 15, self.rows)
                    text_bitmap.draw_text(0, downset, text, font)
                self.bitmaps.append(text_bitmap)

            # display the first word in the first position
            self.sh1106.display_block(self.bitmaps[0], 0, 0, self.cols)

        # how many steps to the nearest home position
        def align_offset(self):
            pos = self.position % self.rows
            midway = self.rows >> 1
            delta = (pos + midway) % self.rows - midway
            return -delta

        def align(self, delay=0.005):
            delta = self.align_offset()
            if delta != 0:
                steps = abs(delta)
                sign = delta // steps
                for i in range(0, steps):
                    if i > 0 and delay > 0:
                        time.sleep(delay)
                    self.scroll(sign)
            return self.position // self.rows

        # scroll up or down.  Does multiple one-pixel scrolls if delta is not >1 or <-1
        def scroll(self, delta):
            if delta == 0:
                return

            count = len(self.list)
            step = (delta > 0) - (delta < 0) # step = 1 or -1
            for i in range(0, delta, step):
                if (self.position % self.rows) == 0:
                    n = self.position // self.rows
                    # at even boundary, need to update hidden row
                    m = (n + step + count) % count
                    row = (self.offset + self.rows) % self.bufrows
                    self.sh1106.display_block(self.bitmaps[m], row, 0, self.cols)
                    if m == self.pan_row:
                        self.pan_offset = 0
                self.offset = (self.offset + self.bufrows + step) % self.bufrows
                self.sh1106.command(self.sh1106.SET_START_LINE | self.offset)
                max_position = count * self.rows
                self.position = (self.position + max_position + step) % max_position

        # pans the current row back and forth repeatedly.
        # Note that this currently only works if we are at a home position.
        def auto_pan(self):
            n = self.position // self.rows
            if n != self.pan_row:
                self.pan_row = n
                self.pan_offset = 0

            text_bitmap = self.bitmaps[n]
            if text_bitmap.cols > self.cols:
                row = self.offset # this only works if we are at a home position
                if self.pan_direction > 0:
                    if self.pan_offset <= (text_bitmap.cols - self.cols):
                        self.pan_offset += 1
                    else:
                        self.pan_direction = -1
                else:
                    if self.pan_offset > 0:
                        self.pan_offset -= 1
                    else:
                        self.pan_direction = 1
                self.sh1106.display_block(text_bitmap, row, 0, self.cols, self.pan_offset)
