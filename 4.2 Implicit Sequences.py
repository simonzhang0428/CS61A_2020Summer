# lazy computation describes any program that delays the computation of a value until that value is needed.

# The iterator abstraction has two components: a mechanism for retrieving the next element in the sequence being
# processed and a mechanism for signaling that the end of the sequence has been reached and no further elements remain.

# The for statement in Python operates on iterators. Objects are iterable (an interface) if they have an __iter__
# method that returns an iterator. Iterable objects can be the value of the <expression> in the header of a for
# statement:
#
# for <name> in <expression>:
#     <suite>
# To execute a for statement, Python evaluates the header <expression>,
# which must yield an iterable value. Then, the iter function is applied to that value. Until a StopIteration
# exception is raised, Python repeatedly calls next on that iterator and binds the result to the <name> in the for
# statement. Then, it executes the <suite>.

class Stream:
    """A lazily computed linked list."""

    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))


s = Stream(1, lambda: Stream(2 + 3, lambda: Stream(9)))
print('s.first', s.first)
print('s.rest.first', s.rest.first)
print('s.rest', s.rest)


def integer_stream(first):
    def compute_rest():
        return integer_stream(first + 1)

    return Stream(first, compute_rest)


positives = integer_stream(1)
print('positives', positives)
print('positives.rest.first', positives.rest.first)
print('positives.rest.rest', positives.rest.rest)


def map_stream(fn, s):
    if s is Stream.empty:
        return s

    def compute_rest():
        return map_stream(fn, s.rest)

    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s):
    if s is Stream.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)

    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k - 1
    return first_k


s = integer_stream(3)
print('s', s)
m = map_stream(lambda x: x * x, s)
print('m', m)
print('first_k_as_list(m, 5)', first_k_as_list(m, 5))


def primes(pos_stream):
    def not_divible(x):
        return x % pos_stream.first != 0

    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))

    return Stream(pos_stream.first, compute_rest)


prime_numbers = primes(integer_stream(2))
print('first_k_as_list(prime_numbers, 7)', first_k_as_list(prime_numbers, 7))