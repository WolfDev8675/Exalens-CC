
from databases.repositories.temp_sens_repo import TemperatureCollectionRepository
from logging import getLogger
from utils.utilities import str2dict

log = getLogger("subscriber|temperature-svc")


def store_temperature_reading(message):
    """ Store Relevant Temperature to the Respective Database"""
    db_obj = TemperatureCollectionRepository()
    print(f" Service (T): {message}")
    write_msg = str2dict(message)
    db_obj.write_data_persistdb(write_msg)
    db_obj.write_data_cachedb(write_msg["sensor_id"], message)
    print(" Data written ");
    
