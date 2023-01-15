
def insertion_sort(v: list[float]) -> None:
  s: list[float] = list()

  for x in v:
    n = len(s)
    s.append(x)
    i = n

    while i > 0 and s[i-1] > s[i]:
      s
      i -= 1




def main() -> None:
  L = [3, 6, 1, 7, 1]
  print(insertion_sort(L))


if __name__ == "__main__":
  main()