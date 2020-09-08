"""
Decimal class helps to represent floating points as decimal floating.
"""
from functools import total_ordering, reduce
from typing import Optional, Union


@total_ordering
class Decimal:
    floating_points = 10

    def __init__(self, s: Optional[Union[str, int, 'Decimal']] = None):
        if isinstance(s, Decimal):
            self.n = s.n
        elif isinstance(s, int):
            self.n = s * (10 ** self.floating_points)
        elif isinstance(s, (str, type(None))):
            if s is None:
                s = '0'

            if '.' not in s:
                s = s + '.'

            is_neg = False
            if s.startswith('+') or s.startswith('-'):
                is_neg = s[0] == '-'
                s = s[1:]

            integer_part, float_part = s.split('.')
            float_part = float_part[:self.floating_points]

            integer_part, float_part = int(integer_part), int(float_part + '0' * (self.floating_points - len(float_part)))

            self.n = (integer_part * (10 ** self.floating_points) + float_part) * (-1 if is_neg else 1)
        else:
            raise NotImplemented('Decimal supports only string or Decimal parameter.')

    @classmethod
    def change_floating_points(cls, floating_points: int):
        Decimal.floating_points = floating_points

    @property
    def sign(self):
        return '+' if self.n >= 0 else '-'

    @property
    def integer_part(self):
        return str(abs(self.n) // (10 ** self.floating_points))

    @property
    def floating_part(self):
        _f = abs(self.n) % (10 ** self.floating_points)
        return '0' * (self.floating_points - len(str(_f))) + str(_f)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{"-" if self.n < 0 else ""}{self.integer_part}.{self.floating_part}'

    def __copy__(self):
        return Decimal(self)

    def __pow__(self, power, modulo=None):
        if not isinstance(power, int):
            raise NotImplemented('Decimal only supports power by integer.')

        if power == 0:
            return Decimal('1')
        if power == 1:
            return self.__copy__()

        return self.__copy__() * self.__pow__(power - 1)

    def __add__(self, other):
        v = self.__copy__()
        v.n += Decimal(other).n
        return v

    def __sub__(self, other):
        v = self.__copy__()
        v.n -= Decimal(other).n
        return v

    def __mul__(self, other):
        v = self.__copy__()
        v.n *= Decimal(other).n
        v.n //= 10 ** self.floating_points
        return v

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __floordiv__(self, other):
        v = self.__copy__()
        other_v = Decimal(other).n
        sign = (-1 if (v.n > 0) ^ (other_v > 0) else 1)
        v.n = sign * (abs(v.n * (10 ** self.floating_points)) // abs(other_v))
        return v

    def __abs__(self):
        v = self.__copy__()
        v.n = abs(v.n)
        return v

    def __pos__(self):
        v = self.__copy__()
        return v

    def __neg__(self):
        v = self.__copy__()
        v.n = -v.n
        return v

    def __iadd__(self, other):
        self.n = (Decimal(self) + Decimal(other)).n

    def __isub__(self, other):
        self.n = (Decimal(self) - Decimal(other)).n

    def __imul__(self, other):
        self.n = (Decimal(self) * Decimal(other)).n

    def __idiv__(self, other):
        self.n = (Decimal(self) / Decimal(other)).n

    def __eq__(self, other):
        return self.n == other.n

    def __lt__(self, other):
        return self.n < other.n
