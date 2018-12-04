#Create a function that will:
#Get the AM2302 readings
#Send them to a newly-made file
#Store them with the time

import Adafruit_DHT
import datetime
import logging
import time
import adafruit_sgp30
import board
import busio

logger = logging.getLogger("sc_fair")

def to_farnheit(temp_in_celcius):
    "This function converts a temperature in celcius to farnheit"
    x = open("dht_readings.log", "r")
    temp_in_farnheit = (temp_in_celcius * 9/5) + 32
    return temp_in_farnheit


def carbon_dioxide(out_file):
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

    # Create library object on our I2C port
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    print("SGP30 serial #", [hex(i) for i in sgp30.serial])

    sgp30.iaq_init()
    sgp30.set_iaq_baseline(0x8973, 0x8aae)

    elapsed_time = 0

    while True:
        now = datetime.datetime.now()
        with open(out_file, 'a') as fd:
            # fd.write("eCO2 = %d ppm, TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
            fd.write("%s, %d, %d " % (str(now), sgp30.eCO2, sgp30.TVOC))

        elapsed_time += 1
        if elapsed_time > 6:
            elapsed_time = 0
            fd = open(out_file, "a")
            # fd.write("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            #        % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
            fd.write("**** Baseline values: %s, 0x%x, 0x%x"
                % (str(now), sgp30.baseline_eCO2, sgp30.baseline_TVOC))
            fd.close()
        time.sleep(300)

def dht_readings(out_file):
    "This function is opening a new file and sending the readings from the AM2302 to the file."
    while True:
        current = datetime.datetime.now()
        sensormodel = Adafruit_DHT.AM2302
        sensorpin = 4
        humidity, temp_in_celcius = Adafruit_DHT.read_retry(sensormodel, sensorpin)
        temp_in_farnheit = to_farnheit(temp_in_celcius)

        with open(out_file, 'a') as f:
            f.write(str(current) + ", " + str(humidity) + ", " + str(temp_in_farnheit) + "\n")
        time.sleep(300)


if __name__ == '__main__':
    which_func = input("Which function would you like to call: 1) CO2, or 2) AM2302?  ")
    if which_func == "1":
        carbon_dioxide("carbon_dioxide.log")
    elif which_func == "2":
        dht_readings("dht_readings.log")
    else:
        print("Invalid selection. Please try again later.")
#    print("Starting readings of humidity and temperature")
#    dht_readings("dht_readings.log")
#    carbon_dioxide("carbon_dioxide.log")
