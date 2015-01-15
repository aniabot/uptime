#!/usr/bin/env python

from __future__ import print_function
from fractions  import Fraction as F

import itertools
import sys

def fact(n):
    result = 1
    for i in xrange(1, n + 1):
        result = result * i
    return result

def binomial(k, n, p):
    j = n - k
    q = 1 - p
    return (p ** k) * (q ** j) * F(fact(n), fact(k) * fact(j))

def binomial_cum(k, n, p):
    result = 0
    for i in range(k, n + 1):
        result = result + binomial(i, n, p)
    return result

def main(args):
    if len(args) < 3:
        print('usage: {} <node up> <desired cluster up>'.format(args[0]),
              file=sys.stderr)
        return -1

    p = F(float(args[1]))
    U = F(float(args[2]))

    for n in itertools.count(2, 2):
        lower = (n / 2) - 1
        if lower <= 0:
            continue

        u = binomial_cum(lower, n, p)
        if u > U:
            print('{} nodes provide {} uptime'.format(n, float(u)))
            break

if __name__ == '__main__':
    sys.exit(main(sys.argv))

