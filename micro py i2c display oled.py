import machine
import utime

sda = machine.Pin(0)
scl = machine.Pin(1)

timeout = 10 #timeout in seconds
timeout_start = utime.sleep(timeout)

i2c = machine.I2C(0, sda = sda, scl = scl, freq = 400000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

while True:
    oled.text("Welcome to the", 0, 0)
    oled.text("pi pico", 0, 10)
    oled.text("display demo", 0, 20)
    oled.show()
    utime.sleep(1)

    oled.fill(1)
    oled.show()
    utime.sleep(1)
    oled.fill(0)
    oled.show()

    oled.fill(0)
    oled.fill_rect(0, 0, 32, 32, 1)
    oled.fill_rect(2, 2, 28, 28, 0)
    oled.vline(9, 8, 22, 1)
    oled.vline(16, 2, 22, 1)
    oled.vline(23, 8, 22, 1)
    oled.fill_rect(26, 24, 2, 4, 1)
    oled.text('MicroPython', 40, 0, 1)
    oled.text('SSD1306', 40, 12, 1)
    oled.text('OLED 128x64', 40, 24, 1)
    oled.show()
    utime.sleep(1)

    oled.fill(0)
    oled.show()
    utime.sleep(1)

    while True:
    #while utime.sleep(timeout) < timeout_start + timeout:
        oled.text("Hello world", 0, 0)
        for i in range (0, 164):
            oled.scroll(1,0)
            oled.show()
            utime.sleep(0.01)
                #utime.sleep(1)
utime.sleep(4)

