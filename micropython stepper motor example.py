from machine import Pin, Timer
from time import sleep

button = Pin(26, Pin.IN, Pin.PULL_UP)
step = Pin(14, Pin.OUT)
direction = Pin(13, Pin.OUT)
enable = Pin(12, Pin.OUT)

# variables
pulse = True
direction.value(0)
enable.value(0)

def motorspin():
    global pulse
    pulse = not pulse
    step.value(pulse)
    

while True:
    logic_state = button.value()
    if logic_state == False:
        motorspin()
    sleep(.001)