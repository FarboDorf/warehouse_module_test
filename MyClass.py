

from math import pi

class Circle():
    @staticmethod
    def CircleArea(radius):
        if type(radius) not in [int, float]:
            raise TypeError("Radius must be non-negative real number")
        if radius < 0:
            raise ValueError("Radius can only be positive")
        return pi*radius**2