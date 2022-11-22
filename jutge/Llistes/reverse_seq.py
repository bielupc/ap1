from yogi import read, scan, tokens
from typing import List

def main() -> None:
    n = scan(int)
    while n is not None:
        L: list[int] = list()
        for _ in range(n):
            i = read(int)
            L.append(i)
        print(*L[::-1])
        n = scan(int)

if __name__ == "__main__":
    main()
