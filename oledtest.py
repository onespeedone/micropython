from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128,32,i2c)

oled.fill(0)
oled.text("Hello",0,0)
oled.show()
