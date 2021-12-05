import numpy as np

def findMatrix(n, m):
  mid_row = n // 2
  mid_col = m // 2
  
  matrix = [ [ np.random.randint(0, 2) for j in range(m)] for i in range(n) ]
  
  # matrix = [
  #   [1,0,0,1,0],
  #   [0,0,1,0,0],
  #   [0,1,0,1,0],
  #   [1,1,0,1,0],
  #   [0,0,0,0,1]
  # ]
  # matrix = [
  #   [1,0,0,1],
  #   [0,0,1,0],
  #   [0,1,0,1],
  #   [1,1,0,1],
  #   [0,0,0,0]
  # ]
  modify_counts = 0
  for i in range(mid_row):
    for j in range(mid_col):
      if matrix[i][j] != matrix[i][m-j-1]:
        modify_counts+=1
        print('ass', i, j)
      
      if matrix[i][j] != matrix[n-i-1][j]:
        print('bss', i, j)
        modify_counts+=1

      if matrix[i][j] != matrix[n-i-1][m-j-1] and m-j-1 != j:
        print('css', i, j)
        modify_counts+=1
  
  if n%2==1: # odd row
    for j in range(mid_col):
      if matrix[mid_row][j] != matrix[mid_row][m-j-1]:
        modify_counts+=1

  
  if m%2==1: # odd col
    for i in range(mid_row):
      if matrix[i][mid_col] != matrix[n-1-i][mid_col]:
        modify_counts+=1

  return modify_counts

print(findMatrix(5, 4))