import random
import utime
from time import sleep
from machine import Pin

#button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)

file = open('file.txt')
content = file.readlines()

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# the lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)

def randy2():
    randsom = random.randrange(0,24)
    print(content[randsom])

# this function gets called every time the button is pressed
def button_pressed_handler(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200: 
        button_presses +=1
        last_time = new_time
        randsom = random.randrange(0,24)
        print(content[randsom])

# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_presses = 0
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        #print(button_presses)
        builtin_led.toggle()
        old_presses = button_presses

