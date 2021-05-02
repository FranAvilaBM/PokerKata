class HandValue:
    def __init__(self, rank, value):
        self._rank = rank
        self._value = value

    @property
    def rank(self):
        return self._rank

    @property
    def value(self):
        return self._value
