#!/usr/bin/env python

import datetime 
import qwiic_ccs811
import time
import sys

def runExample():

	mySensor = qwiic_ccs811.QwiicCcs811()

	if mySensor.connected == False:
		print("The Qwiic CCS811 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySensor.begin()
	mySensor.read_algorithm_results()
	time.sleep(3)
	mySensor.read_algorithm_results()
	time.sleep(3)
	mySensor.read_algorithm_results()
	print(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),end=",")
	print("%.3f" % mySensor.CO2,end = ",")
	print("%.3f" % mySensor.TVOC)	


if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)


