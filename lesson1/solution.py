import random,itertools

def poker(hands):
  """Takes a list of poker hands and returns the winning hands"""
  return allmax(hands, key=hand_rank)

def best_hand(hand):
  """ Takes a single hand with 5 or more cards and returns the best possible
  5 card hand.
  """
  return max(itertools.combinations(hand, 5), key=hand_rank)

def best_wild_hand(hand):
  best_hands = set(best_hand(i) for i in itertools.product(*map(replacement, hand)))
  return max(best_hands, key=hand_rank)

def replacement(replace):
  allblack = [r + s for r in '23456789TJQKA' for s in 'CS']
  allred = [r + s for r in '23456789TJQKA' for s in 'DH']
  return (allblack if replace == '?B' else
    allred if replace == '?R' else
    [replace])

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
  groups = group(ranks)
  counts, ranks = unzip(groups)

  straight = (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
  suits = [s for r,s in hand]
  flush = len(set(suits)) == 1;

  return (8 if straight and flush else
     7 if (4, 1) == counts else
     6 if (3, 2) == counts else
     5 if flush else
     4 if straight else
     3 if (3, 1, 1) == counts else
     2 if (2, 2, 1) == counts else
     1 if (2, 1, 1, 1) == counts else
     0), ranks

def group(items):
  """Return a list of [(count, x)...] highest count first, then highest x"""
  groups = [(items.count(x), x) for x in set(items)]
  groups.sort(reverse = True)
  return groups

def unzip(pairs):
  """ Takes a list of pairs and converts them into a pair of lists
  For example [(3, 13), (2, 14), (1, 15)] is returned as
  ([3,2,1], [13,14,15])
  """
  return zip(*pairs)

def card_ranks(hand):
  """ Return the ranks corresponding to a hand"""
  ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
  ranks.sort(reverse = True)
  # Handle the case where Ace is part of a low straight, A2345
  return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def test_best_hand():
    "Test cases for the functions in solutions program"
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("TD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'TD'])
    return 'best hand tests pass'

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

print test_best_hand()
print test_best_wild_hand()