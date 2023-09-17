#!usr/bin/python3

# IMPORTS
from databases.connectors import DBConnection
from logging import getLogger
from configs.generic_config import GenericConfig
from appconstants import sensors


log = getLogger("subscriber|temperature-repo")


class TemperatureCollectionRepository:
    cache_obj: None
    persist_obj: None
    collection_name = "temperature"

    def __init__(self) -> None:
        _configs = GenericConfig()
        cachedb_cfg = _configs.get_connection_details("cache")
        persistdb_cfg = _configs.get_connection_details("persist-store")
        persistdb_connstr = _configs.get_connection_string("persist-store")
        self.cache_obj = DBConnection().set_cache_configurations(**cachedb_cfg)
        local_persist_obj = DBConnection().set_persistdb_configurations(
            persistdb_connstr, persistdb_cfg["database"]
        )
        self.persist_obj = local_persist_obj[self.collection_name]

    def write_data_persistdb(self, writable):
        """Write Data into the Cache and Persistant DB
        :params writable: list or dict
        """
        try:
            self.persist_obj.insert_one(writable)
        except Exception as e:
            print(f"WRITE FAILED {e}")
            return 1
        return 0

    def write_data_cachedb(self, key, writable):
        """Write Data into the cache"""
        try:
            self.cache_obj.rpush(key, writable)
        except Exception as e:
            print(f"WRITE FAILED {e}")
            return 1
        return 0
