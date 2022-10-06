from typing import Optional


def semiprimalitat(n: int) -> Optional[tuple[int, int]]:
    """Retorna una tupla amb els primers que multiplicats donen n o none si no es semiprimer"""  
    factors = []

    d = 2
    ctl = 0

    while d <= n:
        if ctl <= 2:
            
            if n%d == 0:

                n //= d

                factors.append(d)
                ctl += 1
            else:
                d += 1
        else:
            return None
    if ctl == 2:
        return factors[0], factors[1]
    else:
        return None







