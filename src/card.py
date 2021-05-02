class Card:
    def __init__(self, suit, face_value):
        self._suit = suit
        self._face_value = face_value

    @property
    def suit(self):
        return self._suit

    @property
    def face_value(self):
        return self._face_value
