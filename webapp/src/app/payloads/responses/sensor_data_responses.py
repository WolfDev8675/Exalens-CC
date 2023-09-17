#!usr/bin/python3

# IMPORTS
from pydantic import BaseModel


class SensorDataResponse(BaseModel):
    data: list[object]


class Errors(BaseModel):
    process: str
    path: str
    httpCode: int
    reasons: str
