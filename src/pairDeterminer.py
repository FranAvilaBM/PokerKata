from ranking import Ranking
from handValue import HandValue


class PairDeterminer:

    def determine(self, hand):
        # Sort by face value
        hand.sort(key=lambda x: x.face_value.value, reverse=True)
        face_value = ''
        # Check if pair
        for card in hand:
            if face_value == card.face_value:
                value = card.face_value
                return HandValue(Ranking.PAIR, value)
            else:
                face_value = card.face_value
        # Otherwise return high card
        return HandValue(Ranking.HIGH_CARD, None)
