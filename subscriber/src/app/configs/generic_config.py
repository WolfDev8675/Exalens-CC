#!usr/bin/python3
""" Configuration generation for reading the Application Configurations """
import yaml
import os


class GenericConfig:

    def __init__(self):
        """ READ CONFIG FILE """
        config_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "config.yml",
        )
        config_file = open(config_file_path, "r")
        self.config_dict = yaml.safe_load(config_file)
    
    def get_mqtt_config(self):
        """ Return back with the details of the MQTT """
        return {
            "host":self.config_dict["mqtt"]["service"]["host"],
            "port":self.config_dict["mqtt"]["service"]["port"]
        }

    def get_server_port(self):
        """ Pulls the Server port from the Config file"""
        return self.config_dict["server"]["port"]

    def get_server_host(self):
        """ Pulls the Server hosted URL from the Config file"""
        return self.config_dict["server"]["host"]
    
    def get_connection_details(self,db_type):
        """ Send details of the DB connections back
    as a dictionary for proper operations"""
        return {"driver_name": self.config_dict["app"]["datastore"][db_type]["driver-name"],
            "host": self.config_dict["app"]["datastore"][db_type]["host"],
            "port": self.config_dict["app"]["datastore"][db_type]["port"],
            "username": self.config_dict["app"]["datastore"][db_type]["username"],
            "database": self.config_dict["app"]["datastore"][db_type]["database-name"],
            "password": self.config_dict["app"]["datastore"][db_type]["password"]
            }
    
    def get_connection_string(self,db_type):
        """ Send back the Connection string to the respective database """
        return self.config_dict["app"]["datastore"][db_type]["connection-string"]