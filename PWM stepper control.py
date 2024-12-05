from machine import Pin, Timer, PWM
from time import sleep

led = PWM(Pin(16))
button = Pin(26, Pin.IN, Pin.PULL_UP)
step = PWM(Pin(14))
direction = Pin(13, Pin.OUT)
enable = Pin(12, Pin.OUT)

# variables
pulse = True
direction.value(0)
enable.value(0)
pot_freq = 0
led.freq(4000)
step.freq(5800)

def motorspin():
    global pulse
    pulse = not pulse
    step.value(pulse)
    

while True:
    logic_state = button.value()
    if logic_state == False:
        
        step.duty_u16(32000)
        
    else:
        step.duty_u16(0)
        
        
