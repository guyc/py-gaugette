import imp

class SPI:
    def __init__(self, bus, device):
           
        try:
            SPILIB = 'spidev'
            imp.find_module('spidev')

        except ImportError:
            SPILIB = 'Adafruit_BBIO'
    
            if (SPILIB == 'spidev'):
                import spidev
                import spidev
                self.spi = spidev
                self.writebytes = self.spi.writebytes
                
            elif (SPILIB == 'Adafruit_BBIO'):
                import Adafruit_BBIO.SPI
                self.spi = Adafruit_BBIO.SPI.SPI(bus, device)
                self.writebytes = self.spi.writebytes
