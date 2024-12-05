# basic fo loop
# for x in range(20):
#     print (x)

# for loop with variable
# pulse = 20
# 
# for x in range(pulse):
#     print (x)

# for loop with variable that takes input
# pulse = int(input("enter number: "))
# 
# for x in range(pulse):
#     print (x)
    
# for loop with variable that takes input and time delay
# import time
# 
# pulse = int(input("enter number: "))
# 
# for x in range(pulse):
#     print (x)
#     time.sleep(1)
    
# for loop with variable that takes input and time delay and boolean toggle
import time

pulse = int(input("enter number: "))
toggle = False
for x in range(pulse):
    print (x)
    toggle = not toggle
    print (toggle)
    time.sleep(.1)
    
# for loop with variable that takes input and time delay and boolean toggle and possible linear move
# not quite figured out yet
# import time
# 
# pulse = int(input("enter number of inches: ")/.0002)
# toggle = 0
# for x in range(pulse):
#     print (x)
#     toggle = not toggle
#     print (toggle)
#     time.sleep(.1)

####################################
# pico program mimics cycle tester #
####################################

#from machine import Pin, PWM
#import time


# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
#led1 = Pin(14, Pin.OUT)
#led2 = Pin(16, Pin.OUT)
#pulses = 15
#toggle = True
#dwell = .4
#cycles = int(input("Enter number of cycles: "))
    
#def moveforward():
#    global toggle, pulses, led2, led1, dwell, cycles
#    if cycles > 0:
#        for x in range(pulses):
#            toggle = not toggle
#            led2.value(toggle)
#            time.sleep(dwell)
#        else:
#            led1.value(False)
#            led2.value(False)
#            dwell = .1
#            pulses = 25
#            cycles -= 1
#            print ("cycles remaining: ", cycles)
#            moveback()
#    else:
#        print("end of program")
            
#def moveback():
#    global toggle, pulses, led2, led1, dwell
#    for x in range(pulses):
#        toggle = not toggle
#        led1.value(toggle)
#        time.sleep(dwell)
#    else:
#        led1.value(False)
#        led2.value(False)
#        pulses = 5
#        dwell = .05
#        moveforward()
        
#moveforward()

    