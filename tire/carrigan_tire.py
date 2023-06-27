from .tire import Tire

class CarriganTires (Tire):
    tire_wear: list[float]

    def __init__(self, tire_wear: list[float]) -> None:
        super().__init__()
        self.tire = tire_wear

    def needs_service(self) -> bool:
        return any(tire >= 0.9 in self.tire_wear)