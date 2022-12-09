from yogi import read, scan, tokens




def generar_combinacions(n: int, o: int) -> None:
    generar_combinacions_rec(n, [-1 for _ in range(n)], 0, o)


def generar_combinacions_rec(n: int, L: list, i: int, n0: int) -> None:

    if n0 >= 0 and n0 <= n - i:
        if i == n:
            print(*L)
        else:
            L[i] = 0
            generar_combinacions_rec(n, L, i+1, n0)

            L[i] = 1
            generar_combinacions_rec(n, L, i+1, n0-1)


def main() -> None:
    n = read(int)
    o = read(int)


    generar_combinacions(n, o)


if __name__ == "__main__":
    main()
