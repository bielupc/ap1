from yogi import read, tokens, scan



def main() -> None:
    n = read(int)
    L: list[str] = list()
    for _ in range(n):
        w = read(str)
        L.append(w[::-1])

    for i in range(n - 1, -1, -1):
        print(L[i])

if __name__ == "__main__":
    main()
