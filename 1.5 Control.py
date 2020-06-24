# 06/24/2020

# Compound statements typically span multiple lines and
# start with a one-line header ending in a colon, which identifies the type of statement.
# Together, a header and an indented suite of statements is called a clause.
# A compound statement consists of one or more clauses:

# statements are executed in order,
# but later statements may never be reached, because of redirected control.

# A return statement redirects control:
# the process of function application terminates whenever the first return statement is executed,
# and the value of the return expression is the returned value of the function being applied.

# The fact that functions can only manipulate their local environment is critical to creating modular programs,
# in which pure functions interact only via the values they take and return.

# local assignment also plays a critical role in clarifying the meaning of complex expressions
# by assigning names to intermediate quantities.

# Python includes several false values, including 0, None, and the boolean value False.
# All other numbers are true values.

print('4 or 3:', 4 or 3)
print('4 and 3:', 4 and 3)
print('None and 5:', None and 5)
print('None or 5:', None or 5)
print('not 3:', not 3)
print('not None:', not None)
print('0 or None and 5:', 0 or None and 5)
print('1 and None or 5:', 1 and None or 5)


def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1  # Fibonacci numbers 1 and 2
    k = 2  # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr


# An assert statement has an expression in a boolean context,
# followed by a quoted line of text (single or double quotes are both fine, but be consistent)
# that will be displayed if the expression evaluates to a false value.

assert fib(8) == 13, 'The 8th Fibonacci number should be 13.'


def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'


fib_test()


# The first line of a docstring should contain a one-line description of the function,
# followed by a blank line.
# A detailed description of arguments and behavior may follow.
# In addition, the docstring may include a sample interactive session that calls the function.
def sum_naturals(n):
    """Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total = 0
    while n >= 1:
        total = total + n
        n = n - 1
    return total

# simple doctest
from doctest import testmod

testmod()

# verbose version, test single function
from doctest import run_docstring_examples

run_docstring_examples(sum_naturals, globals(), True)

"""
4 or 3: 4
4 and 3: 3
None and 5: None
None or 5: 5
not 3: False
not None: True
0 or None and 5: None
1 and None or 5: 5
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok

"""