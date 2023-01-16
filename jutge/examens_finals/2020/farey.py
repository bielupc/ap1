from yogi import read, scan, tokens
from math import floor


def farey(a: int, b: int, c: int, d: int, n: int) -> None:
  x = floor((n+b) / d)
  p = x*c-a
  q = x*d-b

  if 0 <= p/q <= 1 and 1 <= q <= n:
    print(f"{p}/{q}", end=" ")
    a, b = c, d
    c, d = p, q
    farey(a, b, c, d, n)


def main() -> None:
  n = scan(int)
  while n is not None:
    print("0/1", end=" ")
    print(f"1/{n}", end=" ")
    farey(0, 1, 1, n, n)
    print()
    n = scan(int)


if __name__ == "__main__":
  main()