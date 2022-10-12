

def hanoi(n: int, ori: str, dst: str, aux: str) -> None:
    """ Mou n discos del piu ori al piu dst passant pel piu aux. Prec: n >= 0."""

    if n > 0:
        hanoi(n - 1, ori, aux, dst)
        print(ori, "->", dst)
        hanoi(n - 1, aux, dst, ori)






hanoi(3, "a", "b", "c")
