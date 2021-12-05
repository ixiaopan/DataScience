def lumen(n, l, maps):
  grid = [ [1]*n for i in range(n) ]

  for i in range(n):
      for col, cell in enumerate(maps[i]):
          if cell == 'C':
              # https://www.xarg.org/puzzle/codingame/lumen/
              # np.array([
              #   [ # distance from the cell to the light
              #     max(0, l - max(abs(i - r), abs(col - j))) for j in range(n)
              #   ] for r in range(n)
              # ])

              for r in range( max(0, i-l+1), min(n, i+l) ):
                  for j in range(l):
                      grid[r][ min(n-1, col + j) ] = 0
                      grid[r][ max(0, col - j) ] = 0

  return sum([sum(x) for x in grid])


# X X X X X
# X C X X X
# X X X X X
# X X X X X
# X X X X X
n=5
maps = [ ['X']*n for i in range(n) ]
maps[1][1] = 'C'
assert lumen(n, 3, maps) == 9
