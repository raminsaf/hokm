

class Player():
  def __init__(self, name):
    self._name = name
    self._hand = Hand()

  def pickHokm(self):
    raise NotImplementedError( "Should have implemented this" )
  
  def resetDast(self):
    self._hand = Hand()
  
  def play(self, cards_on_the_table = []):
    raise NotImplementedError( "Should have implemented this" )
   
class RobotPlayer(Player):
  def __init__(self, name):
    #TODO: Call parent constructor instead of duplication
    self._name = name
    self._hand = Hand()

  def pickHokm(self):
    # AI Hokm Picking Logic:
    # 1. Three of a suit wins at all times (one could argue the total matters more, I disagree but could be persuaded)
    # 2. Two of a suit wins if total points are above 15 (At least 15, one could argue for as low as 10 or as high as 20...)
    # 3. Vasat 
    options = { '1':Suit.HEARTS, '2':Suit.SPADES, '3':Suit.DIAMONDS, '4':Suit.CLUBS, '5':Hokm.VASAT,\
    '6':Hokm.HASHTOM, '7':Hokm.YAZDAHOM }
    print "HELLO HAKEM %s \nYOUR MAJESTY'S DAST: %s\n" % (self._name, self._hand.toString())
    number_of_cards_per_suit = self._hand.getNumberOfCardsPerSuit()
    total_value_per_suit = self._hand.getTotalValuePerSuit()
    cards = self._hand.getCardsPerSuit()
    twos = [] #Suits with two cards
    hokm = Hokm.VASAT
    for suit in Suit.getSuits():
      if number_of_cards_per_suit[suit] >= 3:
        print "Found three or more cards in suit %s, hokm it..." % Suit.getSuitName(suit)
        hokm = suit
      elif number_of_cards_per_suit[suit] == 2:
        print "Found two cards in suit %s, looking into it..." % Suit.getSuitName(suit)
        twos.append(suit)

    # when we get here if hokm is not vasat we have a winner
    if Hokm.VASAT != hokm:
      #print a warning here for a weak three against a strong two
      for two in twos:
        if total_value_per_suit[two] > (2 * total_value_per_suit[hokm]):
          print "Your TWO looks great too: (%s) " % Suit.getSuitName(two)
        else:
          print "Your TWO will be overlooked (not great) (%s) " % Suit.getSuitName(two)
      print (self._hand.getHighestCardForSuit(hokm).printCard())
      return hokm
    
    # by now we have to pick a strong (loose definition > 15) two or vasat
    # there might be more than one strong twos
    for two in twos:
      if total_value_per_suit[two] > 15:
        # VASAT means first acceptable two carder, anything else is the second possibility
        if hokm == Hokm.VASAT or total_value_per_suit[two] >= total_value_per_suit[hokm]:
          print("Picking TWO for hokm: (%s) " % Suit.getSuitName(two))
          hokm = two
    
    # by now either we have a hokm, or we will go VASAT (already initialized)
    print("HOKM IS %s" % Hokm.getHokmSymbol(hokm))
    print (self._hand.getHighestCardForSuit(hokm).printCard())
    return hokm
   
class HumanPlayer(Player):
  def __init__(self, name):
    #TODO: Call parent constructor instead of duplication
    self._name = name
    self._hand = Hand()
  
  def pickHokm(self):
    options = { '1':Suit.HEARTS, '2':Suit.SPADES, '3':Suit.DIAMONDS, '4':Suit.CLUBS, '5':Hokm.VASAT,\
    '6':Hokm.HASHTOM, '7':Hokm.YAZDAHOM }
    print("HELLO HAKEM %s \nYOUR MAJESTY'S DAST: %s\n" % (self._name, self._hand.toString()))
    var = ""
    while var not in options.keys():
      var = input("HOKM (PICK THE TRUMP SUIT) :\n 1. Hearts\n 2. Spades\n 3. Diamonds\n 4. Clubs\n 5. Vasateh Yar\n"\
      " 6. Hashtomeh Khodam\n 7. Yazdahomeh Khodam\n")
    hokm = options[var]
    print("HOKM IS %s" % Hokm.getHokmSymbol(hokm))
    return hokm
