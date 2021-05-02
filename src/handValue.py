class HandValue:

    def __init__(self, rank, value, rest):
        self._rank = rank
        self._value = value
        self._rest = rest

    @property
    def rank(self):
        return self._rank

    @property
    def value(self):
        return self._value

    @property
    def rest(self):
        return self._rest
