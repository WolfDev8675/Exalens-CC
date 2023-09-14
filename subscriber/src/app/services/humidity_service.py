
from databases.repositories.humid_sens_repo import HumidityCollectionRepository
from logging import getLogger
from utils.utilities import str2dict

log = getLogger("subscriber|temperature-svc")

def store_humidity_reading(message):
    """ Store Relevant Humidity to the Respective Database"""
    db_obj = HumidityCollectionRepository()
    print(f" Service (H): {message}")
    db_obj.write_data_persistdb(str2dict(message))
    db_obj.write_data_cachedb(message)
    print(" Data written ");

    