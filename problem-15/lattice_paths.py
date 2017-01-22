#!/usr/bin/env python

def num_paths(n):
  """Compute number of paths for lattice NxN"""
  return r_num_paths(n, 0, 0)

CACHE = {}
CACHE_HITS = [0]

def r_num_paths(n, x, y):
  """Compute number of paths for lattice NxN starting from point (x, y)"""
  
  cache_key = "n{0}_x{1}_y{2}".format(n, x, y)
  if cache_key in CACHE:
    CACHE_HITS[0] += 1
    # print "Cache hit: {0} -> {1}".format(cache_key, CACHE[cache_key])
    return CACHE[cache_key]

  # We have reached bottom-right corner: add current path to the list of paths
  # and return
  if x == n and y == n:
    return 1

  n_paths = 0
  # Current path: add move to the right and compute paths for point (x+1, y)
  if x < n:
    n_paths += r_num_paths(n, x + 1, y)
  # Current path: add move down and compute paths for point (x, y+1)
  if y < n:
    n_paths += r_num_paths(n, x, y + 1)

  # Cache number of paths from point (x, y)
  # print "Path computed: {0} -> {1}".format(cache_key, n_paths)
  CACHE[cache_key] = n_paths
  return n_paths

if __name__ == '__main__':
  n = 20
  print "Solution: {0}".format(r_num_paths(n, 0, 0))
  print "Cache hits: {0}".format(CACHE_HITS[0])
