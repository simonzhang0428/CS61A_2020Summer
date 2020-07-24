class Link:
    """A linked list with a first element and the rest."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, item):
        if item == 0:
            return self.first
        else:
            return self.rest[item - 1]

    def __len__(self):
        return 1 + len(self.rest)


s = Link(3, Link(4, Link(5)))
print('len(s):', len(s))
print('s[1]:', s[1])


def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


print('link_expression(s):', link_expression(s))

Link.__repr__ = link_expression
print('s:', s)

s_first = Link(s, Link(6))
print('s_first:', s_first)
print('len(s_first):', len(s_first))
print('len(s_first[0]):', len(s_first[0]))
print('s_first[0][2]:', s_first[0][2])


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


print('extend_link(s, s):', extend_link(s, s))
Link.__add__ = extend_link
print('s + s:', s + s)


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def square(x):
    return x * x


print('map_link(square, s):', map_link(square, s))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


odd = lambda x: x % 2 == 1
print('map_link(square, filter_link(odd, s)):', map_link(square, filter_link(odd, s)))


def join_link(s, separator):
    if s is Link.empty:
        return ''
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


print('join_link(s, ', '):', join_link(s, ', '))


# def partitions(n, m):
#     """Return a linked list of partitions of n using parts of up to m.
#     Each partition is represented as a linked list.
#     """
#     if n == 0:
#         return Link(Link.empty)
#     elif n < 0 or m == 0:
#         return Link.empty
#     else:
#         using_m = partitions(n - m, m)
#         with_m = map_link(lambda s: Link(m, s), using_m)
#         without_m = partitions(n, m - 1)
#         return with_m + without_m
#
# def print_partitions(n, m):
#     lists = partitions(n, m)
#     strings = map_link(lambda s: join_link(s, ' + '), lists)
#     print(join_link(strings, '\n'))
#
#
# print_partitions(6, 4)

# Tree
class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.label)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, (left, right))


t = fib_tree(6)
print(t)


def sum_labels(t):
    return t.label + sum([sum_labels(b) for b in t.branches])


print('sum_labels(fib_tree(5)):', sum_labels(fib_tree(5)))


def leaves(t):
    """Return a list of leaf labels in Tree t."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


print('leaves(t):', leaves(t))


def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


print('height(t):', height(t))


# Sets
s = {3, 2, 1, 4, 4}
s2 = {5, 6}
s3 = {1, 2}
print('s3:', s3)
print('s2:', s2)
print('s:', s)
print('3 in s:', 3 in s)
print('len(s):', len(s))
print('s.union({1, 5}):', s.union({1, 5}))
print('s.intersection({6, 5, 4, 3}):', s.intersection({6, 5, 4, 3}))
print('s.isdisjoint(s2):', s.isdisjoint(s2))
print('s3.issubset(s):', s3.issubset(s))
print('s.issuperset(s3):', s.issuperset(s3))
s.update(s2)
print('s.update(s2), s:', s)
s.add(7)
print('s.add(7), s:', s)
s.remove(1)  # not find, KeyError
print('s.remove({1, 2}), s:', s)
s.discard(10)  # not find: OK
print('s.discard(10), s:', s)
print('s.pop():', s.pop())
print('s.pop():', s.pop())
print('s.pop():', s.pop())
print('s.pop():', s.pop())
print('s.pop():', s.pop())
print('s:', s)
s.clear()
print('s.clear(), s:', s)


def empty(s):
    return s is Link.empty


def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


s = Link(4, Link(1, Link(5)))
print('set_contains(s, 4):', set_contains(s, 4))


def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


print('s:', s)
t = adjoin_set(s, 2)
print('t = adjoin_set(s, 2), t:', t)


def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2."""
    return filter_link(lambda v: set_contains(set2, v), set1)


print('intersect_set(t, s):', intersect_set(t, s))


def union_set(set1, set2):
    set1_not_set2 = filter_link(lambda v: not set_contains(set2, v), set1)
    return extend_link(set1_not_set2, set2)


print('union_set(s, t):', union_set(s, t))


# if the set is ordered, we can improve as below:
def set_contains_improve(s, v):
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains_improve(s.rest, v)


def intersect_set_improve(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set_improve(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set_improve(set1.rest, set2)
        elif e2 < e1:
            return intersect_set_improve(set1, set2.rest)
