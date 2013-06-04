from Suit import Suit

class Card:
  def __init__(self, suit, value):
    self._suit = suit
    self._value = value
  
  def getValue(self):
    return self._value
  
  def getName(self):
    special = {1:'A', 14:'A', 11:'J', 12:'Q', 13:'K'}
    if self._value in special.keys():
      return special[self._value]
    else:
      return str(self._value)
    
  def getSuit(self):
    return self._suit
    
  def toString(self):
    return Suit.getSuitSymbol(self._suit) + self.getName()
  
  def printCard(self):
    print self.toString()


