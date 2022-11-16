from yogi import tokens
import itertools
import random
import time
from typing import Any, TypeVar

T = TypeVar("T")


def mergesort(L: list[Any]) -> None:
    """Ordena la llista L per fusió"""
    mergesort_rec(L, 0, len(L) - 1)


def mergesort_rec(L: list[Ant], esq: int, dre: int) -> None:
    """Ordena L[esq..dre]."""

    if esq < dre:
        mig = (esq + dre) // 2
        mergesort_rec(L, esq, mig)
        mergesort_rec(L, 1 + mig, dre)
        merge(L, esq, mig, dre)


def merge(L: list[T], esq: int, mig: int, dre: int) -> None:
    """
    Ordena L[esq..dre] sabent que L[esq..mig] està ordenat i sabent que 
    L[mig + 1..dre] està ordenat.
    """
    R: list[T] = list()
    i = esq
    j = mig + 1
    while i <= mig and j <= dre:
        if L[i] <= L[j]:
            R.append(L[i])
            i += 1
        else:
            R.append(L[j])
            j += 1

    R.extend(L[i:mig+1])
    R.extend(L[j:dre+1])
    L[esq:dre+1] = R


def main() -> None:
    pass


if __name__ == "__main__":
    main()
