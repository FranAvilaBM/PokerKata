from ranking import Ranking
from handValue import HandValue
from collections import Counter


def _sort_hand(hand):
    hand.sort(key=lambda x: x.face_value.value, reverse=True)

def _count_items(x, counter):
    return (x, counter[x])

def _orderedSet(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

class PairDeterminer:

    def determine(self, hand):
        _sort_hand(hand)

        rest_cards = []
        pair_found = False
        value = None

        l = list(map(lambda x: x.face_value, hand))
        s = _orderedSet(l)
        c = Counter(l)
        l2 = list(map(lambda x: _count_items(x, c), s))

        for x in l2:
            if not pair_found:
                if x[1] >= 2:
                    pair_found = True
                    value = x[0]
                    for y in range(0, x[1]-2):
                        rest_cards.append(x[0])
                else:
                    for y in range(0, x[1]):
                        rest_cards.append(x[0])
            else:
                for y in range(0, x[1]):
                    rest_cards.append(x[0])

        if pair_found:
            return HandValue(Ranking.PAIR, value, rest_cards)
        return HandValue(Ranking.HIGH_CARD, None, None)
