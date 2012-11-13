===============
Gaugette Python Library
===============

A library for interfacing hardware with the Raspberry Pi.
Supports analog gauges, capacitance switches, RGB leds and other devices.

Prerequisites
=============

Modules that use GPIO require wiringpi.
gaugette.ssd1306 requires spidev.
gaugette.oauth2 requires Google's gdata.

SSD1306 OLED Usage
==================

    import gaugette.ssd1306
    RESET_PIN = 15
    DC_PIN    = 16
    led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
    led.begin()
    led.clear_display()
    led.draw_text2(0,0,'Hello World',2)
    led.display()

OAuth Usage
===========

    import gaugette.oauth
    CLIENT_ID       = 'your client_id here'
    CLIENT_SECRET   = 'your client secret here'

    oauth = gaugette.oauth.OAuth(CLIENT_ID, CLIENT_SECRET)
    if not oauth.has_token():
        user_code = oauth.get_user_code()
        print "Go to %s and enter the code %s" % (oauth.verification_url, user_code)
        oauth.get_new_token()

CapSwitch Usage
===============

    import gaugette.capswitch
    SWICH_PIN = 3
    switch = gaugette.capswitch.CapSwitch(SWITCH_PIN)
    while True:
        if switch.sense():
            print 'sensed'

Rgb Led Usage
=============

    import gaugette.rgbled
    R_PIN = 4
    G_PIN = 5
    B_PIN = 6
    led = gaugette.rgbled.RgbLed(R_PIN,R_PIN,B_PIN)
    led.set(0,50,100)
    led.fade(100,0,0)

Font Usage
==========

    from gaugette.fonts import arial_16
    font = arial_16  # fonts are modules, instance does not need to be instantiated
    led.draw_text3(0,0,'Hello World',font)

Discussion At
=============

https://guy.carpenter.id.au/gaugette/
