from yogi import read

def solve_hanoi(n: int, a: int, b: int, c: int) -> None:
    if n == 1:
        print("A => C")
    else:
        if a >= 3:



def main() -> None:
    n = read(int)
    solve_hanoi(a, a, 0, 0)


if __name__ == "__main__":
    main()
