from operator import mul


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


# Tree
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.label)

    def __str__(self):
        def print_str(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + '\n'
            for b in t.branches:
                tree_str += print_str(b, indent + 1)
            return tree_str

        return print_str(self).rstrip()


t = Tree(3, [Tree(4), Tree(5)])
t.label = 5
print(t.label)


def make_even(t):
    """
    Define a function make even which takes in a tree t whose values are integers,
    and mutates the tree such that all the odd integers are increased by 1 and
    all the even integers remain the same.
    """
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)


t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
make_even(t)
print(t.label)
print(t.branches[0].branches[0].label)
print(t)


def square_tree(t):
    """Mutatea a Tree t by squaring all its elements."""
    t.label *= t.label
    for b in t.branches:
        square_tree(b)


square_tree(t)
print(t)


def find_path(t, entry):
    """
    Define the procedure find path that, given a Tree t and an entry,
    returns a list containing the nodes along the path required to get from the root of t to entry.
    If entry is not present in t, return False.
    Assume that the elements in t are unique. Find the path to an element.
    """
    if t.label == entry:
        return [entry]
    for b in t.branches:
        path = find_path(b, entry)
        if path:
            return [t.label] + path
    return False


tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
print(find_path(tree_ex, 5))


def average(t):
    """Return the average value of all the nodes in t."""

    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            b_total, b_count = sum_helper(b)
            total += b_total
            count += b_count
        return total, count

    total, count = sum_helper(t)
    return total / count


t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
print('average(t0):', average(t0))
t1 = Tree(8, [t0, Tree(4)])
print(average(t1))


def combine_tree(t1, t2, combiner):
    """
    Write a function that combines the values of two trees t1 and t2 together with the combiner function.
    Assume that t1 and t2 have identical structure. This function should return a new tree.
    Hint: consider using the zip() function, which returns an iterator of tuples
    where the first items of each iterable object passed in form the first tuple,
    the second items are paired together and form the second tuple, and so on and so forth.
    """
    combined = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)


a = Tree(1, [Tree(2, [Tree(3)])])
b = Tree(4, [Tree(5, [Tree(6)])])
combined = combine_tree(a, b, mul)
print(combined)


def alt_tree_map(t, map_fn):
    """given a function and a Tree, applies the function to all of the data
    at every other level of the tree, starting at the root.
    """
    def helper(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else:
            label = t.label
        branches = [helper(b, depth + 1) for b in t.branches]
        return Tree(label, branches)
    return helper(t, 0)


t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
negate = lambda x: -x
print(alt_tree_map(t, negate))
