from typing import Tuple

from decimal.decimal import Decimal
from exc import NoRootFoundException
from polynomial import Polynomial


def get_bisection(polynomial: Polynomial, start: Decimal, end: Decimal, count: int) -> Tuple[Decimal, Decimal]:
    """
    Get roots using bisection method.

    :param polynomial: polynomial object.
    :param start: start point in interval.
    :param end: end point in interval.
    :param count: the maximum number of recursive call.

    :return: the root value found and error.
    """
    f_start = polynomial(start)
    f_end = polynomial(end)

    # if interval is 0,
    if start == end:
        return start, Decimal()

    # if signs in interval x0 and x1 is the same, there is no root
    # value in the interval for polynomial function.
    if f_start.sign == f_end.sign:
        raise NoRootFoundException

    # gets the mid point and the polynomial value for mid point.
    mid = (start + end) / Decimal(2)
    f_mid = polynomial(mid)

    # if iterated maximum, returns the mid point value and error.
    if count == 0:
        return mid, mid - start

    # go to next step. The next step interval is the half of current step.
    if f_mid.sign == f_start.sign:
        return get_bisection(polynomial, mid, end, count - 1)
    else:
        return get_bisection(polynomial, start, mid, count - 1)
