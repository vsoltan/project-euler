#!/usr/bin/env python

def num_paths(n):
  """Compute number of paths for lattice NxN"""
  all_paths = []
  r_num_paths(n, 0, 0, [], all_paths)
  return all_paths

RIGHT = 'x'
DOWN = 'y'

def r_num_paths(n, x, y, path, paths):
  """Compute number of paths for lattice NxN starting from point (x, y)"""
  print "Lattice {2}x{2}; Position (x={0}, y={1})".format(x, y, n)
  print "Current path: {0}".format(''.join(path))

  # We have reached bottom-right corner: add current path to the list of paths
  # and return
  if x == n and y == n:
    paths.append(''.join(path))
    print "All paths: {0}".format('\n'.join(paths))
    return

  # Current path: add move to the right and compute paths for point (x+1, y)
  if x < n:
    r_num_paths(n, x + 1, y, path[:]+[RIGHT], paths)
  # Current path: add move down and compute paths for point (x, y+1)
  if y < n:
    r_num_paths(n, x, y + 1, path[:]+[DOWN], paths)

if __name__ == '__main__':
  all_paths = []
  r_num_paths(3, 0, 0, [], all_paths)
  print "Solution:\n{0}, size: {1}".format('\n'.join(all_paths), len(all_paths))
