#!usr/bin/python3

# IMPORTS
from databases.connectors import DBConnection
from logging import getLogger
from configs.generic_config import GenericConfig
from appconstants import sensors
from utils.utilities import str2dict
from datetime import datetime

log = getLogger("webapp|temperature-repo")

class TemperatureCollectionRepository:
    cache_obj: None 
    persist_obj: None
    collection_name = "temperature"


    def __init__(self) -> None:
        _configs = GenericConfig()
        log.info("Connecting TemperatureCollectionRepository .. ")
        cachedb_cfg = _configs.get_connection_details("cache")
        persistdb_cfg = _configs.get_connection_details("persist-store")
        persistdb_connstr = _configs.get_connection_string("persist-store")
        self.cache_obj = DBConnection().set_cache_configurations(**cachedb_cfg)
        local_persist_obj = DBConnection().set_persistdb_configurations(persistdb_connstr,persistdb_cfg["database"])
        self.persist_obj = local_persist_obj[self.collection_name]
        log.info("TemperatureCollectionRepository CONNECTED ..")
    
    def write_data_persistdb(self, writable):
        """ 
        Write Data into the Cache and Persistant DB 
            
        Parameters
        ------------------
        writable: <dict> of the data to be written to Database
        """
        try:
            self.persist_obj.insert_one(writable)
        except Exception as e:
            print(f"WRITE FAILED {e}")
            return 1
        return 0
    
    def write_data_cachedb(self, writable):
        """ 
        Write Data into the cache  

        Parameters
        ------------------
        key: <str> key of the string to which data is to be written into
        
        writable: <str> data to be written

        """
        try:
            self.cache_obj.rpush(sensors.TEMPERATURE_KEY,writable)
        except Exception as e:
            print(f"WRITE FAILED {e}")
            return 1
        return 0

    def find_data_cachedb_latest_n(self, key:str, n:int):
        """ Read Data from the Cache 
        for a key for the Latest 'n' items
        
        Parameters
        ------------------
        key: <str> sensor id

        n: <int> number of items from the latest 
        
        Returns 
        ----------
        List of a Dictionaries 

        """
        data_received=None  #Initialization
        try:
            data_received = self.cache_obj.lrange(key,n*-1, -1)
        except Exception as e:
            print(f"READ FAILED {e}")
            return 1
        data_list = [str2dict(entry.decode("utf-8")) for entry in data_received]
        return data_list
    
    def find_data_persistdb(self, sensor_id:str, start_time:datetime, end_time:datetime):
        """ Read Data from the PersistDB - MongoDB 
        for a sensor_id for a date-time range 
        
        Parameters 
        ------------------
        sensor_id: <str> sensor_id 
        start_time: <datetime> starting time data 
        end_time: <datetime> ending time data 

        Returns 
        ----------
        List of a Dictionaries 

        """
        # Filter conditions 
        filter={
                'sensor_id': sensor_id, 
                'timestamp': {
                    '$gte': start_time, 
                    '$lte': end_time
                }
            }
        data_received = None
        try:
            data_received=self.persist_obj.find(filter=filter)
        except Exception as e:
            print(f"READ FAILED {e}")
            return 1
        data_list = []
        for item in data_received:
            item.pop("_id")
            data_list.append(item)
        return data_list


    
