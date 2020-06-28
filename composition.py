# programs are written to be read by humans,
# and only incidentally to be interpreted by computers.
# A program is composed well if it is concise, well-named, understandable, and easy to follow.

# Purpose. Each line of code in a program should have a purpose.

# Functions. When given the choice between calling a function or copying and pasting its body,
# strive to call the function and maintain abstraction in your program.

# Brevity. look for opportunities to reduce the size of your program substantially
# by reusing functions you have already defined.

# Use lower_case_and_underscores for variables and functions:
total_score = 0
final_score = 1


def mean_strategy(score, opp):
    pass


# On the other hand, use CamelCase for classes:
class ExampleClass:
    pass

# Line Length
# Keep lines under 80 characters long. Other conventions use 70 or 72 characters,
# but 80 is usually the upper limit. 80 characters is not a hard limit, but exercise good judgement!
# Long lines might be a sign that the logic is too much to fit on one line!

# Double-spacing
# Don't double-space code. That is, do not insert a blank line in between lines of code.
# It increases the amount of scrolling needed and goes against the style of the rest of the code we provide.
# One exception to this rule is that there should be space between two functions or classes.

# Spaces with operators
# Use spaces between + and -. Depending on how illegible expressions get, you can use your own judgement for
# *, /, and ** (as long as it's easy to read at a glance, it's fine).
#
# x = a + b*c*(a**2) / c - 4

# Spacing lists
# When using tuples, lists, or function operands, leave one space after each comma ,:
#
# tup = (x, x/2, x/3, x/4)

# Line wrapping
# If a line gets too long, use parentheses to continue onto the next line:
#
# def func(a, b, c, d, e, f,
#          g, h, i):
#     # body
#
# tup = (1, 2, 3, 4, 5,
#        6, 7, 8)
# names = ('alice',
#          'bob',
#          'eve')

# Blank lines
# Leave a blank line between the end of a function or class and the next line:
#
# def example():
#     return 'stuff'
#
# x = example() # notice the space above

# Trailing whitespace
# Don't leave whitespace at the end of a line.

# Boolean comparisons
# Don't compare a boolean variable to True or False:
#
# if pred == True:   # bad!
#     ...
# if pred == False:  # bad!
#     ...
# Instead, do this:
#
# if pred:           # good!
#     ...
# if not pred:       # good!
#     ...
# Use the "implicit" False value when possible.
# Examples include empty containers like [], (), {}, set().
#
# Good
#
# if lst:       # if lst is not empty
#     ...
# if not tup:   # if tup is empty
#     ...

# Checking None
# Use is and is not for None, not == and !=.

# Parentheses are not necessary in Python conditionals
# (they are in other languages though).
# if x == 4:
#     ...

# Remove commented-out code
# Remove commented-out code from final version. You can comment lines out when you are debugging
# but make sure your final submission is free of commented-out code.
# This makes it easier for readers to identify relevant portions of code.

# Only use comments if something is not obvious or needs to be explicitly emphasized.

# Generator expressions are okay for simple expressions.
# This includes list comprehensions, dictionary comprehensions, set comprehensions, etc.
# Generator expressions are neat ways to concisely create lists. Simple ones are fine:
# ex = [x*x for x in range(10)]
# L = [pair[0] + pair[1]
#      for pair in pairs
#      if len(pair) == 2]