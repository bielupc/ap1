from yogi import scan


def main() -> None:
    a = scan(float)
    b = scan(float)
    k = scan(float)

    while a is not None and b is not None and k is not None:
        denom = a
        sum = 0.
        i = 0
        while denom <= b:
            denom = a + i * k
            sum += 1/denom
            i += 1
            print(f"1/{denom}")
        print(sum)

        a = scan(float)
        b = scan(float)
        k = scan(float)

if __name__ == "__main__":
    main()
