import random

class Shuffler(object):
  def random_shuffle(self, cards, times = 1):
    raise NotImplementedError( "Should have implemented this" )

  def shuffleAt(self, cards, cuttingPoint):
    raise NotImplementedError( "Should have implemented this" )

  def shuffle(self, cards):
    raise NotImplementedError( "Should have implemented this" )

class RaminShuffler(Shuffler):
  def __init__(self):
    pass
  
  def shuffle(self, cards):
    return self.shuffleAt(cards, len(cards) // 2)

  def random_shuffle(self, cards, times = 10):
    size = len(cards)
    low = size//2 - size//4
    hi = size//2 + size//4
    while times > 0:
      times = times - 1
      cut = random.randrange(low,hi)
      if cut > size:
        cut = size//2
      cards = self.shuffleAt(cards, cut)
    return cards

  def shuffleAt(self, cards, cut):
    print("CUTTING AT CARD %s" % cut)
    cut_1 = cards[cut:]  
    cut_2 = cards[:cut]
    outcards = [] 
    while len(cut_1) > 0 and len(cut_2) > 0:
      outcards.append(cut_1[0])
      outcards.append(cut_2[0])
      cut_1.remove(cut_1[0])
      cut_2.remove(cut_2[0])
    #print("EXITING THE LOOP cut_1 or cut_2 should be empty, joining with both")
    outcards += cut_1
    outcards += cut_2
    #print("NOW CUT IN HALF")
    cut = len(cards) // 2
    cut_1 = outcards[cut:]  
    cut_2 = outcards[:cut]
    outcards = cut_1 + cut_2
    return outcards

