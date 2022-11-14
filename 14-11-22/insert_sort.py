import itertools, time, random
from yogi import tokens
from typing import Any


def insereix(L: list[Any], i: int) -> None:
    """
       Insereix l'element L[i] en la llista L[:i+1]
       Sabent que L[:i] està ordenada.
    """
    x = L[i]
    j = i - 1
    while j >= 0 and L[j] > x:
        L[j + 1] = L[j]
        j -= 1
    L[j + 1] = x

def ordena_ins(L: list[Any]) -> None:
    n = len(L)
    for i in range(1, n):
        insereix(L, i)

def main():
    L = list(tokens(int))
    ordena_ins(L)


if __name__ == "__main__":
    main()
