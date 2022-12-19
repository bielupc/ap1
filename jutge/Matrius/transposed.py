from yogi import read, scan, tokens



def transpose(M: list[list[int]]) -> None:
  n = len(M)
  for i in range(n):  
      for j in range(i + 1, n):  
          M[i][j], M[j][i] = M[j][i], M[i][j]
          

def transpose_no_funciona(M: list[list[int]]) -> None:

  n = len(M)
  for i in range(n):
    si = n - 1 - i
    for j in range(i + 1, n):
      sj = n - 1 - j
      M[i][j], M[si][sj] = M[si][sj], M[i][j]


def main() -> None:

  L = [[5, 7, 6, 4, 1, 2], [2, 8, 1, 3, 8, 8], [0, 1, 2, 9, 2, 1], [6, 5, 4, 3, 2, 1]]
  L = [[0, 1], [0, 0]]
  transpose(L)
  print(L)



if __name__ == "__main__":
  main()