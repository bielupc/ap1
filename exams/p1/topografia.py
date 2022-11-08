from yogi import read, scan, tokens

def perfil(r: int, n: int, r0: int, n0: int) -> None:
    print("X" * (r0 + r), end="")
    print("." * (n0 + n), end="")
    print()

def main() -> None:
    r = scan(int)
    n = scan(int)
    r0 = 0
    n0 = 0

    while r is not None and n is not None:
        if (r + r0) < 0 or (n + n0) < 0:
            print("ERROR")
            break
        else:
            perfil(r, n, r0, n0)
            r0 += r
            n0 += n
            r = scan(int)
            n = scan(int)

if __name__ == "__main__":
    main()
