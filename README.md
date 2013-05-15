py-gaugette
===========

A library for interfacing hardware with the Raspberry Pi.
Supports analog gauges, capacitance switches, RGB leds and other devices.

Prerequisites
=============

 - Modules that use GPIO require [WiringPi-Python](https://github.com/WiringPi/WiringPi-Python).
 - gaugette.ssd1306 requires [spidev](https://github.com/doceme/py-spidev).
 - gaugette.oauth2 requires [Google's gdata](http://code.google.com/p/gdata-python-client/).

SSD1306 OLED Usage
==================

```python
    import gaugette.ssd1306
    RESET_PIN = 15
    DC_PIN    = 16
    led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
    led.begin()
    led.clear_display()
    led.draw_text2(0,0,'Hello World',2)
    led.display()
```

SSD1306 Font Usage
==================

```python
    from gaugette.fonts import arial_16
    font = arial_16  # fonts are modules, instance does not need to be instantiated
    led.draw_text3(0,0,'Hello World',font)
```

OAuth Usage
===========

```python
    import gaugette.oauth
    CLIENT_ID       = 'your client_id here'
    CLIENT_SECRET   = 'your client secret here'

    oauth = gaugette.oauth.OAuth(CLIENT_ID, CLIENT_SECRET)
    if not oauth.has_token():
        user_code = oauth.get_user_code()
        print "Go to %s and enter the code %s" % (oauth.verification_url, user_code)
        oauth.get_new_token()
```

CapSwitch Usage
===============

```python
    import gaugette.capswitch
    SWICH_PIN = 3
    switch = gaugette.capswitch.CapSwitch(SWITCH_PIN)
    while True:
        if switch.sense():
            print 'sensed'
```

Rgb Led Usage
=============

```python
    import gaugette.rgbled
    R_PIN = 4
    G_PIN = 5
    B_PIN = 6
    led = gaugette.rgbled.RgbLed(R_PIN,R_PIN,B_PIN)
    led.set(0,50,100)
    led.fade(100,0,0)
```

Rotary Encoder Usage
====================

```python
    import gaugette.rotary_encoder
    A_PIN = 7
    B_PIN = 9
    encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
    while True:
      delta = encoder.delta()
      if delta!=0:
        print "rotate %d" % delta
```

Switch Usage
====================

```python
    import gaugette.switch
    SW_PIN = 8
    sw = gaugette.switch.Switch(SW_PIN)
    last_state = sw.state()
    while True:
      state = sw.state()
      if state != last_state:
        print "switch %d" % state
        last_state = state
```

Discussion At
=============

[http://guy.carpenter.id.au/gaugette/](http://guy.carpenter.id.au/gaugette/)

Using This Module In Your Code
==============================

You can use this code by checking it out into your source directory as follows:

```
cd myApplication
git clone git://github.com/guyc/py-gaugette.git
ln -s py-gaugette/gaugette gaugette
```
The soft link is created so that the local directory `gaugette` will point to 
`py-gaugette/gaugette` which simplifies your import statements.

Alternatively if you want to install this module as a system-wide python module, you can
do so as follows:

```
cd myPythonStuff
git clone git://github.com/guyc/py-gaugette.git
cd py-gaugette
sudo python setup.py install
```


