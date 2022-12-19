from yogi import read, scan, tokens


def sum(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
  n = len(a)
  M = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      M[i][j] = a[i][j] + b[i][j]
  return M


