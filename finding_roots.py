import argparse

from decimal import Decimal
from exc import NoRootFoundException
from polynomial import Polynomial
from root import get_bisection, get_newton_raphson

args = argparse.ArgumentParser()
args.add_argument('coefficients', type=str, nargs='+', help='Coefficient list for polynomial')
args.add_argument('--bisection', '-b', type=str, nargs=2, metavar=('x1', 'x2'), help='Use bisection with interval (x1, x2)')
args.add_argument('--newton', '-n', type=str, nargs=1, metavar='x1', help='Use Newton Raphson starting with curve in x1')
args.add_argument('--floating-points', '-f', type=int, default=10, metavar='N', help='The number of floating points to use.')
args.add_argument('--count', '-c', default=10, type=int, help='the maximum count for method iteration.')


if __name__ == '__main__':
    args = args.parse_args()
    Decimal.change_floating_points(args.floating_points)

    polynomial = Polynomial(*map(lambda x: Decimal(x), args.coefficients))

    try:
        if args.bisection:
            root, error = get_bisection(polynomial, Decimal(args.bisection[0]), Decimal(args.bisection[1]), args.count)
        else:
            root, error = get_newton_raphson(polynomial, Decimal(args.newton[0]), args.count)
    except NoRootFoundException:
        print('Cannot find root value by this method..')
        exit(1)

    print(f'Root  : {root}')
    print(f'Error : {abs(error)}')
