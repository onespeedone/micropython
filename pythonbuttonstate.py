# March 5th 2022 Jordan Missiaen
# sample setup for cycle tester that runs a motor and hits
# a limit switch before reversing and running into another
# limit switch

import time
limitswitch = True


def swstate():
    global limitswitch, counter
    if limitswitch == True:
        limitswitch = False
    else:
        limitswitch = True
    counter -= 1

def motor():
    global counter, limitswitch
    while counter > 0 and limitswitch == False:
        print ("Motor", counter)
        counter -= 1
        time.sleep(.25)
        limitswitch = True

# Input to ask how many cycles to do
print("how many cycles?")
counter = int(input())

while counter > 0:
    
    print ("switch 1 state", limitswitch)
    time.sleep(.01)
    motor()
    swstate()
    print("cycles remaining",counter)


