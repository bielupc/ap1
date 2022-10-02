from typing import Optional

def factor_mes_petit(n:int) -> Optional[int]:
    """Donat un natural >=2 retrona none si es primer retorna el factor més petit"""
    d = 2
    while d*d <= n:
        if n % d == 0:
            if d == n  or n//d == n:
                return None
            else:
                return d
        else:
            d += 1
    return None
    
