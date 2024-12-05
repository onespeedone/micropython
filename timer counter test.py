import time

travel = 80
pulse = 0

def limitswitchfwd():
    global travel, pulse
    while travel > 0:
        #print ("travel is:", travel)
        travel -= 1
        pulse = 0
        motor()
        print ("toggle is", pulse)
        print ("new travel is:", travel)
        pulse = 1
        motor()
        print ("new toggle is", pulse)
        #time.sleep(.000000001)
        
    else:
        print("Fwd Limit = FALSE")

def motor():
    global pulse, travel
    if pulse == 1:
        print("High pulse")
        True
    elif pulse == 0:
        print ("LOW pulse")
        False

        
limitswitchfwd()