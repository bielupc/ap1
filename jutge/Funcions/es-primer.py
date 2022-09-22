
def es_primer(n:int) -> bool:
    """Troba si un nombre n es primer"""
    d = 2
    while d * d <= n:
        if n % d == 0:
            if (d != 1 and d != n ) or (n//d != 1 and n//d != n):
                return False
        d += 1
    return True




