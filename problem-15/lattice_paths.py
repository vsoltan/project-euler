#!/usr/bin/env python

def num_paths(n):
  """Compute number of paths for lattice NxN"""
  # all_paths = []
  # all_paths = [0]
  return r_num_paths(n, 0, 0, [])
  # return all_paths[0]

RIGHT = 'x'
DOWN = 'y'

CACHE = {}

def r_num_paths(n, x, y, path):
  """Compute number of paths for lattice NxN starting from point (x, y)"""
  # print "Lattice {2}x{2}; Position (x={0}, y={1})".format(x, y, n)
  # print "Current path: {0}".format(''.join(path))
  
  # cache_key = "n{0}_x{1}_y{2}".format(n, x, y)
  # if cache_key in CACHE:
  #   paths += CACHE[cache_key]
  #   return

  # We have reached bottom-right corner: add current path to the list of paths
  # and return
  if x == n and y == n:
    # paths.append(''.join(path))
    # paths[0] += 1
    # print "All paths: {0}".format('\n'.join(paths))
    # print '.',
    return 1

  n_paths = 0
  # Current path: add move to the right and compute paths for point (x+1, y)
  if x < n:
    n_paths += r_num_paths(n, x + 1, y, path[:]+[RIGHT])
  # Current path: add move down and compute paths for point (x, y+1)
  if y < n:
    n_paths += r_num_paths(n, x, y + 1, path[:]+[DOWN])

  return n_paths

if __name__ == '__main__':
  # all_paths = [0]
  # all_paths = []
  x = r_num_paths(10, 0, 0, [])
  # print "Solution:\n{0}, size: {1}".format('\n'.join(all_paths), len(all_paths))
  print "Solution: {0}".format(x)
