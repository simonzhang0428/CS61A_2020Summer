# Isolate two parts of any program to use data:
# how data are represented (as parts)
# how data are manipulated (as units)
# enforce an abstraction barrier between representation and use

# you can recoginize data abstruction by ites behavior.(not implementation)

# data abstraction isolates how a compound data value is used from the details of how it is constructed. The basic
# idea of data abstraction is to structure programs so that they operate on abstract data. That is, our programs
# should use data in such a way as to make as few assumptions about the data as possible. At the same time,
# a concrete data representation is defined as an independent part of the program.

# Let us further assume that the constructor and selectors are available as the following three functions:
#
# rational(n, d) returns the rational number with numerator n and denominator d.
# numer(x) returns the numerator of the rational number x.
# denom(x) returns the denominator of the rational number x.
# We are using here a powerful strategy for designing programs: wishful thinking.
# We haven't yet said how a rational number is represented,
# or how the functions numer, denom, and rational should be implemented.

pair = [10, 20]
x, y = pair  # unpacking
print('x, y:', x, y)

# index represents how far an element is offset from the beginning of the list.
# start form 0, getitem, offset, substract get length
from operator import getitem

x = getitem(pair, 0)
y = getitem(pair, 1)
print('x, y:', x, y)


def rational1(n, d):
    """Construct a rational number taht represent N/D."""
    return [n, d]

from math import gcd
def rational(n, d):
    g = gcd(n, d)  # reduce to lowest term
    return (n//g, d//g)

def numer(x):
    return x[0]


def denom(x):
    return x[1]


def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
    print(numer(x), '/', denom(x))


def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


half = rational(1, 2)
print_rational(half)
third = rational(1, 3)
print_rational(mul_rationals(half, third))
print_rational(add_rationals(third, third))


def square_rational(x):
    return mul_rational(x, x)

# Abstraction barriers make programs easier to maintain and to modify.
# The fewer functions that depend on a particular representation,
# the fewer changes are required when one wants to change that representation.

# If a pair p was constructed from values x and y, then select(p, 0) returns x, and select(p, 1) returns y.
# We don't actually need the list type to create pairs.
# Instead, we can implement two functions pair and select
# that fulfill this description just as well as a two-element list.
def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

p = pair(20, 14)
print('pair => ', p)
print('index 0:', select(p, 0))
print('index 1:', select(p, 1))