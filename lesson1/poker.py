import random

def poker(hands):
  """Takes a list of poker hands and returns the winning hands"""
  return allmax(hands, key=hand_rank)

def allmax(hands, key=None):
  key = key or (lambda x : x)
  result, maxval = [], None
  for hand in hands:
    xval = key(hand)
    if not result or xval > maxval:
      result, maxval = [hand], xval

    elif xval == maxval:
      result.append(hand)
  return result

def hand_rank(hand):
  """Takes a poker hand and returns its rank"""
  ranks = card_ranks(hand)
  if straight(ranks) and flush(hand):
    return (8, max(ranks))
  if kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  if kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  if flush(hand):
    return (5, ranks)
  if straight(ranks):
    return (4, max(ranks))
  if kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  if two_pair(ranks):
    return (2, two_pair(ranks), ranks)
  if kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  return (0, ranks)

def card_ranks(hand):
  """ Return the ranks corresponding to a hand"""
  ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
  ranks.sort(reverse = True)
  # Handle the case where Ace is part of a low straight, A2345
  return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def kind(count, ranks):
  for rank in ranks:
    if ranks.count(rank) == count:
      return rank

def straight(ranks):
  """ Return true if the ranks form a straight"""
  return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5;

def flush(hand):
  """ Return true if all the cards in the hand belong to a single suit"""
  suits = [s for r,s in hand]
  return len(set(suits)) == 1;

def two_pair(ranks):
  """ Return two pairs if present """
  high_pair = kind(2, ranks);
  low_pair = kind(2, sorted(ranks));
  if high_pair and high_pair != low_pair:
    return (high_pair, low_pair)
  return False;

hand_names = [
    "High card",
    "One pair",
    "Two pair",
    "Three of a kind",
    "Straight",
    "Flush",
    "Full house",
    "Four of a kind",
    "Straight flush",
  ]

mydeck = [r + s for r in '23456789TJQK' for s in 'SHDC']

def deal(numhands, n = 5, deck = mydeck):
  """ Deal numhands with n cards each using the deck """
  random.shuffle(deck)
  return [deck[n*i : n*(i+1)] for i in range (0, numhands)]

def hand_percentages(n = 700*1000):
  counts = [0] * 9;
  for i in range(n/10):
    for hand in deal(10):
      ranking = hand_rank(hand)[0]
      counts[ranking] += 1;
  for i in reversed(range(9)):
    print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n));

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    s3 = "TC JC QC KS AS".split() # 10-A straight
    tp = "5S 5D 9H 9C 6S".split() # two pair
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([s1, s2]) == [s2]
    assert poker([s1, tp]) == [s1]

    # assert hand_rank(sf) == (8, 10)
    # assert hand_rank(fk) == (7, 9, 7)
    # assert hand_rank(fh) == (6, 10, 7)
    # assert hand_rank(s1) == (4, 5)
    # assert hand_rank(s3) == (4, 14)

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]

    # Ace-high beats 7-high
    assert (card_ranks(['AS', '2C', '3D', '4H', '6S']) >
            card_ranks(['2D', '3S', '4C', '6H', '7D']))
    # 5-straight loses to 6-straight
    assert (card_ranks(['AS', '2C', '3D', '4H', '5S']) <
            card_ranks(['2D', '3S', '4C', '5H', '6D']))

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    return 'tests pass'

test()

hand_percentages()