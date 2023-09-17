#!usr/bin/python3

# Imports
from datetime import datetime
from utils.utility import get_random_temperature
from appconstants import sensors


def get_temperature_data():
    """READS TEMPERATURE DATA OF ALL SENSORS"""

    response_list = []

    payload = {}  # SET
    payload["sensor_id"] = sensors.SENSOR_TEMP_ROOM1
    payload["timestamp"] = datetime.now().isoformat()
    payload["value"] = get_random_temperature()
    response_list.append(payload)

    payload = {}  # RESET
    payload["sensor_id"] = sensors.SENSOR_TEMP_ROOM2
    payload["timestamp"] = datetime.now().isoformat()
    payload["value"] = get_random_temperature()
    response_list.append(payload)

    payload = {}  # RESET
    payload["sensor_id"] = sensors.SENSOR_TEMP_ROOM3
    payload["timestamp"] = datetime.now().isoformat()
    payload["value"] = get_random_temperature()
    response_list.append(payload)

    payload = {}  # RESET
    payload["sensor_id"] = sensors.SENSOR_TEMP_ROOM4
    payload["timestamp"] = datetime.now().isoformat()
    payload["value"] = get_random_temperature()
    response_list.append(payload)

    return response_list
