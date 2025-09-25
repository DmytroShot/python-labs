from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name: str, speed: int, capacity: int):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance: int) -> float:
        pass

    @abstractmethod
    def fuel_consumption(self, distance: int) -> float:
        pass

    @abstractmethod
    def info(self) -> str:
        pass


class Car(Transport):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        if self.passengers > self.capacity:
            print("Перевантажено!")
        return distance * 0.07

    def info(self) -> str:
        return f"Car: {self.name}"


class Bus(Transport):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        if self.passengers > self.capacity:
            print("Перевантажено!")
        return distance * 0.15

    def info(self) -> str:
        return f"Bus: {self.name}"


class Bicycle(Transport):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, 20, capacity)

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def info(self) -> str:
        return f"Bicycle: {self.name}"


class ElectricCar(Car):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int):
        super().__init__(name, speed, capacity, passengers)

    def battery_usage(self, distance: int) -> float:
        return distance * 0.02

    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def info(self) -> str:
        return f"Electric Car: {self.name}"


def calculate_cost(distance: int, price_per_unit: float, transport: Transport) -> float:
    consumption = transport.fuel_consumption(distance)
    return consumption * price_per_unit

vehicles = [
    Car("Toyota", 100, 4, 3),
    Bus("Mercedes Bus", 80, 40, 45),
    Bicycle("Trek", 1),
    ElectricCar("Tesla", 120, 5, 4)
]

distance = 100
for vehicle in vehicles:
    print(vehicle.info())
    print(f"Час у дорозі: {vehicle.move(distance):.2f} год")
    print(f"Витрати пального/заряду: {vehicle.fuel_consumption(distance):.2f}")
    print("-" * 30)
