from yogi import read, scan


def appearance(M: list[list[int]]) -> bool:
  n = len(M)
  nums = [x for x in range(1, (n**2) + 1)]
  seen: list[int] = list()

  for i in range(n):
    for j in range(n):
      if M[i][j] in seen:
        return False
      else:
        nums=[k for k in nums if k!= M[i][j]]
        seen.append(M[i][j])
  return True

def rows(M: list[list[int]]) -> bool:
  n = len(M)

  for j in range(n):
    suma = 0
    for i in range(n):
      suma += M[i][j]
    if suma != 15:
      return False
  return True

def columns(M: list[list[int]]) -> bool:
  n = len(M)

  for i in range(n):
    suma = 0
    for j in range(n):
      suma += M[i][j]
    if suma != 15:
      return False
  return True

def diagonals(M: list[list[int]]) -> bool:
  n = len(M)
  diagonal1 = sum([M[i][i] for i in range(n)])
  diagonal2 = sum([M[n - 1 - i][i] for i in range(n)])
  return diagonal1 == 15 and diagonal2 == 15



def is_magic(M: list[list[int]]) -> bool:
  return appearance(M) and rows(M) and columns(M) and diagonals(M)


def main() -> None:
  n = scan(int)
  while n is not None:
    M = [[read(int) for _ in range(n)] for _ in range(n)]
    if is_magic(M):
      print("yes")
    else:
      print("no")
    n = scan(int)


if __name__ == "__main__":
  main()