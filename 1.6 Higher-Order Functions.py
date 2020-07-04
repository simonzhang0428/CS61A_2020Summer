# 06/25/2020

# Functions that manipulate functions are called higher-order functions.

# function as parameter/argument
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


print('Sum of first 100 naturals:', sum_naturals(100))


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total


print('Sum of first 100 natrurals cubes:', sum_cubes(100))


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
    return total


print('Sum of pi for first 100 terms:', pi_sum(100))


# def <name>(n):
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + <term>(k), k + 1
#     return total


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def identity(x):
    return x


def sum_naturals(n):
    return summation(n, identity)


print('Sum of first 10 naturals:', sum_naturals(10))


def square(x):
    return x * x


print('Sum of first 10 naturals\' square:', summation(10, square))


def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))


def pi_sum(n):
    return summation(n, pi_term)


print('10^6 approach to pi:', pi_sum(1e6))


# Golden Ratio
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 / guess + 1


def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


print('Golden Ratio is approach to:', improve(golden_update, square_close_to_successor))

from math import sqrt

phi = 1 / 2 + sqrt(5) / 2


def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation.'


improve_test()

"""
Sum of first 100 naturals: 5050
Sum of first 100 natrurals cubes: 25502500
Sum of pi for first 100 terms: 3.1365926848388144
Sum of first 10 naturals: 55
Sum of first 10 naturals' square: 385
10^6 approach to pi: 3.141592153589902
Golden Ratio is approach to: 1.6180339887498951
"""


def average(x, y):
    return (x + y) / 2


def sqrt_update(x, a):
    return average(x, a / x)


# This discipline of sharing names among nested definitions is called lexical scoping. Critically, the inner
# functions have access to the names in the environment where they are defined (not where they are called).
# locally defined functions are often called closures.
# Looking up a name finds the first value bound to that name in the current environment.
# then to its parent environment, last in global, if not find, raise Error.
def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)

    def sqrt_close(x):
        return approx_eq(x * x, a)

    return improve(sqrt_update, sqrt_close)


print('square root of 256:', sqrt(256))


# function composition
def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


# newton method
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


print('square root of 64:', square_root_newton(64))


def power(x, n):
    """Return x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


print('x^2 = 64, x =', nth_root_of_a(2, 64))
print('x^3 = 64, x =', nth_root_of_a(3, 64))
"""
square root of 256: 16.0
square root of 64: 8.0
2^x = 64, x = 8.0
3^x = 64, x = 4.0
"""


# We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions
# that each take a single argument. This transformation is called currying. currying is useful when we require a
# function that takes in only a single argument, such as Haskell.
def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


print('2^3 =', curried_pow(2)(3))


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1


map_to_range(0, 10, curried_pow(2))


def curry2(f):
    """Return a curried version of the given two-argument function."""

    # curry2(f)(x)(y) is equivalent to f(x, y).
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


# uncurry2(curry2(f)) is equivalent to f.
def uncurry2(g):
    """Return a two-argument version of given curried function."""

    def f(x, y):
        return g(x)(y)

    return f


pow_curried = curry2(pow)
print('2^5 =', pow_curried(2)(5))

map_to_range(0, 10, pow_curried(2))
print('2^5 =', uncurry2(pow_curried)(2, 5))

"""
1
2
4
8
16
32
64
128
256
512
2^5 = 32
"""


# A lambda expression evaluates to a function that has a single return expression as its body.
# Assignment and control statements are not allowed.
# in cases where a simple function is needed as an argument or return value.

#      lambda            x            :          f(g(x))
# "A function that    takes x    and returns     f(g(x))"

def compose2(f, g):
    return lambda x: f(g(x))


s = lambda x: x * x
print('12 * 12 =', s(12))


# example for lambda high order functions
def make_adder(x):
    def adder(y):
        return x + y
    return adder

def make_adder2(x):
    return lambda y: x + y

make_adder = lambda x: lambda y: x + y

# Some of the "rights and privileges" of first-class elements are:
#
# They may be bound to names.
# They may be passed as arguments to functions.
# They may be returned as the results of functions.
# They may be included in data structures.

def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)

    return wrapped


@trace
def triple(x):
    return 3 * x


# triple = trace(triple) The expression following @ is evaluated first (just as the name trace was evaluated above),
# the def statement second, and finally the result of evaluating the decorator expression is applied to the newly
# defined function, and the result is bound to the name in the def statement.
print(triple(23))
"""
->  <function triple at 0x1081adee0> ( 23 )
69
"""


# Think of this:
#
# print(x + 2)
# print(y + 2)
# print(z + 2)
# As opposed to this:
#
# print(adder(x))
# print(adder(y))
# print(adder(z))

# Less repetition! We don't have to add 2 every time anymore, because we have a function that does it for us. For
# that matter, this could be any number, not just 2! Here's the thing about currying: it's not for efficiency.
# Currying doesn't make your code any faster or slower, but it makes it more readable and organized.

# a funtion taht takes any argument and return a function that returns that argument
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

delay(delay)()(6)()
print(delay(print)()(4))

# function always returns the identity function
def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

from operator import add, mul
def square(x):
    return mul(x, x)

add(pirate(3)(square)(4), 1)
# pirate(pirate(pirate))(5)(7)
# matey
# matey
# Error

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)
horse(mask)