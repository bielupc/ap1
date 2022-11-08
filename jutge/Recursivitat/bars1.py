from yogi import read

def bars(n: int) -> None:
    if n == 1:
        print("*")
    else:
        bars(n - 1)
        print("*" * n)
        bars(n - 1)

def main() -> None:
    n = read(int)
    bars(n)
if __name__ == "__main__":
    main()
