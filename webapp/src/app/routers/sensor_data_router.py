#!usr/bin/python3

# IMPORTS
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logging import getLogger
from payloads.responses.sensor_data_responses import SensorDataResponse, Errors
from payloads.requests.sensor_data_requests import DataRequest
from services.sensor_data_service import SensorDataService

# Base Definitions
log = getLogger("webapp|router")
route = APIRouter()

# Services
sensor_service = SensorDataService()


# PATH DEFINITIONS
@route.get(
    path="/api/sensor/latest",
    tags=["Latest Data"],
    summary="Obtain the Latest readings(10) of a sensor identified by it's unique ID ",
    status_code=200,
    response_model=SensorDataResponse,
)
async def get_latest_sensor_data(sensor_id: str) -> SensorDataResponse:
    """Router function to respond back with the latest 10 elements of a certain data"""
    if sensor_id == None or len(sensor_id.strip()) < 1:
        # Error on the ID
        log.error("Sensor_ID can't be empty")
        err = Errors
        err.process = "Get Latest Sensor Data "
        err.path = "/api/sensor/latest"
        err.httpCode = 422
        err.reasons = "Sensor_ID can't be empty"
        return JSONResponse(
            status_code=err.httpCode,
            content=jsonable_encoder(Errors(**err.__dict__).dict()),
        )
    else:
        result = sensor_service.get_latest_sensor_data(sensor_id=sensor_id)

        try:
            if result.data == None:
                # Empty Data Returned
                log.info("NO RECORDS FOUND")
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content=jsonable_encoder(
                        SensorDataResponse(**result.__dict__).dict()
                    ),
                )
            else:
                log.info(" DATA RETURNED FROM CACHE ")
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content=jsonable_encoder(
                        SensorDataResponse(**result.__dict__).dict()
                    ),
                )
        except:
            log.error("Service Returned ERROR ")
            # returned an error from Service
            return JSONResponse(
                status_code=result.httpCode,
                content=jsonable_encoder(Errors(**result.__dict__).dict()),
            )


@route.post(
    path="/api/sensor/data",
    tags=["Timed Data"],
    summary="Obtain the data of a sensor over a certain time range",
    status_code=200,
    response_model=SensorDataResponse,
)
async def get_sensor_data(request: DataRequest) -> SensorDataResponse:
    """Router function to respond back with data over some time range"""
    if request.sensor_id == None or len(request.sensor_id.strip()) < 1:
        # Error on the ID
        log.error("Sensor_ID can't be empty")
        err = Errors
        err.process = "Get Latest Sensor Data "
        err.path = "/api/sensor/latest"
        err.httpCode = 422
        err.reasons = "Sensor_ID can't be empty"
        return JSONResponse(
            status_code=err.httpCode,
            content=jsonable_encoder(Errors(**err.__dict__).dict()),
        )
    else:
        result = sensor_service.get_timed_sensor_data(
            sensor_id=request.sensor_id,
            start_time=request.start_time,
            end_time=request.end_time,
        )

        try:
            if type(result.data) == type(None):
                # Empty Data Returned
                log.info("NO RECORDS FOUND")
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content=jsonable_encoder(
                        SensorDataResponse(**result.__dict__).dict()
                    ),
                )
            else:
                log.info(" DATA RETURNED FROM DATABASE ")
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content=jsonable_encoder(
                        SensorDataResponse(**result.__dict__).dict()
                    ),
                )
        except:
            log.error("Service Returned ERROR ")
            # returned an error from Service
            return JSONResponse(
                status_code=result.httpCode,
                content=jsonable_encoder(Errors(**result.__dict__).dict()),
            )
