import itertools

def floor_puzzle():
  floors = bottom,_,middle,_,top = [1,2,3,4,5]
  g = ((Hooper,Kay,Liskov,Perlis,Ritchie)
    for Hooper,Kay,Liskov,Perlis,Ritchie in itertools.permutations(floors)
    if Hooper is not top
    if Kay is not bottom
    if Liskov is not top and Liskov is not bottom
    if Perlis > Kay
    if not isadjacent(Ritchie, Liskov)
    if not isadjacent(Liskov, Kay)
    )
  return next(g)

def isadjacent(a, b):
  return abs(a - b) == 1

print floor_puzzle()