from typing import TypeVar

T = TypeVar("T")


def fusio(L1: list[T], L2: list[T]) -> list[T]:
    n1, n2 = len(L1), len(L2)
    i1, i2 = 0, 0
    R: list[T] = list()

    while i1 < n1 and i2 < n2:
        if L1[i1] <= L2[i2]:
            R.append(L1[i1])
            i1 += 1
        else:
            R.append([L2[i2]])
            i2 += 1
    R.extend(L1[i1:])
    R.extend(L2[i2:])

    return R
