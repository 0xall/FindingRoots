# FindingRoots

FindingRoots is a program implemented by python, it helps to find root
for polynomial function.

# Usage

For printing help messages, use `-h` option.

```
python finding_roots.py -h
```

### Bisection method
```
python finding_roots.py 5 -22.4 15.85272 24.161472 -23.4824832 -b -2 0 -f 50 -c 100
```

For using bisection method, use `-b` option. Above command means it uses
the polynomial with 5x^4 - 22.4x^3 + 15.85272 x^2 + 24.161472 -23.4824832, 
uses bisection method with interval (-2, 0), uses the 50 floatings points,
and iterates with maximum 100 times.

### Newton-Raphson method

```
python finding_roots.py 5 -22.4 15.85272 24.161472 -23.4824832 -n 4 -f 50 -c 16
```

For using bisection method, use `-n` option. Above command means it uses
the polynomial with 5x^4 - 22.4x^3 + 15.85272 x^2 + 24.161472 -23.4824832, 
uses Newton-Raphson method with starting point x_1 = 4.0, uses the 50 
floatings points, and iterates with maximum 16 times.
