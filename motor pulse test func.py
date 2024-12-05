
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

travel = 80
pulse = 0

GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output
#GPIO.setup(direction,GPIO.OUT)
#GPIO.output(direction,direction1) # LOW = CCW, HIGH = CW
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
# motor 2
GPIO.setup(EN_pin2,GPIO.OUT) # set enable pin as output
GPIO.setup(direction2,GPIO.OUT)
GPIO.output(direction2,GPIO.LOW) # LOW = CCW, HIGH = CW
GPIO.output(EN_pin2,GPIO.LOW) # pull enable to low to enable motor

def limitswitchfwd():
    global travel, pulse
    while travel > 0:
        travel -= 1
        pulse = 0
        motor1()
        pulse = 1
        motor()
        time.sleep(.00001)

def motor1():
    GPIO.setup(step,GPIO.OUT)
    GPIO.setup(direction,GPIO.OUT)
    GPIO.output(step, pulse) # toggle is the same a pulse/step
    GPIO.output(direction,direction1) # LOW = CCW, HIGH = CW
    

limswitch_rev.when_pressed = rev_limit
limswitch_fwd.when_pressed = fwd_limit

limitswitchfwd()


GPIO.cleanup() # clear GPIO allocations after run




