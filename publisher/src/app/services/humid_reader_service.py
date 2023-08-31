#!usr/bin/python3
""" Operator for getting Humidity Data """

# Imports
from datetime import datetime
from utils.utility import get_random_humidity

from appconstants import sensors


def get_humidity_data():
    """ READS HUMIDITY DATA OF ALL SENSORS """
    
    response_list = []

    payload = {}   # SET
    payload["sensor_id"]=sensors.SENSOR_HUMID_ROOM1
    payload["timestamp"]=datetime.now().isoformat()
    payload["value"]= get_random_humidity()
    response_list.append(payload)

    payload = {}   # RESET
    payload["sensor_id"]=sensors.SENSOR_HUMID_ROOM2
    payload["timestamp"]=datetime.now().isoformat()
    payload["value"]= get_random_humidity()
    response_list.append(payload)

    payload = {}   # RESET
    payload["sensor_id"]=sensors.SENSOR_HUMID_ROOM3
    payload["timestamp"]=datetime.now().isoformat()
    payload["value"]= get_random_humidity()
    response_list.append(payload)

    payload = {}   # RESET
    payload["sensor_id"]=sensors.SENSOR_HUMID_ROOM4
    payload["timestamp"]=datetime.now().isoformat()
    payload["value"]= get_random_humidity()
    response_list.append(payload)

    return response_list
