import random

def poker(hands):
  """Takes a list of poker hands and returns the winning hands"""
  return allmax(hands, key=hand_rank)

def allmax(hands, key=None):
  key = key or (lambda x : x)
  result, maxval = [], None
  for hand in hands:
    handval = key(hand)
    if not result or handval > maxval:
      result, maxval = [hand], handval
    elif handval == maxval:
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
  if flush:
    return (5, ranks)
  if straight:
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

def test():
  "Test cases for the functions in poker program."
  sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
  sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
  fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
  fh = "TD TC TH 7C 7D".split() # Full House
  ace_straight = ["AS", "2D", "3D", "4H", "5H"]
  assert card_ranks(sf1) == [10, 9, 8, 7, 6]
  assert card_ranks(fk) == [9, 9, 9, 9, 7]
  assert card_ranks(ace_straight) == [5, 4, 3, 2, 1]
  assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]

test()

mydeck = [r + s for r in '23456789TJQK' for s in 'SHDC']

def deal(numhands, n = 5, deck = mydeck):
  """ Deal numhands with n cards each using the deck """
  random.shuffle(deck)
  return [deck[i*n : n*(i+1)] for i in range (0, numhands)]

print deal(2)