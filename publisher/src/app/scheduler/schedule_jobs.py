#!usr/bin/python3
""" Function to schedule jobs """

# IMPORTS
from appconstants import sensors
from services.temp_reader_service import get_temperature_data
from services.humid_reader_service import get_humidity_data
from services.publisher_service import publish_data

def read_temperature():
    """ READ DATA FROM SENSOR - TEMPERATURE"""
    # get data
    recieved_data = get_temperature_data()
    # publish data
    publish_data(sensors.TEMPERATURE_TOPIC,recieved_data)
    print("Sent Temperature Data")
    

def read_humidity():
    """ READ DATA FROM SENSOR - HUMIDITY"""
    # get data
    recieved_data = get_humidity_data()
    # publish data
    publish_data(sensors.HUMIDITY_TOPIC,recieved_data)
    print("Sent Humidity Data")

def run_jobs():
    read_temperature()
    read_humidity()

