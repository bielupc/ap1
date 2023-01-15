from yogi import scan


def are_primes(m: int, n: int) -> bool:
    """
    Donats dos naturals m i n >= 2, retorna si els dos elements de
    la parella són primers o no.
    """
    d = 2
    x = max(n, m)
    while d*d <= x:
      if n % d == 0 or m % d == 0:
        return False 
      else:
        d += 1
    return True


def nth_twin_primes(n: int) -> tuple[int, int]:
    """
    Donat un natural n >= 1, retorna una tupla amb la n-parella de 
    primers bessons.
    """
    # Partim de la parella inicial de primers bessons
    p = 3
    q = 5

    i = 1
    trobat = False

    while not trobat:
        if are_primes(q, p) and q == p+2:
            if i == n: # Si és l'index que buscavem...
                trobat = True
                break
            else:
                i += 1
        # Busquem per una nova parella de nombres
        p += 1
        q += 1
        
    return p, q


def main() -> None:
    n = scan(int)
    while n is not None:
        result = nth_twin_primes(n)
        print(result[0], result[1])
        n = scan(int)


if __name__ == "__main__":
    main()