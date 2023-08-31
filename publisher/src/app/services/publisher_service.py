#!usr/bin/python3

from paho.mqtt import client as mqtt

from configs.generic_config import GenericConfig

# def connect_mqtt():
#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to Broker")
#         else:
#             print("Failed to connect, return code %d\n", rc)

#     _config = GenericConfig()    # Pulling configs
#     client = mqtt.Client("PUB1")   # FIXED number for IDENTIFICATION 
#     client.on_connect = on_connect
#     client.connect(**_config.get_mqtt_config())
#     return client


def publish_data(topic,data):
    _config = GenericConfig()    # Pulling configs
    client = mqtt.Client("PUB1")   # FIXED number for IDENTIFICATION 
    # client.on_connect = on_connect
    client.connect(**_config.get_mqtt_config())
    client.loop_start()
    for item in data:
        client.publish(topic, str(item))
    client.loop_stop()
