import machine
sda = machine.Pin(20)
scl = machine.Pin(21)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

address = i2c.scan()
print("i2c address "  , address)
print("i2c address "  ,hex(address[0]).upper())