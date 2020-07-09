from operator import mul, getitem

digits = [1, 8, 2, 8]
print('digits:', digits)
print('length:', len(digits))
print('digits[3]:', digits[3])
print('digits[-1]', digits[-1])
print('getitem(digits, 3) =>', getitem(digits, 3))

print('digits[0:2]', digits[0:2])
print('digits[1:]', digits[1:])
print('digits[:-1]', digits[:-1])

lst = [2, 7] + digits * 2
print(lst)

pairs = [[10, 20], [30, 40]]
print('pairs[1]:', pairs[1])
print('pairs[1][0]:', pairs[1][0])
print('5 in digits =>', 5 in digits)


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        element = s[index]
        if element == value:
            total += 1
        index += 1
    return total


print('how many 8 in digits: ', count(digits, 8))


def count2(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total


print('how many 8 in digits: ', count2(digits, 8))

# A for statement consists of a single clause with the form:
#
# for <name> in <expression>:
#     <suite>
# A for statement is executed by the following procedure:
#
# Evaluate the header <expression>, which must yield an iterable value.(a sequence)
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


def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total


print('sum_below(5) =>', sum_below(5))

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

# Strings #
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


# Trees A tree has a root label and a sequence of branches.
# Each branch of a tree is a tree. A tree with no branches is called a leaf.
# Any tree contained within a tree is called a sub-tree of that tree (such as a branch of a branch).
# The root of each sub-tree of a tree is called a node in that tree.
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees.'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print('tree =>', t)
print('root =>', label(t))
print('branch =>', branches(t))
print('is_leaf(t) =>', is_leaf(t))
print('is_leaf(branches(t)[0]) =>', is_leaf(branches(t)[0]))


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


print('fib_tree(4) =>', fib_tree(4))


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


print('count_leaves(fib_tree(5)) =>', count_leaves(fib_tree(5)))

def leaves(tree):
    """Return a list containing the leaf labels of tree."""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

print('leaves(fib_tree(4)) =>', leaves(fib_tree(4)))

def increment_leaves(t):
    """Return a tree like t but with leaf labels invremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

print('increment_leaves(fib_tree(4)) ->', increment_leaves(fib_tree(4)))

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    #  when reach enpty list, assume base case, stop there.

print('increment(fib_tree(4)) =>', increment(fib_tree(4)))

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

print_tree(fib_tree(4))

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


print('partition_tree(2, 2) =>', partition_tree(2, 2))


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


print_parts(partition_tree(6, 4))

def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))


def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), right_binarize(rest)]
    else:
        return [right_binarize(b) for b in bs]


print(right_binarize(tree(0, [tree(x) for x in [1, 2, 3, 4, 5, 6, 7]])))

# Linked list
empty = 'empty'
def is_link(s):
    """S is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list."""
    assert is_link(s), 'fist only applies to a linked list.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list."""
    assert is_link(s), 'rest only applies to a linked list.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

four = link(1, link(2, link(3, link(4, empty))))
print('four ->', four)
print('first(four) ->', first(four))
print('rest(four) ->', rest(four))

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at the index i."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

print('len_link(four) -> ', len_link(four))
print('getitem_link(four, 1) ->', getitem_link(four, 1))

def len_link_recursive(s):
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

print('len_link_recursive(four) ->', len_link_recursive(four))
print('getitem_link_recursive(four, 1) ->', getitem_link_recursive(four, 1))

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

print('extend_link(four, four) ->', extend_link(four, four))

def apply_to_all_link(f, s):
    """Applu f to each element of s."""
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

print('apply_to_all_link(lambda x: x*x, four) ->', apply_to_all_link(lambda x: x*x, four))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

print('keep_if_link(lambda x: x%2 == 0, four) ->', keep_if_link(lambda x: x%2 == 0, four))

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

print('join_link(four, \',\') ->', join_link(four, ','))

def partitions(n, m):
    """Return a linked list of partition of n using parts up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, ' + '), lists)
    print(join_link(strings, '\n'))

print_partitions(6, 4)