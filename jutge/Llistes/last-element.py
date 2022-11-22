from yogi import read


def main() -> None:
    n = read(int)
    L: list[int] = []

    for i in range(n):
        x = read(int)
        L.append(x)

    l = len(L)
    k = 0
    for j in range(l):
        if L[j] == L[-1]:
            k += 1
    print(k-1)

if __name__ == "__main__":
    main()
