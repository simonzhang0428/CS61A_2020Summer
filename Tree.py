# OOP Tree
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.label)

    def map(self, fn):
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, item):
        if self.label == item:
            return True
        else:
            for b in self.branches:
                if item in b:
                    return True
        return False

    def __str__(self):
        def print_str(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + '\n'
            for b in t.branches:
                tree_str += print_str(b, indent + 1)
            return tree_str

        return print_str(self).rstrip()


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, [left, right])


def sum_labels(t):
    return t.label + sum([sum_labels(b) for b in t.branches])


def leaves(t):
    """Return a list of leaf labels in Tree t."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
    return all_leaves


def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


def prune(t, n):
    """Remove subtrees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)


# Tree ADT using function and selector
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for b in branches:
        assert is_tree(b)
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_tree(t):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True


def is_leaf(t):
    return not branches(t)


def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes."""
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def fib_tree_ADT(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def leaves_ADT(tree):
    """Return a list containing the leaf labels of tree."""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])


t = fib_tree(6)
print(t)
print('leaves:', leaves(t))
print('sum_labels:', sum_labels(t))
print('height:', height(t))

t1 = Tree(5)
print(repr(t1))

t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
print(t)

t1.map(lambda x: x + 2)
t1.map(lambda x: x * 4)
print(t1.label)

print(t.branches[0].label)
print(t.branches[1].is_leaf())
print('3 in t:', 3 in t)
print('9 in t:', 9 in t)
