from yogi import read, scan, tokens

def es_primer(n: int) -> bool:
    if n <= 1:
        return False
    else:
        d = 2
        while d*d <= n:
            if n%d == 0:
                return False
            d += 1
        return True

def main() -> None:
    xn = scan(str)
    xn1 = scan(str)
    found = False

    while xn is not None and xn1 is not None:
        if not es_primer(int(xn + xn1)):
            print(xn + xn1)
            found = True
            break
        else:
            xn = xn1
            xn1 = scan(str)
    if not found:
        print("no")

if __name__ == "__main__":
    main()

