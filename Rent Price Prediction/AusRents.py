# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class AusRents(BaseModel):
    Beds: float 
    Baths: float 
    Cars: float 
    Suburb: str
    State: str
    Type: str
    RentMonth: str
    Streetname: str
    

    