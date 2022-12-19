from yogi import read, scan, tokens


def files(M: list[list[int]]) -> bool:
  for j in range(9):
    vists: list[int] = list()
    for i in range(9):
      if M[i][j] in vists:
        return False
      else:
        vists.append(M[i][j]) 
  return True


def columnes(M: list[list[int]]) -> bool:
  for i in range(9):
    vists: list[int] = list()
    for j in range(9):
      if M[i][j] in vists:
        return False
      else:
        vists.append(M[i][j])
  return True


def quadrat_be(M: list[list[int]]) -> bool:
  nums = [x for x in range(1, 10)]
  seen = [0 for y in range(9)]

  for i in range(3):
    for j in range(3):
      if M[i][j] in seen:
        return False
      else:
        nums.remove(M[i][j])
        seen.append(M[i][j])
  return True




def quadrats(M: list[list[int]]) -> bool:

  L = [
  [[M[i][j] for j in range(3)] for i in range(3)],
  [[M[i][j] for j in range(3, 6)] for i in range(3)],
  [[M[i][j] for j in range(6, 9)] for i in range(3)],


  [[M[i][j] for j in range(3)] for i in range(3, 6)],
  [[M[i][j] for j in range(3, 6)] for i in range(3, 6)],
  [[M[i][j] for j in range(6, 9)] for i in range(3, 6)],


  [[M[i][j] for j in range(3)] for i in range(6, 9)],
  [[M[i][j] for j in range(3, 6)] for i in range(6, 9)],
  [[M[i][j] for j in range(6, 9)] for i in range(6, 9)]
  ]


  for q in L:
    if not quadrat_be(q):
      return False
  return True



def solucio(M: list[list[int]]) -> bool:
  return files(M) and columnes(M) and quadrats(M)


def main() -> None:
  n = read(int)
  for _ in range(n):
    M = [[read(int) for _ in range(9)] for _ in range(9)]

    if solucio(M):
      print("yes")
    else:
      print("no")


if __name__ == "__main__":
  main()