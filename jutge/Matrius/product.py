from yogi import read, scan, tokens
from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]

def product(a: Matrix, b: Matrix) -> Matrix:
  n = len(a)
  M = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        M[i][j] += a[i][k] * b[k][j]
  return M


