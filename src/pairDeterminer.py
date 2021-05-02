from ranking import Ranking
from handValue import HandValue


def _sort_hand(hand):
    hand.sort(key=lambda x: x.face_value.value, reverse=True)


class PairDeterminer:

    def determine(self, hand):
        _sort_hand(hand)
        face_value = ''
        rest_cards = []
        pair_found = False
        previous_card_face_value = None
        value = None
        # Check if pair
        for card in hand:
            if not pair_found:
                if face_value == card.face_value:
                    pair_found = True
                    value = card.face_value
                else:
                    face_value = card.face_value
                    if previous_card_face_value:
                        rest_cards.append(previous_card_face_value)
                    previous_card_face_value = card.face_value
            else:
                rest_cards.append(card.face_value)
        if pair_found:
            return HandValue(Ranking.PAIR, value, rest_cards)
        return HandValue(Ranking.HIGH_CARD, None, None)
