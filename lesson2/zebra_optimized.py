import itertools, time

def zebra_puzzle():
  """
  There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.
"""

  houses = first, _, middle, _,_ =[1 ,2 ,3 ,4 ,5]
  # Note the list here. We make a list of out of the permutations because
  # otherwise the for multiple for loops will go awry.
  orderings = list(itertools.permutations(houses))
  g = ((ZEBRA, WATER)
    for red, green, ivory, yellow, blue in c(orderings)
    if is_right_of(green, ivory)
    for Englishman, Spaniard, Ukrainian, Norwegian, Japanese in c(orderings)
    if Englishman is red
    if Norwegian is first
    if Norwegian is blue
    for tea, coffee, milk,orange,WATER in c(orderings)
    if milk is middle
    if coffee is green
    if Ukrainian is tea
    for dog, snails, fox, horse, ZEBRA in c(orderings)
    if dog is Spaniard
    for OldGoldSmoker, Kools, Chesterfields,LuckyStrike,parliaments in c(orderings)
    if is_next_to(Chesterfields, fox)
    if Kools is yellow
    if OldGoldSmoker is snails
    if is_next_to(Kools, horse)
    if LuckyStrike is orange
    if Japanese is parliaments
    )

  return next(g)

def is_next_to(a, b):
  """ Returns true if a and b are next to each other"""
  return abs(a - b) == 1

def is_right_of(a, b):
  """ Returnfs true if a is to the right of b """
  return a - b == 1

def c(sequence):
  c.starts += 1
  for item in sequence:
    c.items += 1
    yield item

def instrument_function(fn, *args):
  c.starts, c.items = 0, 0
  t0 = time.clock();
  result = fn(*args)
  t1 = time.clock()
  print ('%s got %s with %5d iters over %7d items and took time %6.4f seconds'
      %(fn.__name__, result, c.starts, c.items, t1 - t0))

instrument_function(zebra_puzzle)
