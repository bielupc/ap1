from yogi import read, scan, tokens



def position_maximum(v: list[float], m: int) -> int:
  max_ = v[0]
  for i in range(1, m + 1):
    print(v[i])
    print(max_)
    if v[i] > max_:  
      max_ = v[i]

  return v.index(max_)


def main() -> None:
  L = [1., 3., 5., 2., 1.]
  print(position_maximum(L, 4))

if __name__ == "__main__":
  main()