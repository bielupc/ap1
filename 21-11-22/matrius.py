from typing import TypeAlias

m = 2
n = 2
M = [[0 for j in range(n) for i in range(m)]] # Matriu de zeros 2x2

Temperatures: TypeAlias = list[float]

def temperatura_mitana(temperatures: Temperatures) -> float:
  pass

Fila: TypeAlias = list[float]
Matriu: TypeAlias = list[Fila]

def suma(A: Matriu, B: Matriu) -> Matriu:
  m = len(A)
  n = len(A[0])

  return [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

def t(M: Matriu) -> Matriu:
  n = len(M)
  return [[M[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]
