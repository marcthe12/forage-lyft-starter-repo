from datetime import date
from abc import ABC

from serviceable import Serviceable
from engine import *
from batttery import *

class Car(Serviceable, ABC):
    engine: Engine
    battery: Battery
    
    def __init__(self,engine: Engine, battery: Battery) -> None:
        super().__init__()
        self.engine = engine 
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
     @staticmethod
     def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date)) 
    
     @staticmethod
     def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date)) 

     @staticmethod
     def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date)) 

     @staticmethod
     def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date)) 

     @staticmethod
     def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))
