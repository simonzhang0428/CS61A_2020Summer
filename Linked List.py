# OOP Link
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

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link({0}{1})'.format(self.first, rest_repr)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __add__(self, other):
        if self is Link.empty:
            return other
        else:
            return Link(self.first, Link.__add__(self.rest, other))


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def join_link(s, separator):
    if s is Link.empty:
        return ''
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


def add(s, v):
    """
    Add v to an ordered list s with no repeats, returning modified s.
    If v is already in s, then don't modify s, but still return it.
    """
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


# Linked list ADT
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


print('apply_to_all_link(lambda x: x*x, four) ->', apply_to_all_link(lambda x: x * x, four))


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


print('keep_if_link(lambda x: x%2 == 0, four) ->', keep_if_link(lambda x: x % 2 == 0, four))


def join_link_ADT(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link_ADT(rest(s), separator)


print('join_link(four, \',\') ->', join_link_ADT(four, ','))

s = Link(3, Link(4, Link(5)))
print(s)
print(s + s)
