def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """

    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'deposit':
            balance += amount
            return balance
        elif message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        else:
            return 'Invalid message'

    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    count = 0
    wrong_password = []

    def withdraw(amount, try_password):
        nonlocal balance, password, count, wrong_password
        if count >= 3:
            return f'Too many incorrect attempts. Attempts: {wrong_password}'
        elif try_password != password:
            count += 1
            wrong_password.append(try_password)
            return 'Incorrect password'
        elif try_password == password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance

    return withdraw


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst, 2)
    9
    >>> lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 0
    prev = next(t)
    while count < k - 1:
        curr = next(t)
        if prev == curr:
            count += 1
        else:
            count = 0
        prev = curr
    return prev
    # def repeated_helper(t, k, prev, n):
    #     if k == 1:
    #         return prev
    #     nex = next(t)
    #     if nex == prev:
    #         return repeated_helper(t, k - 1, nex, n)
    #     else:
    #         return repeated_helper(t, n, nex, n)
    #
    # return repeated_helper(t, k, next(t), k)


def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    "*** YOUR CODE HERE ***"
    while (next_a is not None) or (next_b is not None):
        if next_a is None:
            yield next_b
            next_b = next(iter_b, None)
        elif next_b is None:
            yield next_a
            next_a = next(iter_a, None)
        elif next_a == next_b:
            yield next_b
            next_a, next_b = next(iter_a, None), next(iter_b, None)
        elif next_a < next_b:
            yield next_a
            next_a = next(iter_a, None)
        elif next_a > next_b:
            yield next_b
            next_b = next(iter_b, None)


# Extra Questions
def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    error = withdraw(0, old_pass)
    if type(error) == str:
        return error

    def joint(amount, attempt):
        if attempt == new_pass:
            return withdraw(amount, old_pass)
        else:
            return withdraw(amount, attempt)

    return joint


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"

    def generator(n):
        while True:
            yield n
            n = m + n

    return generator


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
