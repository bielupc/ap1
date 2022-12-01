import yogi


def generar_permutacions(n: int) -> None:
  generar_permutacions_rec(n, [])


def generar_permutacions_rec(n: int, L: list[int]) -> None:
  if n == len(L):
    print(*L)
  else:
    for k in range(n):
      if k not in L:
        generar_permutacions_rec(n, L + [k])


def main() -> None:
  n = yogi.read(int)
  generar_permutacions(n)


if __name__ == "__main__":
  main()