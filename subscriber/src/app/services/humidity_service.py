from databases.repositories.humid_sens_repo import HumidityCollectionRepository
from logging import getLogger
from utils.utilities import str2dict

log = getLogger("subscriber|humidity-svc")


def store_humidity_reading(message):
    """Store Relevant Humidity to the Respective Database"""
    db_obj = HumidityCollectionRepository()
    print(f" Service (H): {message}")
    write_msg = str2dict(message)
    db_obj.write_data_persistdb(write_msg)
    db_obj.write_data_cachedb(write_msg["sensor_id"], message)
    print(" Data written ")
