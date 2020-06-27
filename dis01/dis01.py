# if <conditional expression>:
#       <suite of statements>
# elif <conditional expression>:
#       <suite of statements>
# else:
#       <suite of statements>

# and, reach the first false
# or, reach the first true

print('-1 and 0 and 1 =>', -1 and 0 and 1)  # first false
print('False or 9999 or 1/0 =>', False or 9999 or 1 / 0)  # first ture


def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    # if raining is True or temp < 60:
    #     return True
    # return False
    return temp < 60 or raining


# while <conditional clause>:
#       <body of statements>

def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# print(square(so_slow(5)))
"""
here! NEVER print since so_slow(5) evaluated first
infinite loop.
"""


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True


# 1. Draw the function object to the right-hand-side of the frames, denoting the
# intrinsic name of the function, its parameters, and the parent frame
# (e.g. func square(x) [parent = Global].
# 2. Write the function name in the current frame and draw an arrow from the
# name to the function object.


# Call expressions, such as square(2), apply functions to arguments.
# When executing call expressions, we create a new frame in our diagram to keep track of local variables:
# 1. Evaluate the operator, which should evaluate to a function.
# 2. Evaluate the operands from left to right.
# 3. Draw a new frame, labelling it with the following:
#       • A unique index (f1, f2, f3, ...)
#       • The intrinsic name of the function, which is the name of the function object itself.
#       For example, if the function object is func square(x) [parent=Global],
#       the intrinsic name is square.
#       • The parent frame ([parent=Global])
# 4. Bind the formal parameters to the argument values obtained in step 2 (e.g. bind x to 3).
# 5. Evaluate the body of the function in this new frame until a return value is obtained.
# Write down the return value in the frame.
# If a function does not have a return value, it implicitly returns None. In that case,
# the “Return value” box should contain None.


x = 3


def p(rint):
    print(rint)


def g(x, y):
    if x:
        print('one')
    elif x:
        print(True, x)
    if y:
        print(True, y)
    else:
        print(False, y)
    return print(p(y)) + x


"""
>>> x, y = 2, x   
>>> g(y, p("rint"))
rint
one
False None
None
None
Error

"""
