
def suma_digits(n: int) -> int:
    """Donat un natural n, retorna la suma dels seus digits (base 10)."""

    if n < 10:
        return n
    else:
        return n % 10 + suma_digits(n // 10)


def main() -> None:
    print(suma_digits(18))

if __name__ == "__main__":
    main()
