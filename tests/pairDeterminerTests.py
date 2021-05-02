from src.card import Card
from src.faceValue import FaceValue
from src.pairDeterminer import PairDeterminer
from src.suit import Suit
from src.ranking import Ranking

def test_determine_given_hand_with_no_pair_should_return_None():
    hand = [Card(Suit.HEARTS, FaceValue.ACE),
            Card(Suit.CLUBS, FaceValue.TWO),
            Card(Suit.HEARTS, FaceValue.THREE),
            Card(Suit.HEARTS, FaceValue.FOUR),
            Card(Suit.HEARTS, FaceValue.SIX)]
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.rank.value == Ranking.HIGH_CARD.value


def test_determine_given_hand_with_pair_should_return_pair_result():
    hand = [Card(Suit.HEARTS, FaceValue.ACE),
            Card(Suit.CLUBS, FaceValue.ACE),
            Card(Suit.HEARTS, FaceValue.TWO),
            Card(Suit.HEARTS, FaceValue.THREE),
            Card(Suit.HEARTS, FaceValue.FOUR)]
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.rank == Ranking.PAIR
