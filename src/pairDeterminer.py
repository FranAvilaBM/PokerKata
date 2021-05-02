from ranking import Ranking
from handValue import HandValue
from collections import Counter




class PairDeterminer:

    def __init__(self):
        self._cards_in_a_pair = 2

    def _sort_hand(self, hand):
        hand.sort(key=lambda x: x.face_value.value, reverse=True)

    def _count_items(self, x, counter):
        return (x, counter[x])

    def _orderedSet(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    def _group_hand_by_value_repetition(self, hand):
        self._sort_hand(hand)
        face_values = list(map(lambda x: x.face_value, hand))
        unique_face_values = self._orderedSet(face_values)
        counter = Counter(face_values)
        return list(map(lambda x: self._count_items(x, counter), unique_face_values))

    def _add_cards_to_rest(self, rest_cards, card_value, amount_to_add):
        for y in range(0, amount_to_add):
            rest_cards.append(card_value[0])

    def determine(self, hand):
        rest_cards = []
        pair_found = False
        value = None

        grouped_hand = self._group_hand_by_value_repetition(hand)

        for card_value in grouped_hand:
            amount = card_value[1]
            if not pair_found:
                if card_value[1] >= self._cards_in_a_pair:
                    pair_found = True
                    value = card_value[0]
                    amount = card_value[1]-self._cards_in_a_pair
            self._add_cards_to_rest(rest_cards, card_value, amount)

        if pair_found:
            return HandValue(Ranking.PAIR, value, rest_cards)
        return HandValue(Ranking.HIGH_CARD, grouped_hand[0][0], rest_cards)


