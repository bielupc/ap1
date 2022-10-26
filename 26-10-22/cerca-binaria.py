from typing import Optional, Union

def cerca(L: list[int], x: int) -> Union[int, None]: # -> int | None també és vàlid
    """
    Si x és a L, retorna una posició i tal que L[i] = x.
    Si x no és a L, retorna None.
    """
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return None

def cerca_binaria(L: list[int], x: int) -> Optional[int]:
    """
    Si x és a L, retorna una posició i tal que L[i] = x.
    Si x no és a L, retorna None.

    Prec: L està ordenada.
    """
    n = len(L)
    esq, dre = 0, n-1

    while esq <= dre:
        mig = (esq + dre) // 2
        if x < L[mig]:
            dre = mig - 1
        elif x > L[mig]:
            esq = mig + 1
        else:
            return mig
    return None




