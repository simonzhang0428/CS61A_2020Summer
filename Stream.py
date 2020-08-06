class Stream:
    """A lazily computed linked list."""

    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
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
        return f'Stream({repr(self.first)}, <...>)'


s = Stream(1, lambda: Stream(2 + 3, lambda:Stream(9)))
print('s.first:', s.first)
print('s.rest:', s.rest)

def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)
    return Steam