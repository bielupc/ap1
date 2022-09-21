def max2(a:int, b:int) -> int:
    """Retorna el màxim entre dos nombres"""
    if a > b:
        return a
    else:
        return b


def max4(a:int, b:int, c:int, d:int) -> int:
    x = max2(a, b)
    y = max2(c, d)

    if x > y:
        return x
    else:
        return y
