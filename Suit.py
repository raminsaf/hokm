 # -*- coding: utf-8 -*-

class Suit:
  HEARTS   = 0
  SPADES   = 1
  DIAMONDS = 2
  CLUBS    = 3
  
  SYMBOLS = { HEARTS:"♥", SPADES:"♠", DIAMONDS:"♦", CLUBS:"♣" }
  NAMES = { HEARTS:"HEARTS", SPADES:"SPADES", DIAMONDS:"DIAMONDS", CLUBS:"CLUBS" }
  
  @staticmethod
  def getSuits():
    return [Suit.HEARTS, Suit.SPADES, Suit.DIAMONDS, Suit.CLUBS]

  @staticmethod
  def getSuitSymbol(suit):
    if suit not in Suit.SYMBOLS.keys():
      return "?"
    else:
      return Suit.SYMBOLS[suit]
    
  @staticmethod
  def getSuitName(suit):
    if suit not in Suit.NAMES.keys():
      return "WHAT?"
    else:
      return Suit.NAMES[suit]
    
