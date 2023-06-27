from datetime import date
from .battery import Battery

class NubbinBattery(Battery):
    last_service_date: date
    current_date: date

    def __init__(self, current_date: date, last_service_date: date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_date.year > 4
