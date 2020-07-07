from operator import mul

digits = [1, 8, 2, 8]
print('dights:', digits)
print('length:', len(digits))
print('digits[3]:', digits[3])

print('digits[0:2]', digits[0:2])
print('digits[1:]', digits[1:])

lst = [2, 7] + digits * 2
print(lst)

pairs = [[10, 20], [30, 40]]
print('pairs[1]:', pairs[1])
print('pairs[1][0]:', pairs[1][0])


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


print('how many 8 in digits: ', count(digits, 8))


def count2(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


print('how many 8 in digits: ', count2(digits, 8))

# A for statement consists of a single clause with the form:
#
# for <name> in <expression>:
#     <suite>
# A for statement is executed by the following procedure:
#
# Evaluate the header <expression>, which must yield an iterable value.
# For each element value in that iterable value, in order:
#   Bind <name> to that value in the current frame.
#   Execute the <suite>.

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count = same_count + 1

# This pattern of binding multiple names to multiple values in a fixed-length sequence
# is called sequence unpacking; it is the same pattern that we see in assignment statements
# that bind multiple names to multiple values.
print('same count:', same_count)

lst = list(range(5, 8))
print('range(5, 8):', lst)

# A common convention is to use a single underscore character (_)
# for the name in the for header if the name is unused in the suite:
for _ in range(3):
    print('Go Bears!')

# List Comprehensions. Many sequence processing operations can be expressed by
# evaluating a fixed expression for each element in a sequence
# and collecting the resulting values in a result sequence.
odds = [1, 3, 5, 7]
evens = [x + 1 for x in odds]
print('evens:', evens)

# Another common sequence processing operation is to select a subset of values
# that satisfy some condition.
lst = [x for x in odds if 25 % x == 0]
print('% 25 == 0:', lst)


# The general form of a list comprehension is:
# [<map expression> for <name> in <sequence expression> if <filter expression>]

# To evaluate a list comprehension, Python evaluates the <sequence expression>,
# which must return an iterable value. Then, for each element in order,
# the element value is bound to <name>, the filter expression is evaluated,
# and if it yields a true value, the map expression is evaluated.
# The values of the map expression are collected into a list.

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]


print('divisors of 4:', divisors(4))
print('divisors of 12:', divisors(12))

# A perfect number is a positive integer that is equal to the sum of its divisors.
perfect_num = [x for x in range(1, 1000) if sum(divisors(x)) == x]
print('perfect number 1 - 1000:', perfect_num)


def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


# The height of a rectangle with integer side lengths must be a divisor of its area.
# We can compute the minimum perimeter by considering all heights.
def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)


area = 80
print('width:', width(area, 5))
print('perimeter 5 * 16:', perimeter(16, 5))
print('perimeter 8 * 10:', perimeter(10, 8))
print('minimum perimeter with area 80:', minimum_perimeter(80))


def apply_to_all(map_fn, s):
    return [map_fn for x in s]


apply_to_all = lambda map_fn, s: list(map(map_fn, s))


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


keep_if = lambda filter_fn, s: list(filter(filter_fn, s))


# Finally, many forms of aggregation can be expressed as repeatedly applying
# a two-argument function to the reduced value so far and each element in turn.
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


from functools import reduce


def product(s):
    return reduce(mul, s)


print('product:', product([1, 2, 3, 4, 5]))

print(reduce(mul, [2, 4, 8], 1))
print(reduce(mul, [2, 4, 8], 10))


def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))


print('divisors of 12:', divisors_of(12))

from operator import add


def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n


print('perfect number 1 - 1000:', keep_if(perfect, range(1, 1000)))

print('你好')

city = 'Berkeley'
print('length of city:', len(city))
print('city[3]', city[3])

print("'here' in \"where's Simon\" =>", 'here' in "where's Simon")

# multiline literals
print("""The Zen of Python
claims, Readability counts.
Read more: import this.""")

print('The Zen of Python\nclaims, "Readability counts."\nRead more: import this.')

print(str(2) + ' is an element of ' + str(digits))