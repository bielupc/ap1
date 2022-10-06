from sumardigits import suma_digits

def arrel_digital(n: int) -> int:
    """Donat un natural n, retorna la seva arrel digital."""
    
    if n < 10:
        return n
    else:
        return arrel_digital(suma_digits(n))



def main() -> None:
    print(arrel_digital(5618))


if __name__ == "__main__":
    main()
