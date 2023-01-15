from yogi import read, scan, tokens

def posicio_minim(v: list[float], i: int) -> int:
  n = len(v)
  p = i
  for j in range(i+1, n):
    if v[j] < v[p]:
      p = j
  return p

def selsort(v: list[float]) -> None:
  n = len(v)
  for i in range(n):
    p = posicio_minim(v, i)
    v[i], v[p] = v[p], v[i]


def main():
  L = [2, 1, 6, 4, 5, 3]
  print(selsort(L))



if __name__ == "__main__":
  main()