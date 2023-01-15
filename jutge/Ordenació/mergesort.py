from yogi import tokens, scan, read



  
def mergesort(v: list[float]) -> None:
  if len(v) == 1:
      return v[0]
  else:
      mid = len(v) // 2
      L = v[:mid]
      R = v[mid:]

      mergesort(L)
      mergesort(V)


def main() -> None:
  l = [2, 4, 5, 7, 4]


if __name__ == "__main__":
  main()