#!usr/bin/python3

from paho.mqtt import client as mqtt

from configs.generic_config import GenericConfig


def publish_data(topic: str, data: list):
    """
    PUBLISH 'data' to the 'topic'

    Args:
        data: list in bulk for the data to be published
        topic: string topic to which data is to be published
    """
    _config = GenericConfig()  # Pulling configs
    client = mqtt.Client("PUB-SVC")  # FIXED number for IDENTIFICATION
    client.connect(**_config.get_mqtt_config())
    client.loop_start()
    for item in data:
        client.publish(topic, str(item))
    client.loop_stop()
