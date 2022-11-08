from yogi import read



def main() -> None:
    n = read(int)
    b = read(int)
    r = n % b
    q = n // b

    print("----------")
    while q != n:
        print("X" * r)
        n = q
        r = n % b
        q = n // b
    print("----------")

if __name__ == "__main__":
    main()
