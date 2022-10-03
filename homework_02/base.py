from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        if not self.started:
            raise exceptions.LowFuelError

    def move(self):
        if self.weight / self.fuel_consumption > self.fuel:
            raise exceptions.NotEnoughtFuel

    def __str__(self):
        return f"{self.__class__.__name__} (weight = {self.weight}, started = {self.started}, fuel = {self.fuel}, fuel_consumption = {self.fuel_consumption})"


def main():
    try:
        test = Vehicle(1000, 0, 50)
        test.start()
    except exceptions.LowFuelError:
        print("low fuel")
    except exceptions.NotEnoughtFuel:
        print("not enought fuel")
    print(test)


if __name__ == '__main__':
    main()