def multiply(m, n):
    """Multiply M by N.

    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def is_prime(n):
    """Return True if N is prime number.

    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)

    return prime_helper(2)


def count_stair_ways(n):
    """Count the ways if you only can take 1 or 2 step per time."""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """Take up to K step one time, Count all the ways.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total


a = [1, 5, 4, [2, 3], 3]
print('a ->', a)
print('a[0], a[-1] ->', a[0], a[-1])
print('len(a) ->', len(a))
print('2 in a ->', 2 in a)
print('4 in a ->', 4 in a)
print('a[3][0] ->', a[3][0])


def even_weighted(s):
    """Return even-indexed elements of S and multiply them by their corresponding index.
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # return [x * (x-1) for x in s if x % 2 == 1]
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive elements of S.
    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    # if s == []:
    #     return 1
    # elif s[0] in s[2:]:
    #     products = [s[0] ** s.count(s[0])]
    # else:
    #     products = [s[0] * max(s[2:])]
    # return max(products)
    if s == []:
        return 1
    # elif len(s) == 1:
    #     return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))


def check_hole_number(n):
    """A hole number is a number in which every other digit dips below the digits immediately adjacent to it.

    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n // 10 == 0:
        return True

    # The \ symbol just allows me to continue this line of code on a new line.
    # It's only included to make sure all the code stays on the page
    return ((n // 10) % 10) < (n % 10) and ((n // 10) % 10) < ((n // 100) % 10) \
           and check_hole_number(n // 100)

def check_mountain_number(n):
    """A mountain number is a number that either
    i. has digits that strictly decrease from right to left OR strictly increase from right to left
    ii. has digits that increase from right to left up to some point in the middle of the number
    (not necessarily the exact middle digit). After reaching the maximum digit,
    the digits to the left of the maximum digit should strictly decrease.

    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(x, is_incresing):
        if x // 10 == 0:
            return True
        if is_incresing and (x % 10) < ((x // 10) % 10):
            return helper(x // 10, is_incresing)
        return (x % 10) > ((x // 10) % 10) and helper(x // 10, False)
    return helper(n, True)