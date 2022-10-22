from yogi import tokens
from math import sqrt, floor


def quadrat_perfecte(n: int) -> bool:
    """Retorna si un nombre n és un quadrat perfecte"""
    return floor(sqrt(n)) ** 2 == n

def divisors(n: int) -> None:
    """Fa un print dels divisors ordenats d'un natural n entre 1 i 10⁹."""

    if n == 1:
        print("divisors of 1: 1")

    else:

        print(f"divisors of {n}:", end="")

        # Primer bucle pels divisors fins l'arrel.
        divisor_petit = 1

        while divisor_petit*divisor_petit <= n:
            if n%divisor_petit == 0:
                print(f" {divisor_petit}", end="")
            divisor_petit += 1

        # Segon bucles pels divisors més grans que l'arrel.
        divisor_gran = floor(sqrt(n)) # sqrt(n) sempre retorna un float, però n sempre és natural, doncs emprem floor().
    
        # Si n es un quadrat perfecte ja hem trobar el primer divisor abans
        if quadrat_perfecte(n):
            divisor_gran -= 1

        while divisor_gran >= 1: # Iterem de l'arrel fins a l'u perquè quedin ordenats.
            if n%divisor_gran == 0:
                print(f" {floor(n//divisor_gran)}", end="")
            divisor_gran -= 1

        # Salt de línia per la següent seqüència de divisors.
        print()

def main() -> None:
    # Apliquem la funció per trobar divisors per cada input vàlid.
    for n in tokens(int):
        divisors(n)

if __name__ == "__main__":
    main()

