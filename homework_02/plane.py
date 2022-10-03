"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02 import exceptions
from homework_02 import base


class Plane(base.Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        # self.weight = weight
        # self.fuel = fuel
        # self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, temp_cargo):
        if self.cargo + temp_cargo <= self.max_cargo:
            self.cargo = self.cargo + temp_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo (self):
        temp_cargo = self.cargo
        self.cargo = 0
        return temp_cargo


def main():
    pass


if __name__ == '__main__':
    main()