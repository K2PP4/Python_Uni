from enum import Enum

class CarStatus(Enum) :
    OK = 0,
    FUEL_OK = 1,
    FUEL_LOW = 2,
    FUEL_MPT = 3,
    ENGINE_FAULT = 4,
    ENGINE_RUN = 5,
    ENGINE_STOP = 6