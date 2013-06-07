from Shuffle import RaminShuffler
from Suit import Suit
from Card import Card

class Deck:
  """Deck Interface/Abstract Base class:
  listing the methods Decks are expected to supply."""
  def __init__(self, cards, shuffler):
    self._cards_dealt = []
    self._cards = cards[:]
    self._shuffler = shuffler

  # Deal these many cards
  def dealCards(self, count):
    cut = self._cards[:count]
    self._cards = self._cards[count:]
    self._cards_dealt.append(cut)
    return cut

  def shuffle(self):
    self._cards = self._shuffler.random_shuffle(self._cards)
  
  def getCards(self):
    return self._cards
  
  def getCardsDealt(self):
    return self._cards_dealt
  
  def resetCards(self):
    self._cards = self_cards + self._cards_dealt
    self._cards_dealt = []
  
  #TODO: Can this move somewhere else?
  def order(self):
    suitmap = { suit:[] for suit in Suit.getSuits() }
    for card in self._cards:
      suitmap[card.getSuit()].append(card)
    self._cards = []
    for suit in Suit.getSuits():
      self._cards += suitmap[suit]
  
  #TODO: Can this move somewhere else?
  def getCardsBySuit(self, suit):
    return [card for card in self._cards if card.getSuit() == suit]
  
  def printDeck(self):
    print "============ %d CARDS ============" % len(self._cards)
    for card in self._cards:
      print card.toString() + ", ",
    print ""
    print "=================================="

class Hand(Deck):
  pass
  
class HokmDeckFactory(object):
  @staticmethod
  def getHokmDeck(shuffler):
    cards = [Card(suit, value) for suit in Suit.getSuits() for value in range(2,15)]
    return Deck(cards, shuffler)

deck = HokmDeckFactory.getHokmDeck(RaminShuffler())
deck.printDeck()
deck.shuffle()
deck.printDeck()
hearts = deck.getCardsBySuit(Suit.HEARTS)
print "HEARTS: %d Cards" % len(hearts)
for card in hearts:
  card.printCard()
deck.order()
deck.printDeck()
