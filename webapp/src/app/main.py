#!usr/bin/python3

from configs.server_config import Servlet
from fastapi import FastAPI
from logging import getLogger

log=getLogger("webapp|main")

class WebApplication:
    app: FastAPI

    def __init__(self) -> None:
        self.app = FastAPI(
            debug=True,
            title="Device Data Web Application ",
            description="An API Service provider to access the specific data of the devices ",
            version="1.0")
        
    def patchRoutes(self):
        """ Connect all the api-routers applicable in the application """
        log.info(" Linking the api-routers ")
        


if __name__ == "__main__":
    api = WebApplication()
    servlet = Servlet()
    executor = servlet.configure_server(api)
    executor.run()
