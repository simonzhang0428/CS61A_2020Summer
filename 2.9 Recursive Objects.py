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


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n - m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return with_m + without_m

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, ' + '), lists)
    print(join_link(strings, '\n'))


print_partitions(6, 4)
