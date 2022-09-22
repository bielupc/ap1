def sum_divisors(n:int) -> int:
    """Retorna el sumatori de tots els divisors d'un nombre n"""
    d = 1
    res = 0
    while d*d < n:
        if n % d == 0:
            res += d
            res += n//d
        d += 1

    if d*d == n:
        res += d
    return res

