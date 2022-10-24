import math


def producte_escalar(x: list[float], y: list[float]) -> float:
    """Retorna el producte escalar de dos vectors x i y de la mateixa mida"""
    s = 0.
    n = len(x)
    for i in range(n):
        s += x[i] * y[i]
    return s

def modul(x: list[float]) -> float:
    """Retorna el mòdul d'un vector x"""
    return math.sqrt(producte_escalar(x, x))

def perpendiculars(x: list[float], y: list[float]):
    """Diu si x i y son vectors perpendiculars"""
    return abs(producte_escalar(x, y)) < 1e-12

def doblar(x: list[float]) -> None:
    """Dobla el valor dels components de x"""
    # Llista = objecte, s'emmagetzemen amb referencies
    n = len(x)
    for i in range(n):
        x[i] = x[i] * 2

def afegeix_suma(L: list[int]) -> None:
    """Afegeix a L un element al final que és la suma dels elements en L"""
    L.append(sum(L))
    

def main() -> None:
    producte_escalar([1, 2, 3], [4, 5, 6])

if __name__ == "__main__":
    main()
