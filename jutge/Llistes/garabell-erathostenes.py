from yogi import tokens


def garabell(n: int):
    L = [True for x in range(n)]
    L[0] = L[1] = False
    i = 2
    while i * i <= n:
        if not L[i]:
            for j in range(2 * i, n + 1, i):
                L[j] = False
        i += 1
    return L

def main() -> None:
    L = garabell(10**6)
    for i in tokens(int):
        if L[i]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
