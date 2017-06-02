#!/usr/bin/env python

# DENOMINATIONS = [1, 5, 10, 25]
DENOMINATIONS = [25, 10, 5, 1]

def change(n, ways):
  return r_change(n, [], ways)

def r_change(n, combination, ways):
  
  if n < 0:
    return 0
  elif n == 0:
    if combination in ways:
      return 0
    ways.append(combination)
    return 1

  ways_to_change = 0
  for denomination in DENOMINATIONS:
    new_combo = combination[:] + [denomination]
    new_combo.sort()
    ways_to_change += r_change(n - denomination, new_combo, ways)
    
  return ways_to_change

if __name__ == '__main__':
  n = 40
  ways = []
  print "Solution: {0}".format(change(n, ways))
  print "Ways:"
  for way in ways:
    print ','.join([str(x) for x in way])
