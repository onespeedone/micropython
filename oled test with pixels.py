# SPDX-FileCopyrightText: Tony DiCola
# SPDX-License-Identifier: CC0-1.0

# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.

# Import all board pins.
import time
import board
import busio
import adafruit_bitmap_font


SDA = board.GP0
SCL = board.GP1

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.

i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
#display.show()

# Set a pixel in the origin 0,0 position.
#display.pixel(0, 2, 1)
#display.fill_rect(9,9,25,25,1)
#display.rect(35,9,25,25,1)
#display.fill_rect(61,9,25,25,1)
#display.hline(8,8,120,1)
#display.hline(8,30,120,1)
display.text("Hi Werld", 5, 10, 1 )
#display.print("your mom")
# Set a pixel in the middle 64, 16 position.
#display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
#display.pixel(127, 31, 1)
display.show()
