# studyfresh

The Citizen Science project for Air Quality.

## Comparing CO2 sensors


The following cheap (<$100) sensors were tested: CCS811, MH-Z19B. They were tested against two assumed-good industrial Extech CO2 and temperature units. The results in charts are below, with details following them. The charts cover 4 days in a small room with intermittent occupation and ventilation.

![CO2](https://github.com/brettbeeson/studyfresh/blob/main/CO2.png)
![Temperature](https://github.com/brettbeeson/studyfresh/blob/main/temperature.png)


## CCS 811 CO2
### Background
- Resources at  [Adafruit](https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor)
- Library used was [Python API](https://qwiic-ccs811-py.readthedocs.io/en/latest/apiref.html)
- There is reportedly (SparkFun forum) inaccurate and bme280 misread due to heating on the combo board.
- [Comparative review](https://www.jaredwolff.com/finding-the-best-tvoc-sensor-ccs811-vs-bme680-vs-sgp30/)
- [The BME280](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/9/BST-BME280_DS001-10.pdf) is used on the combo board to compensate for temperature and humidity.
- 48 burnin required, then 20 minutes for new mode start, before good readings availabel
### Setup and results
- The Sparkfun "Environmental Combo" board was tested over a few days using "Mode 1" (continuous heating) and "Mode 2" (pulse heating)
- Connected to I2C
- CO2 results were inaccurate. See temperature graph below (blue dots). The sensor is sensitive to CO2, but results are wild.
- The BME280 is affected by the CCS811 heating in MOde 1. On the temperature graph we see before 12:00 (Mode 1) the BME280 reads 1K high. After 12:00 (Mode 2) it agrees with the nearby MH-Z19B sensor.

## MH-Z19B
### Background
- Used the [Python library MZ-Z19](https://github.com/UedaTakeyuki/mh-z19) which will correctly setup uart (manual method is below). Follow instructions on library.
### Setup and results
- Connected to UART 
- Good results (see temperature and CO2 graphs) compared to the 'assumed good' Extech sensors.
- Low range sensitivity (400-450ppm) is poor compared to the Extech, but 450-1000ppm is very close
- Temperature sensor is 2K above the reference - perhaps some self heating?
- Occasional read error - so this repo's software includes some retry functionality

### Background: Manual setup of UART On Raspi 3B
- [Setup uart](https://www.raspberrypi.org/documentation/configuration/uart.md) : note it varies by Raspi Model
- On Rpi 3B
- - UART0 is secondary (used for bluetooth). On /dev/serial1 (aka /dev/ttyAMA0)
-- UART1 is primary ("miniUART") and is *disabled by default*. On /dev/serial0 (aka /dev/ttyS0)
```
# /boot/config.txt
enable_uart=1
```
use ```raspi-config``` to disable use of primary uart by the login shell

## Comparing Temperature and Humidity Sensors

No work done here, just some references.
[Selection Guide](https://www.dfrobot.com/blog-695.html) compares BME280, LM35, DS18B20, SHT71
[Humidty](https://www.kandrsmith.org/RJS/Misc/Hygrometers/calib_many.html#commentary)  BME280 is best.
[Humidity and Temperature Test](https://www.youtube.com/watch?v=ynNeiFEJnrA) BME280 (good), HDC1080 (better)
### Cheap options $5-$10
- BME280 is good arounder. Possible self-heating. Good RH.
- HDC1080 is slightly better.
### Expensive options (Sensirion) $50-$100
- SHT71 is much more expensive and out of date. 
- [SHT85] might be good - probably best for long term. [https://www.sensirion.com/en/environmental-sensors/humidity-sensors/sht85-pin-type-humidity-sensor-enabling-easy-replaceability/]
- The [SCD30](https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/) does temperature, humidity and CO2. Untested but looks good.
