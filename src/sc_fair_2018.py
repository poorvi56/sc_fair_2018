#Create a function that will:
#Get the AM2302 readings
#Send them to a newly-made file
#Store them with the time

import Adafruit_DHT
import datetime
import logging
import time

logger = logging.getLogger("sc_fair")

def to_farnheit(temp_in_celcius):
    "This function converts a temperature in celcius to farnheit"
#    return 0.0
    x = open("dht_readings.log", "r")
    temp_in_farnheit = (temp_in_celcius * 9/5) + 32

def dht_readings(out_file):
    "This function is opening a new file and sending the readings from the AM2302 to the file."
    f = open(out_file, "w+")

    while True:
        current = datetime.datetime.now()
        sensormodel = Adafruit_DHT.AM2302
        sensorpin = 4
        humidity, temp_in_celcius = Adafruit_DHT.read_retry(sensormodel, sensorpin)
        temp_in_farnheit = to_farnheit(temp_in_celcius)
        f.write("humidity, temp_in_farnheit, current")
        logger.info("Collected sample at %s", str(current))
        time.sleep(300)
        # TODO Sleep!!!

    f.close()

if __name__ == '__main__':
    logger.info("Starting readings of humidity and temperature")
    dht_readings("dht_readings.log")
