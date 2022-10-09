from typing import Optional

def semiprimalitat(n: int) -> Optional[tuple[int, int]]:
    d = 2
    while d * d <= n:
        if n % d == 0:
            b = n // d
            d2 = 2
            while d2 * d2 <= b:
                if b % d2 == 0:
                    return None
                else:
                    d2 += 1
            return (d, b)
        else:
            d += 1
    return None


