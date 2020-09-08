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

    if start == end:
        return start, Decimal()

    if f_start.sign == f_end.sign:
        raise NoRootFoundException

    mid = (start + end) / Decimal(2)
    f_mid = polynomial(mid)

    if count == 0:
        return mid, mid - start

    if f_mid.sign == f_start.sign:
        return get_bisection(polynomial, mid, end, count - 1)
    else:
        return get_bisection(polynomial, start, mid, count - 1)
