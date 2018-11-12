#Create a function that will:
#Get the AM2302 readings
#Send them to a newly-made file
#Store them with the time

import Adafruit_DHT
import datetime
import logging
import time

logger = logging.getLogger("sc_fair")

def dht_readings():
    "This function is opening a new file and sending the readings from the AM2302 to the file."
    f = open("DHTreading_file", "w+")

    while True:
        current = datetime.datetime.now()
        sensormodel = Adafruit_DHT.AM2302
        sensorpin = 4
        humidity, temperature = Adafruit_DHT.read_retry(sensormodel, sensorpin)
        f.write(humidity, temperature, current)
        logger.info("Collected sample at %s", str(current))
        time.sleep(300)
        # TODO Sleep!!!

    f.close()

if __name__ == '__main__':
    logger.info("Starting readings of humidity and temperature")
    dht_readings()
