class Link:
    """A linked list with a first element and the rest."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

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


# str() is used to describe the object to the end user while
# repr() is mainly used for debugging and development.
# In addition, the print() function calls the str() function of the object,
# while simply calling the object in interactive mode calls the repr() function.

def sum_nums(lnk):
    if lnk == Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)


a = Link(1, Link(6, Link(7)))
print('sum_nums(a):', sum_nums(a))


def multiply_lnks(lst_of_lnks):
    """Return a new list whose elements are multiplied element-wise."""
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(p)


def filter_link(link, f):
    while link != Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


def filter_no_iter(link, f):
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


link = Link(1, Link(2, Link(3)))
g = filter_no_iter(link, lambda x: x % 2 == 0)
print('next(g):', next(g))
