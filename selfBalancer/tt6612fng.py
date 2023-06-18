# Makers Digest
# DC Motor Control with tb6612fng dual bridge motor controller

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PWM Frequency
pwmFreq = 100

# Setup Pins for motor controller
GPIO.setup(18, GPIO.OUT) # PWMA
GPIO.setup(24, GPIO.OUT) # AIN2
GPIO.setup(23, GPIO.OUT) # AIN1
GPIO.setup(25, GPIO.OUT) # STBY
GPIO.setup(22, GPIO.OUT) # BIN1
GPIO.setup(27, GPIO.OUT) # BIN2
GPIO.setup(17, GPIO.OUT) # PWMB

pwma = GPIO.PWM(18, pwmFreq)
pwmb = GPIO.PWM(17, pwmFreq)
pwma.start(100)
pwmb.start(100)

## Functions
###########################################
def forward(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 0)
    print('Forward')
def reverse(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 1)
    print('Reverse')
    
def turnLeft(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 1)
    print('Left')
    
def turnRight(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 0)
    print('Right')
    
def runMotor(motor, spd, direction):
    GPIO.output(25, GPIO.HIGH)
    in1 = GPIO.HIGH
    in2 = GPIO.LOW
    
    if direction == 1:
        in1 = GPIO.LOW
        in2 = GPIO.HIGH
        
    if motor == 0:
        GPIO.output(23, in1)
        GPIO.output(24, in2)
        pwma.ChangeDutyCycle(spd)
    elif motor == 1:
        GPIO.output(22, in1)
        GPIO.output(27, in2)
        pwmb.ChangeDutyCycle(spd)
        
def motorStop():
    GPIO.output(25, GPIO.LOW)
    print('Stop')
    
# Main
#################################################

def main(args = None):
    while True:
        forward(20)
        sleep(2)
        motorStop()
        sleep(.25)
        
        reverse(20)
        sleep(2)
        motorStop()
        sleep(.25)
        
        turnLeft(20)
        sleep(2)
        motorStop()
        sleep(.25)
        
        turnRight(20)
        sleep(2)
        motorStop()
        sleep(.25)
        
try:
    if __name__ == '__main__':
        main()
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
        