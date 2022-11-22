from yogi import read, tokens, scan


def main() -> None:
    n = read(int)
    L: list[int] = list()
    c = 1

    for m in tokens(int):
        L.append(m)
    L.sort()

    for i in range(1, n+1):
        if i == n:
            if L[i - 1] == L[i - 2]:
                print(f"{L[i - 1]} : {c}")
            else:
                print(f"{L[i - 1]} : 1")

        else:
            if L[i] == L[i - 1]:
                c += 1
            else:

                print(f"{L[i - 1]} : {c}")
                c = 1


if __name__ == "__main__":
    main()
