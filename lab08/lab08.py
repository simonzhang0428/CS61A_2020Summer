def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    Write the generator function make_generators_generator, which takes a zero-argument generator function g and
    returns a generator that yields generators. For each element e yielded by the generator object returned by
    calling g, a new generator object is yielded that will generate entries 1 through e yielded by the generator
    returned by g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while i <= n:
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"

    def gen(i):
        for entry in g():
            if i <= 0:
                return
            yield entry
            i -= 1

    i = 1
    for entry in g():
        yield gen(i)
        i += 1


