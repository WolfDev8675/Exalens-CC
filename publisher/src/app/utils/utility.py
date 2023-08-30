#!usr/bin/python3
""" Random value generator functions used for setting various temperatures  
Target: keep reading as a simulation 
"""
# IMPORTS
from random import uniform

def get_random_temperature():
    """ Generate a random temperature 
    Liveable temperature range taken as 24 - 29 Celcius
    """
    return uniform(24.00,29.00)

def get_random_humidity():
    """ Generate a random humidity 
    Liveable humidity range taken as 30% - 85% 
    """
    return uniform(30.00,85.00)
