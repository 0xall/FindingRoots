from functools import reduce
from typing import List

from decimal import Decimal


class Polynomial:
    """
    Represents polynomial function. It supports the calculating value in x and
    getting differential of polynomial function.
    """
    def __init__(self, *args: List[Decimal]):
        if len(args) == 0:
            # if no polynomial arguments (it means no coefficient), it's 0-degree polynomial (y = 0)
            self.coefficients = [Decimal()]
        else:
            self.coefficients = list(reversed(args))

    def __call__(self, x: Decimal):
        """
        Returns the value from the polynomial with x.
        :param x: the value.
        :return: calculated from the polynomial with x.
        """
        return reduce(
            lambda prev, value: prev + value[1] * (x ** value[0]),
            enumerate(self.coefficients),
            Decimal()
        )

    def differential(self):
        """
        Returns the differential polynomial object.
        :return: the differential polynomial.
        """
        return Polynomial(*reversed([(coefficient * (degree + 1)) for degree, coefficient in enumerate(self.coefficients[1:])]))
