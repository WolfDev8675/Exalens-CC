#!usr/bin/python3

# IMPORTS 
from pydantic import BaseModel



class DataRequest(BaseModel):
    sensor_id: str
    start_time: str
    end_time: str

