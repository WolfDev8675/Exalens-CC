#!usr/bin/python3

from schedulers import job_scheduler 
from configs.server_config import Servlet
from fastapi import FastAPI
from logging import getLogger

log=getLogger("publisher|main")

class PublisherApplication:
    app: FastAPI

    def __init__(self) -> None:
        self.app = FastAPI(
            debug=True,
            title="Device Data Publisher Service",
            description="A service to publish data of various devices over the MQTT Broker ",
            version="1.0")
        
    def patchRoutes(self):
        """ Connect all the api-routers applicable in the application """
        log.info(" Linking the api-routers ")
        self.app.include_router(job_scheduler.api_router)



if __name__ == "__main__":
    api = PublisherApplication()
    servlet = Servlet()
    executor = servlet.configure_server(api)
    executor.run()
