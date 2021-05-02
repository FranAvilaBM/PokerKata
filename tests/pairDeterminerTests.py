from src.card import Card
from src.faceValue import FaceValue
from src.pairDeterminer import PairDeterminer
from src.suit import Suit
from src.ranking import Ranking

def _build_hand_with_pair():
    hand = [Card(Suit.HEARTS, FaceValue.ACE),
            Card(Suit.CLUBS, FaceValue.ACE),
            Card(Suit.HEARTS, FaceValue.TWO),
            Card(Suit.CLUBS, FaceValue.TWO),
            Card(Suit.HEARTS, FaceValue.FOUR)]
    return hand

def test_determine_given_hand_with_no_pair_should_return_None():
    hand = [Card(Suit.HEARTS, FaceValue.ACE),
            Card(Suit.CLUBS, FaceValue.TWO),
            Card(Suit.HEARTS, FaceValue.THREE),
            Card(Suit.HEARTS, FaceValue.FOUR),
            Card(Suit.HEARTS, FaceValue.SIX)]
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.rank.value == Ranking.HIGH_CARD.value
    assert result.value == None



def test_determine_given_hand_with_pair_should_return_pair_result():
    hand = _build_hand_with_pair()
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.rank.value == Ranking.PAIR.value

def test_determine_given_hand_with_pair_should_return_highest_pair_result():
    hand = _build_hand_with_pair()
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.value == FaceValue.ACE

def test_determine_given_hand_with_pair_should_return_highest_pair_result_and_rest():
    hand = _build_hand_with_pair()
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.rest == [FaceValue.FOUR, FaceValue.TWO, FaceValue.TWO]

def test_determine_given_hand_with_pair_should_return_pair_result_and_rest():
    hand = [Card(Suit.HEARTS, FaceValue.ACE),
            Card(Suit.HEARTS, FaceValue.THREE),
            Card(Suit.HEARTS, FaceValue.TWO),
            Card(Suit.CLUBS, FaceValue.TWO),
            Card(Suit.HEARTS, FaceValue.FOUR)]
    determiner = PairDeterminer()
    result = determiner.determine(hand)
    assert result.value == FaceValue.TWO
    assert result.rest == [FaceValue.ACE, FaceValue.FOUR, FaceValue.THREE]

