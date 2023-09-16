#!usr/bin/python3

#IMPORTS
from logging import getLogger
from fastapi import status
from databases.repositories.humid_sens_repo import HumidityCollectionRepository
from databases.repositories.temp_sens_repo import TemperatureCollectionRepository
from payloads.responses.sensor_data_responses import Errors, SensorDataResponse
from utils.utilities import iso8601_format
from datetime import datetime

log = getLogger("sensor-data|service|webapp")



class SensorDataService():
    # Repositories 
    _temp_repo: TemperatureCollectionRepository
    _humid_repo: HumidityCollectionRepository

    def __init__(self):
        self._temp_repo = TemperatureCollectionRepository()
        self._humid_repo = HumidityCollectionRepository()

    def get_latest_sensor_data(self, sensor_id: str):
        """ Return with the latest 10 data from the cache """
        sensor_data = None
        if "Temp" in sensor_id: 
            # Sensor Type : Temperature 
            sensor_data = self._temp_repo.find_data_cachedb_latest_n(sensor_id,10)
            log.info(" Returning data for query")
        elif "Humid" in sensor_id:
            # Sensor Type : Humidity 
            sensor_data = self._humid_repo.find_data_cachedb_latest_n(sensor_id,10)
            log.info(" Returning data for query")
        else:
            log.error(" Un-Registered Sensor-ID in request ")
            err = Errors
            err.process="Get Latest Sensor Data "
            err.path="/api/sensor/latest"
            err.httpCode=status.HTTP_404_NOT_FOUND
            err.reasons=" Un-Registered Sensor-ID in request "
            return err
        
        # Returns 
        ret = SensorDataResponse
        ret.data = sensor_data
        return ret

    def get_timed_sensor_data(self, sensor_id: str, start_time: str, end_time: str):
        """ Return with the data of sensor defined in the time range """           
        sensor_data = None
        start = datetime.strptime(start_time,iso8601_format)
        end = datetime.strptime(end_time,iso8601_format)
        if "Temp" in sensor_id: 
            # Sensor Type : Temperature 
            log.info("Temperature Sensor ")
            sensor_data = self._temp_repo.find_data_persistdb(sensor_id=sensor_id,start_time=start,end_time=end)
            log.info(" Returning data for query")
        elif "Humid" in sensor_id:
            # Sensor Type : Humidity 
            log.info("Humidity Sensor ")
            sensor_data = self._humid_repo.find_data_persistdb(sensor_id=sensor_id,start_time=start,end_time=end)
            log.info(" Returning data for query")
        else:
            log.error(" Un-Registered Sensor-ID in request ")
            err = Errors
            err.process="Get Sensor Data -Over Time Range "
            err.path="/api/sensor/data"
            err.httpCode=status.HTTP_404_NOT_FOUND
            err.reasons=" Un-Registered Sensor-ID in request "
            return err
        
        # Returns 
        ret = SensorDataResponse
        ret.data = sensor_data
        return ret
