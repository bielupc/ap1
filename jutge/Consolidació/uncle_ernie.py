from yogi import scan 


def main() -> None:
    n = scan(int)
    while n is not None:
        print(((((n // 5) - 9) // 4) - 6) // 5)
        n = scan(int)

if __name__ == "__main__":
    main()
