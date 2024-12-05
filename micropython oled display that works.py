import machine
import utime

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = machine.I2C(0, sda = sda, scl = scl, freq = 400000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

#print(i2c.scan())

# oled.text("Welcome to the", 0, 0)
# oled.text("pi pico", 0, 10)
# oled.text("display demo", 0, 20)
# oled.show()
# utime.sleep(4)

# oled.fill(1)
# oled.show()
# utime.sleep(2)
# oled.fill(0)
# oled.show()

while True:
    oled.text("Hello world", 0, 0)
    for i in range (0, 164):
        oled.scroll(1,0)
        oled.show()
        utime.sleep(0.1)
