#!usr/bin/python3

from configs.server_config import Servlet
from fastapi import FastAPI
from logging import getLogger
from routers import sensor_data_router

log = getLogger("webapp|main")


class WebApplication:
    app: FastAPI

    def __init__(self) -> None:
        self.app = FastAPI(
            debug=True,
            title="Device Data Web Application ",
            description="This API provides access to sensor data, "+
                "allowing you to retrieve the latest data entries or "+
                "data within a specified time range.",
            version="1.0",
        )

    def patchRoutes(self):
        """Connect all the api-routers applicable in the application"""
        log.info(" Linking the api-routers ")
        self.app.include_router(sensor_data_router.route)


if __name__ == "__main__":
    api = WebApplication()
    servlet = Servlet()
    executor = servlet.configure_server(api)
    executor.run()
