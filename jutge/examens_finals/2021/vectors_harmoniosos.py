from yogi import read, scan, tokens

c = 0

def generar_vectors(n: int, d: int) -> int:
  global c
  c = 0
  generar_vectors_rec(n, d, 0, 0, 0, [-1 for x in range(n)])
  return c


def generar_vectors_rec(n: int, d: int, n1: int, n0: int, i: int, v: list[int]) -> None:
  global c
  if n0 + n1 < n and abs(n0 - n1) <= d:
    v[i] = 0
    generar_vectors_rec(n, d, n1, n0 + 1, i+1, v)

    v[i] = 1
    generar_vectors_rec(n, d, n1 + 1, n0, i+1, v)

  else:
    if n0 + n1 == n and abs(n0 - n1) <= d:
      c += 1
      
   

def main() -> None:
  n = scan(int)
  d = scan(int)
  while n is not None and d is not None:
    print(generar_vectors(n, d))
    n = scan(int)
    d = scan(int)


if __name__ == "__main__":
  main()