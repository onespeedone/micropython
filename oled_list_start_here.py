import random
import utime
from time import sleep
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128,32,i2c)

# oled.fill(0)
# oled.text("Hello",0,0)
# oled.show()


# I2C_ADDR     = 0x27
# I2C_NUM_ROWS = 2
# I2C_NUM_COLS = 16
# 
# i2c = I2C(0, sda=machine.Pin(20), scl=machine.Pin(21), freq=400000)
# lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS) 

#lcd.clear()

file = open('file.txt')
content = file.readlines()

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# the lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail
button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)


# this function gets called every time the button is pressed
def button_pressed_handler(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200: 
        button_presses +=1
        last_time = new_time
        randsom = random.randrange(0,24)
        oled.fill(0)
        oled.text(content[randsom],0,10)
        oled.show()
        #print(content[randsom])
        
        
# now we register the handler function when the button is pressed
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

# This is for only printing when a new button press count value happens
old_presses = 0
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        old_presses = button_presses

