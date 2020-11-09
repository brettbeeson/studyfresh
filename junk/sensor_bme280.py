import smbus2
import bme280
from time import sleep

port = 1
address = 0x77
bus = smbus2.SMBus(port)

cal = bme280.load_calibration_params(bus,address)


while True:

    data = bme280.sample(bus, address, cal)
    print(data)
    sleep (1)
