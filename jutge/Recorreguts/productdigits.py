from yogi import tokens

def producte_digits(n: int) -> int:
    """Retorna el producte dels digits de un natural N"""
    if n < 10:
        return n
    else:
        return n % 10 * producte_digits(n // 10)

def main() -> None:

    for number in tokens(int):
        if number < 10:
            print(f"The product of the digits of {number} is {number}.")
        ctl = number
        while ctl >= 10:
            res = producte_digits(ctl)
            print(f"The product of the digits of {ctl} is {res}.")
            ctl = res
        print("----------")

if __name__ == "__main__":
    main()
