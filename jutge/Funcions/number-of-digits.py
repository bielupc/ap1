
def number_of_digits(n:int) -> int:
    """Retorna el nombre de digits d'un nombre n"""
    if n == 0:
        return 1
    else:
        d = 0
        while n != 0:
            d += 1
            n //= 10
    return d


