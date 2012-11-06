import wiringpi

class RgbLed:

    def __init__(self, r_pin, g_pin, b_pin):
        self.r_pin = r_pin
        self.b_pin = b_pin
        self.g_pin = g_pin
        self.r_pwm = wiringpi.softPwmCreate(r_pin, 0, 100)
        self.g_pwm = wiringpi.softPwmCreate(g_pin, 0, 100)
        self.b_pwm = wiringpi.softPwmCreate(b_pin, 0, 100)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.set(0,0,0)

    def set(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        wiringpi.softPwmWrite(self.r_pin, red)
        wiringpi.softPwmWrite(self.g_pin, green)
        wiringpi.softPwmWrite(self.b_pin, blue)
        print [red,green,blue]

    def fade(self, red, green, blue, delay=100, interval=5):
        for i in range(0, delay, interval):
            f = (0.0+i)/delay
            r = self.red   + (red  -self.red)   * f
            wiringpi.softPwmWrite(self.r_pin, int(r))
            g = self.green + (green-self.green) * f
            wiringpi.softPwmWrite(self.g_pin, int(g))
            b = self.blue  + (blue -self.blue)  * f
            wiringpi.softPwmWrite(self.b_pin, int(b))
            wiringpi.delay(interval)
        self.red = red
        self.blue = blue
        self.green = green
