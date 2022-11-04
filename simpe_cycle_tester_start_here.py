from machine import Pin, PWM
import time


# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led1 = Pin(14, Pin.OUT)
led2 = Pin(16, Pin.OUT)
pulses = 15
toggle = True
dwell = .4
cycles = int(input("Enter number of cycles: "))
    
def moveforward():
    global toggle, pulses, led2, led1, dwell, cycles
    if cycles > 0:
        for x in range(pulses):
            toggle = not toggle
            led2.value(toggle)
            time.sleep(dwell)
        else:
            led1.value(False)
            led2.value(False)
            dwell = .1
            pulses = 25
            cycles -= 1
            print ("cycles remaining: ", cycles)
            moveback()
    else:
        print("end of program")
            
def moveback():
    global toggle, pulses, led2, led1, dwell
    for x in range(pulses):
        toggle = not toggle
        led1.value(toggle)
        time.sleep(dwell)
    else:
        led1.value(False)
        led2.value(False)
        pulses = 5
        dwell = .05
        moveforward()
        
moveforward()