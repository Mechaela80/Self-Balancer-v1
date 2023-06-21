from machine import Pin
import time

# a dictionary of States and their Potentiometer  #mapping settings
States = {'Set Point': None, 'Kp': None, 'Ki': None, 'Kd': None}

# The onboard LED is connected to GP25 on the Pico
led = Pin("LED", Pin.OUT)

# The button is connected to GP15
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    # If the button is pressed (logic low because of the pull-up resistor)
    if button.value() == 0:
        # Turn the LED on
        led.value(1)
    else:
        # Turn the LED off
        led.value(0)
    
    # Wait for a bit so we're not constantly polling the button
    time.sleep(0.1)










