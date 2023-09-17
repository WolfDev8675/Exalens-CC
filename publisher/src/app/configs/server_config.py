#!usr/bin/python3

import uvicorn
from configs.generic_config import GenericConfig


class Servlet:
    host: str
    port: int
    server: uvicorn.Server

    def __init__(self):
        _get_Config = GenericConfig()
        self.host = _get_Config.get_server_host()
        self.port = _get_Config.get_server_port()

    def configure_server(self, api) -> uvicorn.Server:
        """Configure server to host the required API"""
        api.patchRoutes()
        config = uvicorn.Config(api.app, host=self.host, port=self.port)

        self.server = uvicorn.Server(config)
        return self.server
