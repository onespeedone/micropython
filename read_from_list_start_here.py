import random
from time import sleep
from machine import Pin

button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)

file = open('file.txt')
content = file.readlines()

  
def randy2():
    randsom = random.randrange(0,24)
    print(content[randsom])
    
while True:
    if button1.value()== True:
        randy2()
        sleep(1)
    else:
        print("no button")