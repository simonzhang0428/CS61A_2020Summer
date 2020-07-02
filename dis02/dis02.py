def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)

        return g

    return f


make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)


def curry(h):
    return lambda h: lambda x: lambda y: h(x, y)


n = 7


def f(x):
    n = 8
    return x + 1


def g(x):
    n = 9

    def h():
        return x + 1

    return h


def f(f, x):
    return f(x + n)


f = f(g, n)
g = (lambda y: y())(f)

# 1.4
y = "y"
h = y


def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)


y = y(y)(y)


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true.

    >>> def is_even(x): return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    k = 1
    while k <= n:
        if cond(k):
            print(k)
        k = k + 1


def make_keeper(n):
    """Return a function which takes one parameter cond and prints out all integers 1..i..n
    where calling cond(i) returns True.
    >>> def is_even(x): return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """

    def f(cond):
        keep_ints(cond, n)

    return f


# Self Refrence, where a function eventually returns itself.
# In particular, a self-referencing function will not return a function call,
# but rather the function object itself.
def print_all(x):
    print(x)
    return print_all


# Self-referencing functions will oftentimes employ helper functions that
# reference the outer function, such as the example to the right, print sums.
def print_sums(n):
    print(n)

    def next_sum(k):
        return print_sums(n + k)

    return next_sum


def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Write a function print n that can take in an integer n and returns a repeatable print function
# that can print the next n parameters. After the nth parameter, it just prints ”done”.
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

# our order of evaluation is evaluate the operator, evaluate the operands,
# apply the function to the operands.
# Hence, the operands are evaluated before the function call is initiated,
# so they must be evaluated in the frame in which the call was performed.
def yes(no):
    yes = 'no'
    return no

no = 'no'

def no(no):
    return no + yes(no)

yes = yes(yes)(no)('ok')