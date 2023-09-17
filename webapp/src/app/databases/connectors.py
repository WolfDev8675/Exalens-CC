#!usr/bin/python3

# IMPORTS
from logging import getLogger
from redis import Redis
from pymongo import MongoClient
from pymongo.database import Database


log = getLogger("webapp|datastore-connect")


class DBConnection:
    cachedb: Redis
    persistdb: Database

    def set_cache_configurations(self, host, port, database, password, **kwargs):
        print("CONNECTING TO:: REDIS - CACHE ")
        try:
            self.cachedb = Redis(host=host, port=port, db=database, password=password)
        except:
            print("FATAL ERROR::: COULD NOT CONNECT TO REDIS CACHE ")
        # SUCCESSFUL CONNECTION
        print(" SUCCESSFULLY CONNECTED TO REDIS ")
        return self.cachedb

    def set_persistdb_configurations(self, connection_string, database, **kwargs):
        print("CONNECTING TO:: MONGODB ")
        try:
            persistdb = MongoClient(connection_string)
        except:
            print("FATAL ERROR::: COULD NOT CONNECT TO MONGODB ")
        # SUCCESSFUL CONNECTION
        print(" SUCCESSFULLY CONNECTED TO MONGODB ")
        self.persistdb = persistdb[database]
        return self.persistdb
