from ranking import Ranking
from handValue import HandValue


class PairDeterminer:

    def determine(self, hand):
        return HandValue(Ranking.HIGH_CARD, None)
