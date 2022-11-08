from yogi import scan


def is_prime(n: int) -> bool:
    d = 2

    if n == 1 or n == 0:
        return False
    else:
        while d * d <= n:
            if n % d == 0:
                if d != 1 and d != n or n // d != 1 and n // d != n:
                    return False
            else:
                d += 1
        return True
    

def main() -> None:
    n = scan(int)

    while n is not None and is_prime(n):
        while True:
            n += 1
            if is_prime(n):
                print(n)
                break
        n = scan(int)



if __name__ == "__main__":
    main()
