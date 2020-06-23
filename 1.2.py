# 06/23/2020
#
# primitive expressions and statements, which represent the simplest building blocks that the language provides,
# means of combination, by which compound elements are built from simpler ones, and
# means of abstraction, by which compound elements can be named and manipulated as units.

x = max(min(1, -2), min(pow(3, 5), -4))
print(x)

from math import sqrt, pi

print('square of 256:', sqrt(256))
print('100 * pi:', pi * 100)

from operator import add, sub, mul

print('14 + 28:', add(14, 28))
print('100 - 7 * (8 + 4) = ', sub(100, mul(7, add(8, 4))))

print(max)
f = max
print(f)
print(f(2, 3, 4))
f = 2
print(f)

max = 5
print(max)
# max(2, 3, 4), bind built-in names to new values
# TypeError: 'int' object is not callable

x = 2
x = x + 1
print(x)

radius = 10
area, circumference = pi * radius * radius, 2 * pi * radius
print('area:', area)
print('circumference:', circumference)

x, y = 3, 4.5
y, x = x, y
print('x:', x)
print('y:', y)

print('2^(1+10) - 2^5 =', sub(pow(2, add(1, 10)), pow(2, 5)))

print('absolute value of -2:', abs(-2))
# pure function, always the same, good for concurrent programming

print(print(1), print(2))
# return None, non-pure, side-effect, careful when in nested expression
two = print(2)
print(two)
