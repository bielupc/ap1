from yogi import tokens, read, scan




def genrear_permutacions(n: int) -> None:
    L = [-1 for _ in range(n)]
    usats = [False for _ in range(n+1)]
    genrear_permutacions_rec(n, L, usats, 0)




def genrear_permutacions_rec(n: int, L: list[int], usats: list[bool], i: int) -> None:
    if n == i:
        print("(", ','.join([str(x) for x in L]),")", sep="")
    else:
        for j in range(1, n+1):
            if not usats[j]:
                L[i] = j
                usats[j] = True
                genrear_permutacions_rec(n, L, usats, i+1)
                usats[j] = False






def main() -> None:
    n = read(int)
    genrear_permutacions(n)


if __name__ == "__main__":
    main()
