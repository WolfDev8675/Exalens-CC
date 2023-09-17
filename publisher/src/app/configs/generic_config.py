#!usr/bin/python3
""" Configuration generation for reading the Application Configurations """
import yaml
import os


class GenericConfig:
    def __init__(self):
        """READ CONFIG FILE"""
        config_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "config.yml",
        )
        config_file = open(config_file_path, "r")
        self.config_dict = yaml.safe_load(config_file)

    def get_mqtt_config(self):
        """Return back with the details of the MQTT"""
        return {
            "host": self.config_dict["mqtt"]["service"]["host"],
            "port": self.config_dict["mqtt"]["service"]["port"],
        }

    def get_server_port(self):
        """Pulls the Server port from the Config file"""
        return self.config_dict["server"]["port"]

    def get_server_host(self):
        """Pulls the Server hosted URL from the Config file"""
        return self.config_dict["server"]["host"]
