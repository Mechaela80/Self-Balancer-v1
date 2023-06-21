from machine import Pin, ADC
import time

pot = ADC(Pin(26))  # assuming the potentiometer is connected to GPIO 26

def map(x, in_min, in_max, out_min, out_max):
    """ Maps two ranges together """
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)


while True:
    pot_value = pot.read_u16()
    mapped = map(pot_value,288,65535,0,100)
    print(mapped)  # read and print the value
    time.sleep(0.1)  # delay for a bit
