from yogi import read, scan, tokens
from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]

def product(a: Matrix, b: Matrix) -> Matrix:
  m = len(a)
  n = len(a[0])

  p = len(b[0])


  M = [[0 for _ in range(p)] for _ in range(m)]
  for i in range(m):
    for j in range(p):
      for k in range(n):
        M[i][j] += a[i][k] * b[k][j]
  return M


