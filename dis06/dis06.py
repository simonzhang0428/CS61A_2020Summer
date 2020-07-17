def stepper(n):
    def step():
        nonlocal n
        n += 1
        return n

    return step


step1 = stepper(10)
print('step1():', step1())
print('step1():', step1())
print('step1():', step1())
step2 = stepper(10)
print('step2():', step2())


def memory(n):
    """Return function which take a function that used to update N.
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def f(fn):
        nonlocal n
        return fn(n)

    return f


from operator import add

six = 1


def ty(one, a):
    summer = one(a, six)
    return summer


six = ty(add, 6)
summer = ty(add, 6)


def nonlocalist():
    """prepend and get, which represent the “add to front of list”
    and “get the ith item” operations, respectively.
    """
    get = lambda x: "Index out of range!"

    def prepend(value):
        nonlocal get
        f = get

        def get(i):
            if i == 0:
                return value

            return f(i - 1)

    return prepend, lambda x: get(x)


prepend, get = nonlocalist()
prepend(2)
prepend(3)
prepend(4)
print(get(0))
print(get(1))
print(get(2))

square = lambda x: x * x
double = lambda x: 2 * x


def memory(x, f):
    """Return a higher-order function that prints its memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """

    def g(h):
        print(f(x))
        return memory(x, h)

    return g


# def announce_losses(who, last_score=0): """
#     >>> f = announce_losses(0)
#     >>> f1 = f(10, 0)
#     >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
#     Oh no! Player 0 just lost 9 point(s).
#     >>> f3 = f2(7, 10)
#     >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
#     >>> f5 = f4(11, 12)
#     """
#
#
#     assert who == 0 or who == 1, 'The who argument should indicate a player.'
#
#
#     def say(score0, score1):
#         if who == 0:
#             score = score0
#         elif who == 1:
#             score = score1
#         if score0 < last_score:
#             print("Oh no! Player", who, "just lost", last_score - score, "point(s).")
#         return announce_losses(who, score)
#
#
#     return say


def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """

    def repeat(k):
        nonlocal num, middle
        if k == 1:
            return middle
        return middle + '-' + repeat(k - 1)

    return start + '-' + repeat(num) + '-' + end


def primary_stress(t):
    """
    >>> word = tree("", [
            tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),
            tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [
                tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),
    tree("w", [tree("requirement")])]) >>> primary_stress(phrase)
    'law'
    """

    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in braches(t)],
                   key=lambda a: a[1])

    return helper(t, 0)[0]


def subset_sum(seq, k):
    if len(seq) == 0:
        return False
    elif k in seq:
        return True
    else:
        included = subset_sum(seq[1:], k-seq[0])
        excluded = subset_sum(seq[1:], k)
        return included or excluded

print(subset_sum([2, 4, 7, 3], 5))
print(subset_sum([1, 9, 5, 7, 3], 2))
print(subset_sum([1, 1, 5, -1], 3))