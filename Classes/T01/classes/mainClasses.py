from enum import Enum
from Enums.mainEnum import CarStatus

class Car :
    def __init__(self):
        self._nickname = ""
        self._make = ""
        self._model = ""
        self._year = ""
        self._status = CarStatus.OK
        self._fuelLvl = 0
        self._oilLifeLeft = 100
        self._fuelEcon = 12.7 # Km/l
        self._odo = 0

    def __str__(self):
        return f"\n{self._nickname}\
            \n  Car info: {self._make} {self._model} ({self._year})\
            \n  Status: {self._status.name}\
            \n  Fuel Level: {self._fuelLvl}L - ({self._fuelEcon} Km/l)\
            \n  Odometer: {self._odo} Km - Range: {self._fuelLvl * self._fuelEcon} Km\
            \n  Oil Life Left: {self._oilLifeLeft}%\
            \n"

# region Getters and Setters

    def getStatus(self) -> CarStatus:
        return self._status

    def setStatus(self, status: CarStatus):
        self._status = status

    def setValues(self, make: str, model: str, year: str, nickname: str = ""):
        self._make = make
        self._model = model
        self._year = year
        self._nickname = nickname

# endregion

# region fuel
    def refuel(self, fuel: float) -> float:
        self._fuelLvl += fuel
        if self._fuelLvl > 100:
            self._fuelLvl = 100
        if self._fuelLvl > 20:
            self.setStatus(CarStatus.FUEL_OK)
        elif self._fuelLvl <= 20 and self._fuelLvl > 0:
            self.setStatus(CarStatus.FUEL_LOW)
        else:
            self.setStatus(CarStatus.FUEL_MPT)
        return self._fuelLvl

    def getFuelLvl(self) -> float:
        return self._fuelLvl

    def consumeFuel(self, cons: float) -> float:
        self._fuelLvl -= cons
        if self._fuelLvl <= 20:
            self._status = CarStatus.FUEL_LOW
            return self._fuelLvl
        else:
            return self._fuelLvl

# endregion

# region engine

    def start(self) -> bool:
        if self._status == CarStatus.ENGINE_RUN:
            return True
        elif self._status == CarStatus.ENGINE_STOP:
            self.setStatus(CarStatus.ENGINE_RUN)
            self.consumeFuel(0.01)
            return True
        else:
            return False

    def stop(self) -> bool:
        if self._status == CarStatus.ENGINE_STOP:
            return True
        elif self._status == CarStatus.ENGINE_RUN:
            self.setStatus(CarStatus.ENGINE_STOP)
            return True
        else:
            return False

    def checkEngine(self):
        if self._oilLifeLeft >= 10 and self._fuelLvl > 20:
            return CarStatus.OK
        elif self._oilLifeLeft < 10:
            return CarStatus.ENGINE_FAULT
        elif self._fuelLvl <= 20:
            return CarStatus.FUEL_LOW

    def changeOil(self) -> int:
        self._oilLifeLeft = 100
        return self._oilLifeLeft

# endregion