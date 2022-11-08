from yogi import read

def bars2(n: int) -> None:
    if n == 1:
        print("*")
    else:
        print(n * "*")
        bars2(n - 1)
        bars2(n - 1)

def main() -> None:
    n = read(int)
    bars2(n)

if __name__ == "__main__":
    main()
