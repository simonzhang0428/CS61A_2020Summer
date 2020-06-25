# Interactive Debugging
# python -i file.py
# python ok -q <question name> -i

# Visualizer
# http://pythontutor.com/composingprograms.html#mode=edit
# python ok -q <question name> --trace

# doctest
# python3 -m doctest file.py
# python3 -m doctest file.py -v

# Note: prefixing debug statements with the specific string "DEBUG: "
# allows them to be ignored by the ok auto grader used by cs61a.

# use a global debug variable
debug = True


def foo(n):
    i = 0
    while i < n:
        i += func(i)
    if debug:
        print('DEBUG: i is', i)


def func(i):
    pass


# Python has a feature known as an assert statement, which lets you test that a condition is true, and print an error
# message otherwise in a single line. This is useful if you know that certain conditions need to be true at certain
# points in your program. For example, if you are writing a function that takes in an integer and doubles it,
# it might be useful to ensure that your input is in fact an integer. You can then write the following code
def double(x):
    assert isinstance(x, int), "The input to double(x) must be an integer"
    return 2 * x

# One major benefit of assert statements is that they are more than a debugging tool, you can leave them in code
# permanently. A key principle in software development is that it is generally better for code to crash than produce
# an incorrect result, and having asserts in your code makes it far more likely that your code will crash if it has a
# bug in it.


# The reason the error message says "global name" is because Python will start searching for the variable from a
# function's local frame. If the variable is not found there, Python will keep searching the parent frames until it
# reaches the global frame. If it still can't find the variable, Python raises the error. IndexError