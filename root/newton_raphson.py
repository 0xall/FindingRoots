from decimal import Decimal
from exc import NoRootFoundException

from polynomial import Polynomial


def get_newton_raphson(polynomial: Polynomial, start: Decimal, count: int):
    """
    Gets the root value by using Newton-Raphson method.

    :param polynomial: the polynomial function for calculating the root.
    :param start: start position for Newton-Raphson method.
    :param count: the maximum number of iteration.

    :return: the root value found and error (%)
    """
    # diff is differential function for polynomial.
    diff = polynomial.differential()

    # get function value.
    poly_x = polynomial(start)
    # get gradient value.
    diff_x = diff(start)

    if diff_x == Decimal(0):
        # if diff_x is 0, it means the gradient is 0, it cannot get next
        # value, so checks the polynomial value.
        if poly_x == Decimal(0):
            # if gradient is 0 and also function value is 0, it is the
            # root of function.
            return start, Decimal(0)
        else:
            # if function value is not 0, cannot move next step.
            raise NoRootFoundException
    else:
        # if gradient is not 0, calculate the next x value. (x_(n+1))
        next_value = start - poly_x / diff_x

    if next_value == start or count == 0:
        return next_value, (next_value - start) / next_value if next_value != Decimal(0) else Decimal(1)
    else:
        return get_newton_raphson(polynomial, next_value, count - 1)
