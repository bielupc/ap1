from yogi import read, scan, tokens


def selsort(v: list[float]) -> None:
  for i, n in enumerate(v):
    min = n
    for j,m in enumerate(v[i::]):
      if m < min:
        min = m
        idx = j
    v[i], v[v.index(min)] = v[v.index(min)], v[i]

  return v


def main():
  L = [2, 1, 6, 4, 5, 3]
  print(selsort(L))



if __name__ == "__main__":
  main()