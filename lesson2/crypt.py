from __future__ import division
import itertools, re, string, time

def solve(formula):
  """ Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
  For example 655+655 = 1310
  """
  for answer in fill_in_formula(formula):
    if valid(answer):
      return answer

def fill_in_formula(formula):
  letters = ''.join(set(re.findall('[A-Z]', formula)))
  for digits in itertools.permutations('0123456789', len(letters)):
    table = string.maketrans(letters, ''.join(digits))
    yield formula.translate(table)

def valid(f):
  """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
  try:
    return not re.search(r'\b0[0-9]', f) and eval(f) is True
  except ArithmeticError:
    return False

def faster_solve(formula):
  letters,compiled = compile_formula(formula)
  for digits in itertools.permutations(range(10), len(letters)):
    try:
      if compiled(*digits):
        table = string.maketrans(letters, ''.join(map(str, digits)))
        return formula.translate(table)
    except ArithmeticError:
      pass;


def compile_formula(formula, verbose=True):
  letters = ''.join(set(re.findall('[A-Z]', formula)))
  parameters = ','.join(letters)
  tokens = map(compile_word, re.split('([A-Z]+)', formula))
  body = ''.join(tokens)

  firstletters = set(re.findall(r'\b([A-Z])[A-Z]+', formula))
  if firstletters:
    tests = ' and '.join(L + '!=0' for L in firstletters)
    body = '%s and %s' % (tests, body)
  f = 'lambda %s:%s' %(parameters, body)

  if verbose:
    print f
  return letters, eval(f)

def compile_word(word):
  if word.isupper():
    terms = [ ('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
    return '(' + '+'.join(terms) + ')'
  return word;


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def timedcall(fn, *args):
  t0 = time.clock();
  result = fn(*args)
  t1 = time.clock()
  return t1 - t0, result

def test(solve):
  t0 = time.clock();
  for example in examples:
    print 13 * ' ', example
    print '%6.4f sec: %s' % timedcall(solve, example)
  print '%6.4f tot:' % (time.clock() - t0)


test(faster_solve)