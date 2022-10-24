def es_primer(x: int) -> bool:

    if x <= 1:
        return False
    else:
        c = 2
        while c*c <= x:
            if x % c == 0:
                return False 
        return True

def garabell(n: int) -> list[bool]:
    """Retorna una llista L de n+1 posicions tal que L[i] és
       cert si i nomes si i es un nombre primer
    """
    L = [True for i in range(n+1)]
    L[0] = False
    L[1] = False

    i = 2
    while i * i <= n:
        if L[i]:
            for j in range(2 * i, n + 1, i):
                L[j] = False
        i += 1
    return L

def llista_primers(n: int) -> list[int]:
    """Retorna la llista de tots els primers fins a n. Per n >= 0."""

    # primers: list[int] = [] # LLista buida amb especificació de tipus

    primers = garabell(n)
    return [x for x in range(n + 1) if primers[x]]
