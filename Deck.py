from Shuffle import RaminShuffler
from Suit import Suit
from Card import Card

class Deck(object):
  """Deck Interface/Abstract Base class:
  listing the methods Decks are expected to supply."""
  def __init__(self, cards):
    self._cards_dealt = []
    self._cards = cards[:]

  # Deal these many cards
  def dealCards(self, count):
    cut = self._cards[:count]
    self._cards = self._cards[count:]
    self._cards_dealt += cut
    return cut

  # Deal this card
  def dealCard(self, card):
    if card in self._cards:
      self._cards.remove(card)
      self._cards_dealt.append(card)
    return card

  def shuffle(self, shuffler):
    self._cards = shuffler.random_shuffle(self._cards)

  def getCards(self):
    return self._cards
  
  def getCardsDealt(self):
    return self._cards_dealt
  
  def reset(self):
    self._cards += self._cards_dealt
    self._cards_dealt = []
    self.order()
  
  #TODO: Can this move somewhere else?
  def order(self):
    suitmap = { suit:[] for suit in Suit.getSuits() }
    for card in self._cards:
      suitmap[card.getSuit()].append(card)
    self._cards = []
    for suit in Suit.getSuits():
      self._cards += sorted(suitmap[suit], key = lambda x: x.getValue(), reverse = True)
  
  #TODO: Can this move somewhere else?
  def getCardsBySuit(self, suit):
    return sorted([card for card in self._cards if card.getSuit() == suit], key = lambda x: x.getValue(), reverse = True)
  
  def printCards(self):
    print "============ %d CARDS ============" % len(self._cards)
    for card in self._cards:
      print card.toString() + ", ",
    print ""
    print "=================================="

class Hand(Deck):
  def __init__(self, cards = []):
    super(Hand, self).__init__(cards)
  
  def getAllSuitValues(self):
    suitmap = {}
    for suit in Suit.getSuits():
      suitmap[suit] = self.getSuitValue(suit)
    return suitmap

  def getSuitValue(self, suit):
    return sum(card.getValue() for card in self._cards if card.getSuit() == suit)

  def getHighestCardForSuit(self, suit):
    return max(self.getCardsBySuit(suit), key=lambda card: card.getValue())

  def addCards(self, cards):
    for card in cards:
      print "ADDING CARD ",
      card.printCard()
      print ""
    self._cards += cards

  def toString(self):
    ret = ""
    for suit in Suit.getSuits():
      for card in suit:
        ret = ret + card.toString()
    return ret

  
class HokmDeckFactory(object):
  @staticmethod
  def getHokmDeck():
    cards = [Card(suit, value) for suit in Suit.getSuits() for value in range(2,15)]
    return Deck(cards)

deck = HokmDeckFactory.getHokmDeck()
deck.printCards()
deck.shuffle(RaminShuffler())
deck.printCards()
hearts = deck.getCardsBySuit(Suit.HEARTS)
print "HEARTS: %d Cards" % len(hearts)
for card in hearts:
  print card.toString(), 
print ""
deck.order()
deck.printCards()
deck.dealCards(50)
deck.printCards()
tmp = deck.getCards()[0]
deck.dealCard(tmp)
deck.printCards()
deck.reset()
deck.printCards()
print "================================"
hand = Hand(deck.dealCards(3))
deck.shuffle(RaminShuffler())
hand.addCards(deck.dealCards(2))
hand.printCards()
print hand.getAllSuitValues()
print hand.getSuitValue(Suit.HEARTS)
print hand.getSuitValue(Suit.CLUBS)
hand.getHighestCardForSuit(Suit.HEARTS).printCard()
