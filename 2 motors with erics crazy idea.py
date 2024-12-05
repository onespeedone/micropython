
import RPi.GPIO as GPIO
import time
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#define GPIO pins
direction= 22 # Direction (DIR) GPIO Pin
step = 20 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

#define GPIO pins
direction2= 17 # Direction (DIR) GPIO Pin
step2 = 16 # Step GPIO Pin
EN_pin2 = 23 # enable pin (LOW to enable)

limswitch_rev = Button(13)
limswitch_fwd = Button(12, pull_up = False)

counter = 0
motor1step = 1
toggle2 = 1
timer1 = 0
timer2 = 0
direction1 = 0
lim_rev = True
lim_fwd = False
cycle = int(input("Enter Number of Cycles:")) # variable for number of cycles to perform
completedcycles = cycle # captures initial cycle count

GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
#GPIO.setup(direction,GPIO.OUT)
#GPIO.output(direction,direction1) # LOW = CCW, HIGH = CW
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
# motor 2
GPIO.setup(EN_pin2,GPIO.OUT) # set enable pin as output
GPIO.setup(direction2,GPIO.OUT)
GPIO.output(direction2,GPIO.LOW) # LOW = CCW, HIGH = CW
GPIO.output(EN_pin2,GPIO.LOW) # pull enable to low to enable motor

def fwd_limit():
    global lim_fwd, lim_rev, cycle, direction1
    lim_fwd = True
    lim_rev = False
    direction1 = 1
    cycle -= 1
    print ("fwd limit switch")
    print ("Number of cycles remaining", cycle)
    
        
def rev_limit():
    global lim_rev, lim_fwd, direction1
    lim_rev = True
    lim_fwd = False
    direction1 = 0
    #print("rev limit switch")

def motor1stephandler(): # motor 1 step/pulse handler
   global motor1step, timer1
   if timer1 == 3: # larger number = slower motor
       timer1 = 0
       motor1step = 0
   else:
       timer1 += 1
       motor1step = 1
              
def togglehandle2(): # motor 2 pulse/step handler
   global toggle2, timer2
   if timer2 == 10: # larger number = slower motor
       timer2 = 0
       toggle2 = 0
   else:
       timer2 += 1
       toggle2 = 1

def forward():
    GPIO.setup(step,GPIO.OUT)
    GPIO.setup(direction,GPIO.OUT)
    GPIO.output(step, motor1step) # toggle is the same a pulse/step
    GPIO.output(direction,direction1) # LOW = CCW, HIGH = CW
    

def forward2():
    GPIO.setup(step2,GPIO.OUT)
    GPIO.output(step2, toggle2)

limswitch_rev.when_pressed = rev_limit
limswitch_fwd.when_pressed = fwd_limit

while cycle > 0:
    time.sleep(.001)
    motor1stephandler()
    togglehandle2()
    forward()
    forward2()
# else:
#     #print("number of cycles completed", completedcycles)
#     direction1 = 0
#     forward() # reverse function call at end of cycle to pull motor off limit switch
#     forward()
#     forward()
#     forward()
#     forward()
#     forward()
#     forward()
#     forward()
#     forward()
#     forward()
#     print("number of cycles completed", completedcycles)


GPIO.cleanup() # clear GPIO allocations after run



