from machine import Pin, I2C
import time
from lcd_i2c import LCD # micropython_i2c_lcd

# The onboard LED is connected to GP25 on the Pico
led = Pin("LED", Pin.OUT)

# The button is connected to GP15
button = Pin(15, Pin.IN, Pin.PULL_UP)

# PCF8574 on 0x50
I2C_ADDR = 0x27     # DEC 39, HEX 0x27
NUM_ROWS = 2
NUM_COLS = 16

# define custom I2C interface, default is 'I2C(0)'
# check the docs of your device for further details and pin infos
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=800000)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c) # Must be connected to 5v!!!

while True:
    # If the button is pressed (logic low because of the pull-up resistor)
    if button.value() == 0:
        # Turn the LED on
        led.value(1)
        lcd.begin()
        lcd.print("Button Pressed")
        time.sleep(5)
        lcd.clear()
    else:
        # Turn the LED off
        led.value(0)
    
    # Wait for a bit so we're not constantly polling the button
    time.sleep(0.1)
