# to sum the digits of a number n, add its last digit n % 10 to the sum of the digits of n // 10.
# There's one special case: if a number has only one digit, then the sum of its digits is itself.
def sum_digits(n):
    """Return sum of first n naturals.
    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return last + sum_digits(all_but_last)


# A common pattern can be found in the body of many recursive functions. The body begins with a base case,
# a conditional statement that defines the behavior of the function for the inputs that are simplest to process. In
# the case of sum_digits, the base case is any single-digit argument, and we simply return that argument. Some
# recursive functions will have multiple base cases.

# The base cases are then followed by one or more recursive calls. Recursive calls always have a certain character:
# they simplify the original problem. Recursive functions express computation by simplifying problems incrementally.

# it is often clearer to think about recursive calls as functional abstractions. That is, we should not care about
# how fact(n-1) is implemented in the body of fact; we should simply trust that it computes the factorial of n-1.
# Treating a recursive call as a functional abstraction has been called a recursive leap of faith.

# In general, iterative functions must maintain some local state that changes throughout the course of computation.
# At any point in the iteration, that state characterizes the result of completed work and the amount of work
# remaining.
def fact_iter(n):
    """Return nth factorial using iterator.
    >>> fact_iter(4)
    24
    """
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


# On the other hand, fact is characterized by its single argument n. The state of the computation is entirely
# contained within the structure of the environment, which has return values that take the role of total, and binds n
# to different values in different frames rather than explicitly tracking k.

# Recursive functions leverage the rules of evaluating call expressions to bind names to values,
# often avoiding the nuisance of correctly assigning local names during iteration.
# For this reason, recursive functions can be easier to define correctly.
def fact(n):
    """Return nth factorial using recursion.
    >>> fact(4)
    24
    """
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# When a recursive procedure is divided among two functions that call each other,
# the functions are said to be mutually recursive.
# As an example, consider the following definition of even and odd for non-negative integers:
#
# a number is even if it is one more than an odd number
# a number is odd if it is one more than an even number
# 0 is even

def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)


# change mutually recursive into a single recursive function by breaking the abstraction boundary between the two
# functions. In this example, the body of is_odd can be incorporated into that of is_even, making sure to replace n
# with n-1 in the body of is_odd to reflect the argument passed into it:
def is_even2(n):
    if n == 0:
        return True
    else:
        if (n - 1) == 0:
            return False
        else:
            return is_even2((n - 1) - 1)


def cascade(n):
    """Print a cascade of prefixes of n.

    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade2(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def inverse_cascade(n):
    grow = lambda n: f_then_g(grow, print, n // 10)
    shrink = lambda n: f_then_g(print, shrink, n // 10)
    grow(n)
    print(n)
    shrink(n)


inverse_cascade(2013)


# As another example of mutual recursion, consider a two-player game in which there are n initial pebbles on a table.
# The players take turns, removing either one or two pebbles from the table, and the player who removes the final
# pebble wins. Suppose that Alice and Bob play this game, each using a simple strategy:
#
# Alice always removes a single pebble
# Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
# Given n initial pebbles and Alice starting, who wins the game?
def play_alice(n):
    if n == 0:
        print('Bob wins!')
    else:
        play_bob(n - 1)


def play_bob(n):
    if n == 0:
        print('Alice wins!')
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)


play_alice(20)


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def count_partitions(n, m):
    """Count the ways to partition n using paarts up to m.
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    assert type(m) == int and type(n) == int, 'input must be integer.'
    assert m > 0 and n > 0, 'input must be positive'
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


# paths(-1, 1)
# paths(0.2, 5)

# make use of template, make sure your time is almost always creative time
# use simplest test to begin
def remove(n, digit):
    """Return all digits of non-negative N that are not DIGIT.
    >>> remove(231, 2)
    31
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits = digits + 1
    return kept


from doctest import testmod

testmod()
