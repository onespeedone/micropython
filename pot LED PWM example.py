# example showing PWM to control brightness of LED
# POT reading is used to control PWM duty cycle
# JJM 29 March 2022

from machine import ADC, Pin, PWM
import time

adc = ADC(Pin(26))
pwm = PWM(Pin(14))
pwm.freq(5000)
led2 = PWM(Pin(16))
led2.freq(960)

while True:
    duty = adc.read_u16()
    flip = 65600 # variable that allows flipping of duty cycle for 2nd LED output
    pwm.duty_u16(duty) 
    led2.duty_u16(flip - duty)
    #print(adc.read_u16())
    

    

