# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


# begin discussion #
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])
    # return 1 + max([0] + [height(branch) for branch in branches(t)])


def square_tree(t):
    """Return a tree with the square of every elements in t."""
    sq_branched = [square_tree(branch) for branch in branches(t)]
    return tree(label(t) ** 2, sq_branched)


numbers = tree(1, [tree(2,
                        [tree(3),
                         tree(4)]),
                   tree(5,
                        [tree(6,
                              [tree(7)]),
                         tree(8)])])
print_tree(numbers)
print_tree(square_tree(numbers))


def find_path(t, x):
    """Return path list from root to X.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # return None
    """
    if label(t) == x:
        return [label(t)]
    paths = [find_path(b, x) for b in branches(t)]
    for path in paths:
        if path:
            return [label(t)] + path


t = tree(1, [tree(2), tree(3)])
print('label(t) ->', label(t))
print('branches(tree(2, tree(t, [])))[0] ->', branches(tree(2, tree(t, [])))[0])

# mutation
pizza = ['cheese', 'mushroom']

# 1. append(el): Adds el to the end of the list, and returns None
# 2. extend(lst): Extends the list by concatenating it with lst, and returns None
# 3. insert(i, el): Insert el at index i (does not replace element but adds a new one), and returns None
# 4. remove(el): Removes the first occurrence of el in list, otherwise errors, and returns None
# 5. pop(i): Removes and returns the element at index i
lst1 = [1, 2, 3]
lst2 = lst1
print('lst2 is lst1:', lst2 is lst1)
lst2.extend([5, 6])
print('lst1[4]:', lst1[4])
lst1.append([-1, 0, 1])
print('-1 in lst1:', -1 in lst1)
print('lst2[5]:', lst2[5])
lst3 = lst2[:]  # Slicing a list creates a new list and leaves the original list unchanged.
lst3.insert(3, lst2.pop(3))
print('len(lst1):', len(lst1))
print('lst1[4] is lst3[6]:', lst1[4] is lst3[6])
print('lst3[lst2[4][1]]:', lst3[lst2[4][1]])
print('lst1[:3] is lst2[:3]:', lst1[:3] is lst2[:3])
print('lst1[:3] == lst2[:3]:', lst1[:3] == lst2[:3])

x = (1, 2, [4, 5, 6])
print('x:', x)
# x[2] = [3, 5, 6]
x[2][0] = 3
print('x:', x)


def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    times = lst.count(x)
    return lst.extend([el] * times)


def group_by(s, fn):
    """The values of the dictionary are lists of elements from s.
    Each element e in a list should be constructed such that fn(e) is the same
    for all elements in that list. Finally, the key for each value should be fn(e).

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    result = {}
    for el in s:
        key = fn(el)
        if key not in result:
            result[key] = [el]
        else:
            result[key] += [el]
    return result

    # result = {}
    # for el in s:
    #     key = fn(el)
    #     if key in result:
    #         result[key].append(el)
    #     else:
    #         result[key] = [el]
    # return result


def partition_options(total, biggest):
    """Outputs all the ways to partition a number
    total using numbers no larger than biggest.

    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total - biggest, biggest)
        without_biggest = partition_options(total, biggest - 1)
        with_biggest = [[biggest] + elem for elem in with_biggest]
        return with_biggest + without_biggest


def min_elements(T, lst):
    """Return the minimum number of elements from the list that need to be summed in order to add up to T.
    The same element can be used multiple times in the sum.
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    if T == 0:
        return 0
    else:
        return min([1 + min_elements(T - i, lst) for i in lst if T - i >= 0])

