from rotary import Rotary
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import rp2
from machine import Pin

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, set_init=rp2.PIO.IN_LOW)
def hx711():
    set(x, 24)           #generate 25 Pulses 1us on 1us off to initialise hx711 for channel A with gain 128
    label("loop1")
    nop()    .side(1)    [7]
    nop()    [1]
    nop()    .side(0)    [6]
    nop()    [1]
    jmp(x_dec, "loop1")
    
    wrap_target()
    wait(0,pin,0)        #wait for data ready, indicated by low level
    
    set(x, 23)           #generate 24 Pulses...
    label("loop2")
    nop()    .side(1)    [7]
    nop()    [1]
    nop()    .side(0)    [5]   
    in_(pins, 1)         #... to read read 24 bits 
    nop()    [1]
    jmp(x_dec, "loop2")
    nop()    .side(1)    [7]    #generate 1 more pulse to get to 25 pulses
    nop()    [1]
    nop()    .side(0)    [7]
    nop()    [1]
    push()               #write data to FIFO
    
    wrap()
    
sm = rp2.StateMachine(0, hx711, freq=10_000_000, sideset_base=Pin(16), in_base=Pin(17))

sm.active(1)

#Test Program
i2c=I2C(0,sda=Pin(4), scl=Pin(5), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
button = Pin(2, Pin.IN, Pin.PULL_DOWN)
CalAccumulate = 0
CalCounter = 0
CalOffset = 0
CalGain = 63272
rotary = Rotary(0,1,2)
val = 1
limit_out = Pin(8, Pin.OUT)
MaxMessage = "OVER LIMIT"

def button_handler(pin):
    button.irq(handler=None)
    global CalCounter
    global CalAccumulate
    global CalOffset
    CalCounter = 0
    CalAccumulate = 0
    CalOffset = 0
    button.irq(handler=button_handler)
    
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW and val < 40:
        val = val + 1
    elif change == Rotary.ROT_CCW and val > 1:
        val = val - 1

rotary.add_handler(rotary_changed)

while True:
    time.sleep(0.01)          #I'm looking for a better way than this
    Data=sm.get()              #read Data from FIFO
    if (Data > 8388608):
        Data = Data - 16777215
    if(CalCounter <= 9):
        CalAccumulate = Data + CalAccumulate
        CalCounter = CalCounter + 1
    elif(CalCounter == 10):
        CalOffset = CalAccumulate / 10
        CalCounter = 20
    elif(CalCounter == 20):
        Data = Data - CalOffset
    if Data/CalGain > -.1:
        Data = abs(Data)                #sets values above -0.1 as absolute to avoid showing -0.0
    if CalCounter != 20:
        oled.fill(0)
        oled.text(str("Zeroing..."), 0, 0)
    elif Data >= 0:
        oled.fill(0)
        oled.text(str("Force(lb):  " + '%.1f'%(Data/CalGain)), 0, 0)
        oled.text(str("Max: +/- " + str(val) + " lb"), 0, 16)
        if Data/CalGain >= val:
            oled.text(str("---" + MaxMessage + "---"), 0, 32)
            limit_out.value(1)
        else:
            limit_out.value(0)
    else:
        oled.fill(0)
        oled.text(str("Force(lb): " + '%.1f'%(Data/CalGain)), 0, 0)
        oled.text(str("Max: +/- " + str(val) + " lb"), 0, 16)
        if abs(Data/CalGain) >= val:
            oled.text(str("---" + MaxMessage + "---"), 0, 32)
            limit_out.value(1)
        else:
            limit_out.value(0)

    oled.show()