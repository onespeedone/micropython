
import RPi.GPIO as GPIO
import time
from gpiozero import Button
import tkgpio

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

travel = 4250 # motor 1 steps for linear travel // .0002" linear travel per pulse
travel2 = 400 # motor 2 steps for key turn
pulse = False #JJM
totalcount = 0
direction1 = False #False = reverse
direction2 = True
cycles = int(input("Enter Number of Cycles:"))
cyclesstart = cycles


# motor 1 enable setup and ouput
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
# motor 2 enable setup and ouput
GPIO.setup(EN_pin2,GPIO.OUT) # set enable pin as output
GPIO.output(EN_pin2,GPIO.LOW) # pull enable to low to enable motor

def motor1cal():
    global travel, pulse, direction1, cycles #JJM
    direction1 = True
    while limswitch_fwd.is_pressed == False:
            pulse = not pulse #JJM
            motor1()
            time.sleep(.001)
    else:
        motor1start()

def motor1start():
    global travel, pulse, direction1, cycles #JJM
    direction1 = False
    for x in range(travel): #JJM
            pulse = not pulse #JJM
            motor1()
            time.sleep(.0002)
    else:
        motor1fwd()
        
def motor1end():
    global travel, pulse, direction1, cycles #JJM
    travel = 14000
    direction1 = False
    for x in range(travel): #JJM
            pulse = not pulse #JJM
            motor1()
            time.sleep(.0003)
    print("Done!")

def motor1fwd():
    global travel, pulse, direction1, cycles #JJM
    if cycles > 0:
        direction1 = True
        for z in range(2):
            direction1 = not direction1
            for x in range(travel): #JJM
                pulse = not pulse #JJM
                motor1()
                time.sleep(.0001)
        else:
            cycles -= 1
            print ("Cycles remaining: ", cycles)
            motor2fwd()
    else:
        motor1end()
        
def motor2fwd():
    global pulse, direction2, cycles #JJM
    for y in range(2):
            direction2 = not direction2 #JJM
            for x in range(travel2): #JJM
                pulse = not pulse #JJM
                motor2()
                time.sleep(.001)
    else:
        motor1fwd()

#limswitch_fwd.when_pressed = motor1start
        
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

motor1cal()

GPIO.cleanup() # clear GPIO allocations after run





