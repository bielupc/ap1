from yogi import read, tokens, scan
from typing import TypeVar,Union


T = TypeVar("T")

def posicio(x: T, v: list[T], left: int, right: int) -> int:
  """Retorna l'index del element que es busca d'un llista ordenada"""

  if left > right:
    return -1

  else:
    mig = (left + right) // 2
    if x > v[mig]:
      return posicio(x, v, mig + 1, right)
    elif x < v[mig]:
      return posicio(x, v, left, mig - 1)
    else:
        return mig



def main() -> None:
  L = [1]
  print(posicio(1, L, 0, len(L) - 1))


if __name__ == "__main__":
  main()
