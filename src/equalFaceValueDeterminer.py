from abc import ABC, abstractmethod
from ranking import Ranking
from handValue import HandValue
from collections import Counter


class EqualFaceValueDeterminer(ABC):

    @abstractmethod
    def __init__(self):
        #self._amount_equal_face_value = Amount of elements to check
        #self._ranking = Rank of the combination
        self._next_determiner = None
        pass

    @staticmethod
    def _sort_hand(hand):
        hand.sort(key=lambda x: x.face_value.value, reverse=True)

    @staticmethod
    def _count_items(x, counter):
        return x, counter[x]

    @staticmethod
    def _ordered_set(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    @staticmethod
    def _add_cards_to_rest(rest_cards, card_value, amount_to_add):
        for y in range(0, amount_to_add):
            rest_cards.append(card_value[0])

    def _group_hand_by_value_repetition(self, hand):
        self._sort_hand(hand)
        face_values = list(map(lambda x: x.face_value, hand))
        unique_face_values = self._ordered_set(face_values)
        counter = Counter(face_values)
        return list(map(lambda x: self._count_items(x, counter), unique_face_values))

    def _get_combination(self, grouped_hand):
        rest_cards = []
        pair_found = False
        value = None
        for card_value in grouped_hand:
            amount = card_value[1]
            if not pair_found:
                if card_value[1] >= self._amount_equal_face_value:
                    pair_found = True
                    value = card_value[0]
                    amount = card_value[1] - self._amount_equal_face_value
            self._add_cards_to_rest(rest_cards, card_value, amount)
        return pair_found, value, rest_cards

    def determine(self, hand):

        grouped_hand = self._group_hand_by_value_repetition(hand)
        found, value, rest_cards = self._get_combination(grouped_hand)

        if found:
            return HandValue(self._ranking, value, rest_cards)
        if self._next_determiner is not None:
            return self._next_determiner.determine(hand)
        return HandValue(Ranking.HIGH_CARD, None, rest_cards)

class PairDeterminer(EqualFaceValueDeterminer):
    def __init__(self, next_determiner=None):
        self._amount_equal_face_value = 2
        self._ranking = Ranking.PAIR
        self._next_determiner = next_determiner


class ThreeOfAKindDeterminer(EqualFaceValueDeterminer):
    def __init__(self, next_determiner=None):
        self._amount_equal_face_value = 3
        self._ranking = Ranking.THREE_OF_A_KIND
        self._next_determiner = next_determiner


class FourOfAKindDeterminer(EqualFaceValueDeterminer):
    def __init__(self, next_determiner=None):
        self._amount_equal_face_value = 4
        self._ranking = Ranking.FOUR_OF_A_KIND
        self._next_determiner = next_determiner
