from yogi import read

def bars3(n: int) -> None:
    if n == 1:
        print("*")
    else:
        bars3(n - 1)
        bars3(n - 1)
        print(n * "*")

def main() -> None:
    n = read(int)
    bars3(n)

if __name__ == "__main__":
    main()
