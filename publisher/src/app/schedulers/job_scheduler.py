#!usr/bin/python3
""" Function to schedule jobs """

# IMPORTS
from appconstants import sensors
from services.temp_reader_service import get_temperature_data
from services.humid_reader_service import get_humidity_data
from services.publisher_service import publish_data
from fastapi import APIRouter
from apscheduler.schedulers.background import BackgroundScheduler
from logging import getLogger
import atexit

log=getLogger("publisher|scheduler")
scheduled_jobs=BackgroundScheduler()
api_router = APIRouter()

def read_temperature():
    """ READ DATA FROM SENSOR - TEMPERATURE"""
    # get data
    recieved_data = get_temperature_data()
    # publish data
    publish_data(sensors.TEMPERATURE_TOPIC,recieved_data)
    log.info("Sent Temperature Data")
    

def read_humidity():
    """ READ DATA FROM SENSOR - HUMIDITY"""
    # get data
    recieved_data = get_humidity_data()
    # publish data
    publish_data(sensors.HUMIDITY_TOPIC,recieved_data)
    log.info("Sent Humidity Data")

def read_sensors():
    """ TRIGGER BOTH READ FUNCTIONS """
    read_temperature()
    read_humidity()


@api_router.on_event("startup")
def run_jobs():
    log.info("Setting up Scheduler jobs ")
    scheduled_jobs.add_job(read_sensors, trigger= "cron", second = "*/5")
    scheduled_jobs.start()

# @api_router.
# def error_handler():
#     log.error(" FAILED OPERATIONS ")
#     scheduled_jobs.remove_all_jobs()

atexit.register(lambda: scheduled_jobs.remove_all_jobs)