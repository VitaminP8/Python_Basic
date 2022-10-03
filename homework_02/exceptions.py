"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass


def main():
    a = 0
    try:
        a < 10
    except LowFuelError:
        LowFuelError()


if __name__ == '__main__':
    main()