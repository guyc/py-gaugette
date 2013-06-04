import wiringpi2

class CapSwitch:
    def __init__(self, pin):
        self.pin = pin
        self.gpio = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)
        self.gpio.pinMode(self.pin, self.gpio.OUTPUT)
        self.maxCycles = 100
        self.repeats = 2
        self.threshold = 40

    def sense(self):
        for i in range(0,self.repeats):

            # 1) set pin low and to output to discharge
            self.gpio.pinMode(self.pin, self.gpio.OUTPUT)
            self.gpio.digitalWrite(self.pin, self.gpio.LOW)
    
            # 2) make the pin an input without the internal pull-up on
            self.gpio.pinMode(self.pin, self.gpio.INPUT)
            self.gpio.pullUpDnControl(self.pin, self.gpio.PUD_OFF)

            # 3) read input and see how long it takes to go high

            cycles = 0
            total = 0.0
            while (cycles<self.maxCycles and self.gpio.digitalRead(self.pin)==0):
                cycles+=1;

            total += cycles
        mean = total / self.repeats
    
        return (mean > self.threshold)
            

        
        
        
