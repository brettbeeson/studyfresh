# studyfresh

Repo for code for citiz science project

## CCS 811 CO2
- Good info at (Adafruit) [https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor]
- (Python API)[https://qwiic-ccs811-py.readthedocs.io/en/latest/apiref.html]
- reportedly (SparkFun) inaccurate due to heating on the combo board
- (Comparative review here) [https://www.jaredwolff.com/finding-the-best-tvoc-sensor-ccs811-vs-bme680-vs-sgp30/]

- 48 burnin required, then 20 minutes for new mode start, before good readings availabel


## BME280

- (Datasheet)[https://cdn.sparkfun.com/assets/learn_tutorials/4/1/9/BST-BME280_DS001-10.pdf]

### UART On Raspi 3B
- [https://www.raspberrypi.org/documentation/configuration/uart.md]
- 3.3v only
- UART0 is secondary (used for bluetooth). On /dev/serial1 (aka /dev/ttyAMA0)
- UART1 is primary ("miniUART") and is *disabled by default*. On /dev/serial0 (aka /dev/ttyS0)
```
# /boot/config.txt
enable_uart=1
```
use ```raspi-config``` to disable use of primary uart by the login shell
