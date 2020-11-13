#!/usr/bin/env python

import smbus2
import bme280
import datetime 
import qwiic_ccs811
import mh_z19
import time
import sys
from time import sleep
import argparse
from datetime import timedelta
from datetime import datetime as dt


# constants
i2c_port = 1
bme_i2c_address = 0x77

# globals
i2c_bus = smbus2.SMBus(i2c_port)    
ccs811 = None
bme280_cal = None
         


def create_ccs811(verbose = False):
    """ Return a ccs811 object to access this sensor. Raises an error if it cannot connect. """
    new_ccs811 = qwiic_ccs811.QwiicCcs811() #i2c_driver = i2c_bus)
    new_ccs811.begin()
            
    if not new_ccs811.connected:
        raise Exception(f"Cannot connect to ccs811 on i2c_bus {i2c_bus}")
    # Mode 1 = read every 1s, constant heat (more accurate?)
    # Mode 2 = every 10s, pulse heat 
    # Mode 3 = every 60s, pulse heat
    #new_ccs811.set_drive_mode  (1)
    new_ccs811.set_drive_mode  (2)
    return new_ccs811
    

def sample_bme280():
    """ Read the current temp and rh from the bme280 """
    sample = bme280.sample(i2c_bus, bme_i2c_address, bme280_cal)
    return  sample.humidity, sample.temperature 
    
    
def sample_ccs811(rh = 50, temp = 25):
    """ Read the current co2 and tvoc from the ccs811, optionally temperature/rh compensating """
    ccs811.set_environmental_data(rh, temp)
    ccs811.read_algorithm_results()
    
    return ccs811.CO2, ccs811.TVOC

def sample_mh_z19():
    sample = mh_z19.read_all()
    return sample['co2'], sample['temperature']

if __name__ == '__main__':
    
    try:
        # Command line arguments
        parser = argparse.ArgumentParser(description="Read the CCS881 CO2, temperature compensating with a BME280")
        parser.add_argument("-v","--verbose", action='store_true', help="Display verbose output")
        parser.add_argument("-s", type=int,default=0, help="Seconds between readings - implies continuous running")
        parser.add_argument("-t", action='store_true', help="Print title row")
        args = parser.parse_args()
        
        if args.t:
            print("datetime, co2_ccs811, co2_mhz, rh_bme280, temp_bme280, temp_mhz")
            sys.exit(0)
        
        # setup devices
        i2c_bus = smbus2.SMBus(i2c_port)    
        ccs811 = create_ccs811(i2c_bus)
        bme280_cal = bme280.load_calibration_params(i2c_bus,bme_i2c_address)
        mh_z19.detection_range_2000()
            
        if args.verbose:
            print(f"ccs811 baseline: {ccs811.get_baseline()}")
            print(f"ccs811 resistance: {ccs811.get_resistance()}")
            print(f"ccs811 reference resistance: {ccs811.referance_resistance}")
            print(f"ccs811 current resistance: {ccs811.resistance}")
        
        sleep(5)  # allow sensors to warmup
    
        sample_time = dt.now()
        n_errors = 0
        
        while True:
            try:
                # wait until next sample time                
                sample_time = sample_time  + timedelta(seconds=args.s)
                sleep_seconds = (sample_time - dt.now()).total_seconds()
                if args.verbose:
                    print(f"sleeping for {sleep_seconds:.1f}s")
                sleep(sleep_seconds)
                # sample sensors
                rh, temp = sample_bme280()
                co2, tvoc = sample_ccs811(rh, temp)
                co2_mhz, temp_mhz = sample_mh_z19()
                # output
                print(f"{sample_time.replace(microsecond=0).isoformat()},{co2},{co2_mhz},{temp:.1f},{temp_mhz:.1f}", flush=True)
                # exit if in single-reading mode
                if args.s == 0:
                    sys.exit(0)

                n_errors = 0
            except Exception as ex:
                n_errors += 1
                if n_errors > 10:
                    raise
                else:
                    # skip this reading and retry
                    print (f"{ex}. Retrying {n_errors}/10.", file=sys.stderr)          
        
    except KeyboardInterrupt as ex:
        print (ex)
        sys.exit(0)
        
    

