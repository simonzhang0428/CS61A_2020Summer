# 06/24/2020

# A description of the formal parameters of a function is called the function's signature.
# all built-in functions will be rendered as <name>(...),
# because these primitive functions were never explicitly defined.

# A name evaluates to the value bound to that name in the earliest frame
# of the current environment in which that name is found.

# A new local frame is introduced every time a function is called,
# even if the same function is called twice.

# the scope of a local name is limited to the body of the user-defined function that defines it.
# the parameter names of a function must remain local to the body of the function.

# Function names are lowercase, with words separated by underscores. Descriptive names are encouraged.
# Function names typically evoke operations applied to arguments by the interpreter (e.g., print, add, square)
# or the name of the quantity that results (e.g., max, abs, sum).

# Parameter names are lowercase, with words separated by underscores. Single-word names are preferred.
# Parameter names should evoke the role of the parameter in the function, not just the kind of argument that is allowed.
# Single letter parameter names are acceptable when their role is obvious,
# but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.

# The domain of a function is the set of arguments it can take.
# The range of a function is the set of values it can return.
# The intent of a function is the relationship it computes between inputs and output
# (as well as any side effects it might generate).


from operator import mul, add


def square(x):
    return mul(x, x)


print('square of 21:', square(21))
print('(2+5)^2 =', square(add(2, 5)))
print('(3^2)^2 =', square(square(3)))


def sum_squares(x, y):
    return add(square(x), square(y))


print('3^2+ 4^2 =', sum_squares(3, 4))


from operator import truediv, floordiv

print('5 / 4 =', truediv(5, 4))
print('5 // 4 =', floordiv(5, 4))

"""
square of 21: 441
(2+5)^2 = 49
(3^2)^2 = 81
3^2+ 4^2 = 25
5 / 4 = 1.25
5 // 4 = 1
"""