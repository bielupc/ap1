from yogi import read, scan, tokens



def generar_combinacions(n: int) -> None:
    generar_combinacions_rec(n, [-1 for _ in range(n)], 0)

def generar_combinacions_rec(n: int, L: list, i: int) -> None:

    if i == n:
        print(*L)
    else:
        L[i] = 0
        generar_combinacions_rec(n, L, i+1)
        L[i] = 1
        generar_combinacions_rec(n, L, i+1)


def main() -> None:
    n = read(int)
    generar_combinacions(n)





if __name__ == "__main__":
    main()
