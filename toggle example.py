import time

led = 0
cycles = int(input("enternumberof cycles"))

def led_toggle():
    global led, cycles
    #led = not led
    led = (1,0)[led]
    cycles -= 1
    print(led)

    
while True:
    led_toggle()
    if cycles == 0:
        break
print("end")
quit()