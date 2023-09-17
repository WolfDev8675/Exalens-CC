#!usr/bin/python3
""" Function to schedule jobs """

# IMPORTS
from logging import getLogger
from paho.mqtt.client import Client
from services.temperature_service import store_temperature_reading
from services.humidity_service import store_humidity_reading
from appconstants import sensors

log = getLogger("subscriber|routes")


def connection_event(client: Client, userdata, flags, rc):
    """Operations to execute on connection event"""
    log.info(f"Connected {client} with result code {str(rc)}")
    client.subscribe([(sensors.TEMPERATURE_TOPIC, 0), (sensors.HUMIDITY_TOPIC, 0)])


def message_event(client: Client, userdata, msg):
    log.info(f"Received on Topic {msg.topic}  :: {str(msg.payload.decode())} ")
    if msg.topic == sensors.TEMPERATURE_TOPIC:
        store_temperature_reading(msg.payload.decode())
    elif msg.topic == sensors.HUMIDITY_TOPIC:
        store_humidity_reading(msg.payload.decode())
    else:
        log.error(" TOPIC NOT A REGISTERED APP-CONSTANT ")
