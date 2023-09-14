#!usr/bin/python3

from logging import getLogger
from appconstants import sensors
from configs.generic_config import GenericConfig
import paho.mqtt.client as mqtt
from events.event_router import connection_event,message_event

# log=getLogger("subscriber|main")


if __name__ == "__main__":
    """ Subscriber service main """
    print(" STARTING SUBSCRIBER SERVICE ")
    client = mqtt.Client("SUB-SVC")     # SETTING DEFAULTS FOR RECOGNITION 
    client.on_connect = connection_event
    client.on_message = message_event
    _config = GenericConfig()
    print(f"Attempting Connection attempt to {client}")
    client.connect(keepalive=60,**_config.get_mqtt_config())
    client.loop_forever()

