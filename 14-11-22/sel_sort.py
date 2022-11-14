from yogi import tokens
import itertools
import random
import time
from typing import Any

def posicio_minim(L: list[Any], i: int) -> int:
    """Retorna la posició del mínim de L[i:]."""
    n = len(L)
    p = i
    for j in range(i + 1, n):
        if L[j] < L[p]:
            p = j
    return p

def orderna_sel(L: list[Any]) -> None:
    n = len(L)

    for i in range(n):
        p = posicio_minim(L, i)
        L[i], L[p] = L[p], L[i]

def main2() -> None:
    c = 0
    for n in range(4):
        for permutacio in itertools.permutations(range(n)):
            c += 1
            L =list(permutacio)
            orderna_sel(L)
            if L != list(range(n)):
                print("no", permutacio)
    print(c)

def main1() -> None:
    for n in range(1000, 20000, 1000):
        L = [random.randint(0, n) for _ in range(n)]
        t1 = time.perf_counter()
        orderna_sel(L)
        t2 = time.perf_counter()

        print(n, t2 - t1)



if __name__ == "__main__":
    main1()

