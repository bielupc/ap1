from yogi import scan, tokens, read


def is_prime(n: int) -> bool:
    d = 2

    if n == 1 or n == 0:
        return False
    else:
        while d * d <= n:
            if n % d == 0:
                if (d != 1 and d != n) or (n // d != 1 and n//d != n):
                    return False
            else:
                d += 1

        return True

def main() -> None:

    t = read(int)

    for i in range(t):
        n = read(int)

        if is_prime(n):
           print(f"{n} is prime")
        else:
            print(f"{n} is not prime")


if __name__ == "__main__":
    main()

