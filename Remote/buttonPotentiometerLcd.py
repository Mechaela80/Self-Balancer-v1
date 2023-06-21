"""To do:
        1. Enter one of four states with button - 'setpoint', 'P', 'I', 'D' 
        2. Set poentiometer output for each state
        3. Bluetooth connection to the Pi
        4. Make mapping less redundant (function?)
        
LCD1602: vcc->5v,gnd->gnd, SDA->GP0, SCL->GP1
Button: '+'->GP15, '-'->gnd
Potentiometer: '+'-> 3.3v, '-'->gnd, signal-> GP26from machine import Pin, ADC, I2C
import time
"""
from lcd_i2c import LCD

pot = ADC(Pin(26))  # assuming the potentiometer is connected to GPIO 26

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
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c) # Must be connected to 5v

# Create a map function to adjust the output range.
def map(x, in_min, in_max, out_min, out_max):
    """ Maps two ranges together """
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

#def mapped_value(): 
    

try:
    while True:
    
        if button.value() == 0:
            lcd.begin()
            while True:
                pot_value = pot.read_u16() # get the value of the potentiometer from the onboard ADC
                mapped = map(pot_value,288,65535,0,100)# Set range to 0-100 from 288-65535. Uses the map() function
                led.value(1)# Turn the LED on
                time.sleep(.2)
                lcd.clear() # refresh the LCD
                lcd.print(str(mapped)) # Print the mapped potentiometer value to the LCD
                print("LCD: ", mapped) # Print to the shell
            
        else:
            # Turn the LED off
            led.value(0)
            # Fix refresh
            pot_value = pot.read_u16() # How ot not duplicate??? vvv Too
            mapped = map(pot_value,288,65535,0,100) #same
        
            print("REPL: ", mapped, "pot: ", pot_value)  # read and print the value
            time.sleep(0.1)  # delay for a bit
except KeyboardInterrupt:
    lcd.clear()
    led.value(0)
    raise SystemExit # Exit the script











