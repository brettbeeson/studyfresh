#!/usr/bin/env python
#

from __future__ import print_function
import qwiic_ccs811
import time
import sys

def runExample():

	print("\nSparkFun CCS811 Sensor Basic Example \n")
	mySensor = qwiic_ccs811.QwiicCcs811()

	if mySensor.connected == False:
		print("The Qwiic CCS811 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySensor.begin()
	time.sleep(1)

	t=0
	while True:
		mySensor.set_environmental_data( 50, t )
		t += 2

		mySensor.read_algorithm_results()

		print("temp:\t%.3f" % t)
		print("CO2:\t%.3f" % mySensor.CO2)

		print("tVOC:\t%.3f\n" % mySensor.TVOC)	

		
		time.sleep(5)


if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)


