
import RPi.GPIO as GPIO
import time
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#define GPIO pins motor 1
direction= 22 # Direction (DIR) GPIO Pin
step = 20 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

#define GPIO pins motor 2
directionpin2= 7 # Direction (DIR) GPIO Pin
step2 = 16 # Step GPIO Pin
EN_pin2 = 23 # enable pin (LOW to enable)

limswitch_fwd = Button(12, pull_up = False)

travel = 4500 # motor 1 steps for linear travel // .0002" linear travel per pulse
travel2 = 400 # motor 2 steps for key turn
pulse = 0
totalcount = 0
direction1 = 0
direction2 = 0
cycles = int(input("Enter Number of Cycles:"))
cyclesstart = cycles

# motor 1 enable setup and ouput
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
# motor 2 enable setup and ouput
GPIO.setup(EN_pin2,GPIO.OUT) # set enable pin as output
GPIO.output(EN_pin2,GPIO.LOW) # pull enable to low to enable motor

def motor1fwd():
    global travel, pulse, direction1, test, cycles
    while travel > 0:
        direction1 = 1
        travel -= 1
        pulse = (1,0)[pulse]
        motor1()
        time.sleep(.00002)
    else:
        motor2fwd()
        
def motor1rev():
    global travel, pulse, direction1, travel2, direction2, cycles
    while travel > 0:
        direction1 = 0
        travel -= 1
        pulse = (1,0)[pulse]
        motor1()
        time.sleep(.00002)
    else:
        travel = 4500
        travel2 = 400
        direction2 = 1
        cycles -= 1
        print("cycles remaining", cycles)
        motor1fwd()
            
def motor2fwd():
    global travel, travel2, pulse, direction2
    while travel2 > 0 and travel2 <= 400:
        direction2 = 0
        travel2 -= 1
        pulse = (1,0)[pulse]
        motor2()
        time.sleep(.00002)
    else:
        travel2 = 401
        direction2 = 1
        pulse = 0
        motor2rev()
            
def motor2rev():
    global travel, travel2, pulse, direction2
    while travel2 < 800:
        travel2 += 1
        pulse = (1,0)[pulse]
        motor2()
        time.sleep(.0005)
    else:
        travel = 4500
        travel2 = 400
        motor1rev()

def motor1():
    GPIO.setup(step,GPIO.OUT)
    GPIO.setup(direction,GPIO.OUT)
    GPIO.output(step, pulse) # toggle is the same a pulse/step
    GPIO.output(direction,direction1) # LOW = CCW, HIGH = CW
    
def motor2():
    GPIO.setup(step2,GPIO.OUT)
    GPIO.setup(directionpin2,GPIO.OUT)
    GPIO.output(step2, pulse) # toggle is the same a pulse/step
    GPIO.output(directionpin2,direction2) # LOW = CCW, HIGH = CW

motor1fwd()

GPIO.cleanup() # clear GPIO allocations after run





