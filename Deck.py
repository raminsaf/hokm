from Shuffle import RaminShuffler
from Suit import Suit
from Card import Card

class Deck:
  """Deck Interface/Abstract Base class:
  listing the methods Decks are expected to supply."""
  def __init__(self, cards, shuffler):
    self._cards = cards
    self._cards_dealt = []
    self._cards_remaining = cards[:]
    self._shuffler = shuffler

  # Deal these many cards
  def dealCards(self, count):
    cut = self._cards_remaining[:count]
    self._cards_remaining = self._cards_remaining[count:]
    self._cards_dealt.append(cut)
    return cut

  def shuffle(self):
    self._cards_remaining = self._shuffler.random_shuffle(self._cards_remaining)
  
  def getCards(self):
    return self._cards
  
  def getCardsRemaining(self):
    return self._cards_remaining
  
  def getCardsDealt(self):
    return self._cards_dealt
  
  def resetCards(self):
    self._cards_dealt = []
    self._cards_ramaining = cards[:]
  
  def printCut(self, cut):
    for card in cut:
      print card.toString() + ", ",
    print ""
  
  def printDeck(self):
    print "============ %d CARDS ============" % len(self._cards)
    self.printCut(self._cards_remaining)
    print "=================================="


class HokmDeckFactory(object):
  @staticmethod
  def getHokmDeck(shuffler):
    cards = [Card(suit, value) for suit in Suit.getSuits() for value in range(2,15)]
    return Deck(cards, shuffler)

deck = HokmDeckFactory.getHokmDeck(RaminShuffler())
deck.printDeck()
deck.shuffle()
deck.printDeck()
